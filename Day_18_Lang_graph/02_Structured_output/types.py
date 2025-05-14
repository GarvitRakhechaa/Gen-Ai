from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Country(BaseModel):
    """Information about a country"""

    name: str = Field(description="name of the country")
    language: str = Field(description="language of the country")
    capital: str = Field(description="capital of the country")


structured_output = model.with_structured_output(Country)

response = structured_output.invoke("tell me about Bharat")
print(response)