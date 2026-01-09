from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches for the current weather in a given location.
    Args:
        query (str): The search query, e.g., "weather in Tokyo".
    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI()
# llm = ChatOllama(model="gemma3:270m", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from search_agent!")
    result = agent.invoke({"messages": HumanMessage(content="What's the weather like in Tokyo?")})
    print(result)
    result_2 = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Hyderabad on linkedin and list the results")})
    print(result_2)

    
if __name__ == "__main__":
    main()