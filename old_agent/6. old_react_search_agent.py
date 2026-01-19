# Module 6: Old React Search Agent
# This module demonstrates the use of a React-based agent for search tasks.
# React agents use a reasoning framework to decide which tools to use and how to use them.
# Key Difference: Unlike Module 4, which uses the newer `create_agent` function, this module uses the older `create_react_agent` function.
# The `create_react_agent` function requires a reasoning-based prompt, which is pulled from the LangChain Hub in this example.
# This approach provides more control over the reasoning process but is more verbose and requires manual setup.
# For example, it can search for job postings dynamically and return the results using the React reasoning framework.
from dotenv import load_dotenv
load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
react_prompt = hub.pull("hwchase17/react") # Public Prompt Template from LangChain Hub (https://smith.langchain.com/hub/hwchase17/react?organizationId=75c882e4-f6f4-424a-ba9d-ae8be027eb27)
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    print("Hello from langchain-course!") 
    result = chain.invoke(
        input = {
            "input": "search for 3 job postings for an ai engineer using langchain in bay area on linkedin and list the results"

        }
    )
    print(result)
if __name__ == "__main__":
    main()