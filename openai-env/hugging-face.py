# Firts, run following commands to install libraries

# terminal
# pip install --upgrade "diffusers[torch]"
# pip install transformers

# colab
# !pip install --upgrade diffusers(torch)
# !pip install transformers

# import pretrained deffusion model
from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
pipeline("An image of a squirrel in Picasso style").images[0]


# useage example
# pip install gradio
import gradio as gr
from gradio import mix 

title = 'gpt-2'
