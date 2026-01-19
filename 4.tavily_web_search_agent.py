# Module 4: Tavily Web Search Agent
# This module focuses on integrating the Tavily search tool into a LangChain agent for advanced web search capabilities.
# Unlike Module 3, which uses a custom tool, this module directly uses LangChain's `create_agent` function.
# The `create_agent` function simplifies the process of combining tools and language models into a single agent.
# Key Difference: The `create_agent` function is part of the newer LangChain framework, which abstracts away the reasoning framework.
# It does not require manually defining reasoning-based prompts, making it easier to use for straightforward tasks.
# For example, it can search for job postings dynamically and return the results.
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


llm = ChatOpenAI()
# llm = ChatOllama(model="gemma3:270m", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from search_agent!")
    result_2 = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Hyderabad on linkedin and list the results")})
    print(result_2)


        
    
if __name__ == "__main__":
    main()