from typing import List, Optional
from transformers import pipeline, Pipeline


def load_model(model_tag: str, use_gpu: bool = False) -> Optional[Pipeline]:
    device = 0 if use_gpu else -1
    try:
        model = pipeline("token-classification", model=model_tag, tokenizer=model_tag, device=device)
        return model
    except Exception as e:
        print(f"Error loading Model: \n\n{e}")
        return None


def create_entity_map(model_output: List[dict], text: str) -> dict:
    entity_map = {}
    for token in model_output:
        start = token["start"]
        end = token["end"]
        entity = text[start: end]
        entity_map[entity] = token["entity_group"]
    return entity_map


def replace_entities(text: str, entity_map: dict) -> str:
    for word in entity_map:
        if word in text:
            text = text.replace(word, f"[{entity_map[word]}]")
    return text


def mask_pii(input_sentence: str, anonymizer: Pipeline) -> Optional[str]:
    output = anonymizer(input_sentence, aggregation_strategy="simple")
    if isinstance(output, list):
        entity_map = create_entity_map(output, input_sentence)
        return replace_entities(input_sentence, entity_map)
    else:
        print("Output is not in the expected format")
    return None


# Example usage:
anonymizer_model = load_model("Isotonic/distilbert_finetuned_ai4privacy_v2")
if anonymizer_model:
    masked_text = mask_pii("My name is Sarah Jessica Parker but you can call me Jessica", anonymizer_model)
    print(masked_text)