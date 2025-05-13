from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template = """
    write a {tone} email t0 {company} expressing interest in the {position} position,
    mentioning {skills} 
    as a key strength. keep it to 4 line max
"""

prompt_template = ChatPromptTemplate.from_template(template)  # converted templare to that format in which lanchain can understand
# print(prompt_template)

prompt = prompt_template.invoke({
    "tone": "comedy",
    "company": "Google",
    "position": "Software Engineer",
    "skills": "Python, Java, and C++"
})

response = model.invoke(prompt)
# print(response.content)

#example 2 --------------

messages = [
    ("system", "you are comedian and tells a jokes on given topic"),
    ("human", "tell me {num_of_jokes} on {topic}")
]

prompt_template2 = ChatPromptTemplate.from_messages(messages=messages)

prompt2 = prompt_template2.invoke(
    {"num_of_jokes": "4",
    "topic": "doctor"}
)
# print(prompt2)

result = model.invoke(prompt2)

print(result.content)
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     ("human", "Tell me {joke_count} jokes."),
# ]

# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "doctors", "joke_count": 3})
# result = model.invoke(prompt)
# print(result)

