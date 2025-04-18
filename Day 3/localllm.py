import os
from transformers import AutoTokenizer , AutoModelForCausalLM, pipeline
import torch
import json
import torch
from dotenv import load_dotenv
load_dotenv(".env")
Hf_Token =  os.getenv('HF_TOKEN')


  

os.environ["HF_TOKEN"] = Hf_Token
model_name = "google/gemma-3-1b-it"

tokenizer = AutoTokenizer.from_pretrained(model_name)  # loaded google gemma tokenizer

# print(tokenizer("hello how are you"))
# print(tokenizer.get_vocab())

input_tokens = tokenizer("hello how are you")['input_ids']
print(input_tokens)


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16
    )

gen_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

print(gen_pipeline("hello how are you")[0]['generated_text'])





