from langchain_google_genai import ChatGoogleGenerativeAI
# from typing_extensions import Annotated, TypedDict
# from typing import Optional



# class Joke(TypedDict):
#     """Joke to tell user"""
#     setup: Annotated[str, ...,"the setup of the joke"]
#     punchline: Annotated[str , ... , "the punchline of the joke"]
#     rating: Annotated[Optional[int], None, "how funny the joke is from 1 to 10"]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# structured_output = llm.with_structured_output(Joke)

# # response = structured_output.invoke("tell me joke on indian sister")
# llm.invoke("tell me joke on indian sister")

from typing_extensions import Annotated, TypedDict
from typing import Optional


# TypedDict
class Joke(TypedDict):
    """Joke to tell user."""
    setup: Annotated[str, ..., "The setup of the joke"]
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], None, "How funny the joke is, from 1 to 10"]

    # Alternatively, we could have specified setup as:

    # setup: str                    # no default, no description
    # setup: Annotated[str, ...]    # no default, no description
    # setup: Annotated[str, "foo"]  # default, no description



structured_llm = llm.with_structured_output(Joke)

response = structured_llm.invoke("tell me joke in cat")
print(response)