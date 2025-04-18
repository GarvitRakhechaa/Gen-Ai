from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import torch 
import torch.nn as nn
from torch.optim import AdamW
from dotenv import load_dotenv
load_dotenv("../.env")
Hf_Token =  os.getenv('HF_TOKEN')


# get a hugging face token
os.environ["HF_TOKEN"] = Hf_Token


# # pulled model from hugging face
model_name = "google/gemma-3-1b-it"

#checkd gpu 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)



# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)  # loaded google gemma tokenizer

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
)

# -----------------------------------------------------------------------------------
helloSimple = tokenizer("hello world", ) # this will provide input_ids and attention mask in simple format
print("this is hello in Simple format ",helloSimple)  

# simple tokenization

# output_tokens1_simple = model.generate(helloSimple["input_ids"])  # this will give error because model need tensor format tokens
# print("ye output tokens hai ",output_tokens1_simple)  # this will give error because model need tensor format tokens
# detokenized1_simple = tokenizer.batch_decode(output_tokens1_simple) # this will give error because model need tensor format tokens    # detokenizing tokens generatedc by model
# print("ye detokenized output hai ",detokenized1_simple)

# ---------------------------------------------------------------------------------------------------------------

# tensor tokenization

hellotensor = tokenizer("hello world", return_tensors="pt") # this will provide input_ids and attention mask in tensor format
print("this is hello in tensor format ",hellotensor)  
output_tokens1_tensor = model.generate(hellotensor["input_ids"])
print("ye output tokens hai ",output_tokens1_tensor)
detokenized1_tensor = tokenizer.batch_decode(output_tokens1_tensor)     # detokenizing tokens generatedc by model
print("ye detokenized output hai ",detokenized1_tensor)


# -------------------------------------------------------------------------------------------------------------------------

# chat template
input_conversation = [
    {"role": "user", "content": "which is best place to learn Gen AI "},
    # {"role": "assistant", "content": "the best place to learn Gen AI is "},
]

input_tokens_simple = tokenizer.apply_chat_template(  
    conversation = input_conversation,
    tokenize = True, 
) 

# print("ye chat template simple format me hai ",input_tokens_simple)
# output_tokens_simple = model.generate(input_tokens_simple)   # this will give error because model need tensor format tokens
# print("ye output tokens hai ",output_tokens_simple)  # this will give error because model need tensor format tokens
# detokenized_simple = tokenizer.batch_decode(output_tokens_simple) # this will give error because model need tensor format tokens    # detokenizing tokens generatedc by model
# print("ye detokenized output hai ",detokenized_simple)



#-------------------------------------------------------------------------------------------------------------------------------

input_tokens_tensor = tokenizer.apply_chat_template(  
    conversation = input_conversation,
    tokenize = True, 
    return_tensors="pt"
)   

print("ye chat template tensor format me hai ",input_tokens_tensor)
output_tokens_tensor = model.generate(input_tokens_tensor)  
print("ye output tokens hai ",output_tokens_tensor)
detokenized_tensor = tokenizer.batch_decode(output_tokens_tensor)  # detokenizing tokens generatedc by model
print("ye detokenized output hai ",detokenized_tensor)

# --------------------------------------------------------------------------------------------------------------------------






