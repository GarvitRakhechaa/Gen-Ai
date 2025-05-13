from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

summery_template = ChatPromptTemplate.from_messages(
[
    ("system", "you are a movie critic"),
    ("human", "Provide a brief summery of the movie {movie_name}.")
])

def analyse_plot(plot):
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system", "you are a movie critic"),
            ("human", "Analyse the plot: {plot}. What is its strengths answeaknesses?")
        ]
    )
    return plot_template.format_prompt(plot=plot)

def analyse_characters(characters):
    characters_template = ChatPromptTemplate.from_messages(
        [
            ("system", "you are a movie critic"),
            ("human", "Analyse the plot: {characters}. What is its strengths ans weaknesses?")
        ]
    )
    return characters_template.format_prompt(characters=characters)

def combine_verdicts(plot_analysis, character_analysis):
    return f"Plot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis}"

plot_branch_chain = (
    RunnableLambda(lambda x: analyse_plot(x)) | model | StrOutputParser()
)

character_branch_chain = (
    RunnableLambda(lambda x: analyse_characters(x)) | model | StrOutputParser()
)

chain = (
    summery_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"plot": plot_branch_chain, "characters": character_branch_chain})
    | RunnableLambda(lambda x: combine_verdicts(x["branches"]["plot"], x["branches"]["characters"]))
)

# Run the chain
result = chain.invoke({"movie_name": "indian movie WAR"})

print(result)
