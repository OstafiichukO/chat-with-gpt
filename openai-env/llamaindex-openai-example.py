# article link: https://docs.llamaindex.ai/en/latest/examples/node_postprocessor/PII/

# Import necessary libraries
import logging
import sys

# Set up basic logging configuration to output to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Import required modules from llama_index
from llama_index.core.postprocessor import (PIINodePostprocessor)
from llama_index.llms.openai import OpenAI
from llama_index.core.schema import TextNode, NodeWithScore
from llama_index.core import Document, VectorStoreIndex

# Load and define the document
text = """
Hello Paulo Santos. The latest statement for your credit card account \
1111-0000-1111-0000 was mailed to 123 Any Street, Seattle, WA 98109.
"""
node = TextNode(text=text)

# Initialize the PII Node Postprocessor with the OpenAI LLM
processor = PIINodePostprocessor(llm=OpenAI())

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

# Query the index
response = index.as_query_engine().query("What address was the statement mailed to?")
print("Query Response:", str(response))
