# 1. Hugging Face LLMs
import os
from typing import List, Optional

from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI

HF_TOKEN: Optional[str] = os.getenv("HUGGING_FACE_TOKEN")

# Initialize Hugging Face LLM to run locally
# This uses https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha
# downloaded (if first invocation) to the local Hugging Face model cache,
# and actually runs the model on your local machine's hardware
locally_run = HuggingFaceLLM(model_name="HuggingFaceH4/zephyr-7b-alpha")

# Initialize Hugging Face Inference API to run the model remotely on Hugging Face's servers
# Note that using your token will not charge you money,
# the Inference API is free it just has rate limits
# remotely_run = HuggingFaceInferenceAPI(
#     model_name="HuggingFaceH4/zephyr-7b-alpha", token=HF_TOKEN
# )

# Or you can skip providing a token, using Hugging Face Inference API anonymously
# remotely_run_anon = HuggingFaceInferenceAPI(
#     model_name="HuggingFaceH4/zephyr-7b-alpha"
# )

# If you don't provide a model_name to the HuggingFaceInferenceAPI,
# Hugging Face's recommended model gets used (thanks to huggingface_hub)
# remotely_run_recommended = HuggingFaceInferenceAPI(token=HF_TOKEN)

# Generate a completion using the locally run model
completion_response = locally_run.complete("To infinity, and")
print(completion_response)

# 2. PII Masking
# Import necessary libraries for logging
import logging
import sys

# Set up basic logging configuration to output to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Import required modules from llama_index
from llama_index.core.postprocessor import PIINodePostprocessor
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.schema import TextNode, NodeWithScore
from llama_index.core import Document, VectorStoreIndex

# Load and define the document with PII
text = """
Hello Paulo Santos. The latest statement for your credit card account \
1111-0000-1111-0000 was mailed to 123 Any Street, Seattle, WA 98109.
"""
node = TextNode(text=text)

# Initialize the PII Node Postprocessor with the Hugging Face LLM
processor = PIINodePostprocessor(llm=locally_run)

# Create NodeWithScore instance and postprocess the node to redact PII
new_nodes = processor.postprocess_nodes([NodeWithScore(node=node)])

# View the redacted text
redacted_text = new_nodes[0].node.get_text()
print("Redacted Text:", redacted_text)

# Get the PII mapping from the node's metadata (this metadata is not sent to the LLM)
pii_mapping = new_nodes[0].node.metadata["__pii_node_info__"]
print("PII Mapping Metadata:", pii_mapping)

# Feed the processed nodes into the VectorStoreIndex
index = VectorStoreIndex([n.node for n in new_nodes])

# Query the index to retrieve specific information
response = index.as_query_engine().query("What address was the statement mailed to?")
print("Query Response:", str(response))
