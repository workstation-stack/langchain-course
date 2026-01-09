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