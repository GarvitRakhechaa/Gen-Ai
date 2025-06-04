from vapi_python import Vapi
from vapi import Vapi

vapi = Vapi(
    api_key="ak_4f3a47222ad66843ef591da3710bd0fe8a1d",
    provider_keys={"google": "AIzaSyA8rx3rgLfGRenHrBalqd4es3bnpE8WNjE"}
)

assistant = {
    "firstMessage": "Hi! Need any help today?",
    "context": "You are a friendly assistant.",
    "model": {
        "provider": "google",
        "model": "gemini-2.0-flash"
    },
    "voice": "jennifer-playht",
    "recordingEnabled": True,
    "interruptionsEnabled": True
}

vapi.start(assistant=assistant)
