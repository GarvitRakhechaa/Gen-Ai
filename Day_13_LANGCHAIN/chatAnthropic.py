from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3.5-sonnet-20240620")

result = llm.invoke("What is the capital of France?")

print(result.content)