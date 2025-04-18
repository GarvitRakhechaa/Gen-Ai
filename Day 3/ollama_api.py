from fastapi import FastAPI, Body
from ollama import Client
import uvicorn

app = FastAPI()

client = Client(
    host="http://localhost:11434"
)

client.pull('gemma3:1b')

@app.post("/chat")
def chat(message: str = Body(..., description="Chat Message")):
    response = client.chat(model="gemma3:1b", messages=[
        {"role": "user", "content": message}
    ])
    
    return {"response": response["message"]["content"]}

uvicorn.run(app, host="127.0.0.1", port=8000)