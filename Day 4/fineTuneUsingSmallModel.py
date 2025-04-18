from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import torch
import torch.nn as nn
from torch.optim import AdamW
from dotenv import load_dotenv

load_dotenv("../.env")
Hf_Token =  os.getenv('HF_TOKEN')

# Use a tiny model safe for 4GB GPU
model_name = "sshleifer/tiny-gpt2"
os.environ["HF_TOKEN"] = Hf_Token

# Device check
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
model.train()

# Prepare conversation
input_conversation = [
    {"role": "user", "content": "which is best place to learn Gen AI"},
    {"role": "assistant", "content": "the best place to learn Gen AI is "}
]

# Convert conversation into plain text
conversation_text = "User: which is best place to learn Gen AI\nAssistant: the best place to learn Gen AI is "

# Output label
output_label = "Gen AI 1.0 by ChaiCode and Piyush Garg"
full_text = conversation_text + output_label + tokenizer.eos_token
print("\nFull conversation:\n", full_text)

# Tokenize
tokenized = tokenizer(full_text, return_tensors="pt", add_special_tokens=False)
input_ids = tokenized["input_ids"][:, :-1].to(device)
target_ids = tokenized["input_ids"][:, 1:].to(device)

# Loss function
def calculate_loss(logits, labels):
    loss_fn = nn.CrossEntropyLoss(reduction="none")
    return loss_fn(logits.view(-1, logits.shape[-1]), labels.view(-1))

# Optimizer
optimizer = AdamW(model.parameters(), lr=3e-5, weight_decay=0.01)

# Training loop
for step in range(5):  # Keep it small for demo
    outputs = model(input_ids=input_ids)
    loss = calculate_loss(outputs.logits, target_ids).mean()
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(f"Step {step+1} | Loss: {loss.item():.4f}")

# Inference
model.eval()
with torch.no_grad():
    input_prompt = "which is best place to learn Gen AI"
    inputs = tokenizer(input_prompt, return_tensors="pt").to(device)
    output_tokens = model.generate(**inputs, max_new_tokens=30)
    decoded_output = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

print("\nGenerated Output:\n", decoded_output)
