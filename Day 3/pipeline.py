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

input_prompt = [  # this input prompt
    "the capital of india is"
]

tokenized = tokenizer(input_prompt, return_tensors="pt")  # tokenize input and return in tensor format
# tokenized = tokenizer(input_prompt)
print(tokenized["input_ids"])

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16
    )

response = model.generate(tokenized["input_ids"])    #model generate tokens 
print(response)   # print generated tokens
detokenized = tokenizer.batch_decode(response)  # detokenizing tokens generatedc by model
print(detokenized)  # priniting response
print(detokenized[0])

