from typing import List, Optional
from transformers import pipeline, Pipeline

# Function to load the token classification model
def load_model(model_tag: str, use_gpu: bool = False) -> Optional[Pipeline]:
    """
    Load a token classification model from Hugging Face's model hub.

    Parameters:
    - model_tag (str): The identifier for the pre-trained model.
    - use_gpu (bool): Flag to use GPU if available.

    Returns:
    - Optional[Pipeline]: A Pipeline object for the model if loaded successfully, otherwise None.
    """
    device = 0 if use_gpu else -1  # Determine device: 0 for GPU, -1 for CPU
    try:
        # Load the model and tokenizer
        model = pipeline("token-classification", model=model_tag, tokenizer=model_tag, device=device)
        return model
    except Exception as e:
        print(f"Error loading Model: \n\n{e}")
        return None

# Function to create a mapping of entities to their entity groups from model output
def create_entity_map(model_output: List[dict], text: str) -> dict:
    """
    Create a mapping of entities to their entity groups from the model output.

    Parameters:
    - model_output (List[dict]): List of token classification results from the model.
    - text (str): The original text that was classified.

    Returns:
    - dict: A dictionary mapping entities to their entity groups.
    """
    entity_map = {}  # Initialize an empty dictionary
    for token in model_output:
        start = token["start"]  # Start position of the entity in the text
        end = token["end"]  # End position of the entity in the text
        entity = text[start: end]  # Extract the entity from the text
        entity_map[entity] = token["entity_group"]  # Map the entity to its group
    return entity_map

# Function to replace entities in the text with their corresponding entity group tags
def replace_entities(text: str, entity_map: dict) -> str:
    """
    Replace entities in the text with their corresponding entity group tags.

    Parameters:
    - text (str): The original text.
    - entity_map (dict): Mapping of entities to their entity groups.

    Returns:
    - str: The text with entities replaced by their entity group tags.
    """
    for word in entity_map:
        if word in text:
            text = text.replace(word, f"[{entity_map[word]}]")  # Replace entity with its tag
    return text

# Function to mask PII in the input sentence using the loaded model
def mask_pii(input_sentence: str, anonymizer: Pipeline) -> Optional[str]:
    """
    Mask PII in the input sentence using the loaded model.

    Parameters:
    - input_sentence (str): The sentence to be anonymized.
    - anonymizer (Pipeline): The loaded token classification model.

    Returns:
    - Optional[str]: The sentence with PII masked or None if the output is not as expected.
    """
    output = anonymizer(input_sentence, aggregation_strategy="simple")  # Get model's output
    if isinstance(output, list):
        entity_map = create_entity_map(output, input_sentence)  # Create entity map from the output
        return replace_entities(input_sentence, entity_map)  # Replace entities in the text
    else:
        print("Output is not in the expected format")
    return None

# Example usage:
# Step 1: Load the anonymizer model using `load_model`
anonymizer_model = load_model("Isotonic/distilbert_finetuned_ai4privacy_v2")

# Step 2: Check if the model is loaded successfully
if anonymizer_model:
    # Step 3: Mask PII in a sample sentence using `mask_pii`
    masked_text = mask_pii("My name is Sarah Jessica Parker but you can call me Jessica", anonymizer_model)
    
    # Step 4: Print the masked text
    print(masked_text)
