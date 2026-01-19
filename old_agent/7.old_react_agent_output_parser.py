# Module 7: Old React Agent with Output Parser
# This module extends the React agent introduced in Module 6 by adding structured output parsing using Pydantic.
# Structured output is important because it ensures that the agent's responses follow a specific format, making them easier to process.
# To achieve this, we define a schema (`AgentResponse`) using Pydantic and use the `PydanticOutputParser` to enforce this schema.
# A custom prompt template (`REACT_OUTPUT_PARSING_PROMPT`) is used with format instructions to guide the agent's output.
# Key Difference: This module uses the older `create_react_agent` function, which requires manual setup of the reasoning framework.
# The structured output is enforced by passing the schema and format instructions to the prompt and output parser.
# For example, it can search for job postings dynamically and return the results in a structured format.
from dotenv import load_dotenv
load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent

from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from prompt import REACT_OUTPUT_PARSING_PROMPT
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
# react_prompt = hub.pull("hwchase17/react") # Public Prompt Template from LangChain Hub (https://smith.langchain.com/hub/hwchase17/react?organizationId=75c882e4-f6f4-424a-ba9d-ae8be027eb27)
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template = REACT_OUTPUT_PARSING_PROMPT,
    input_variables = ["input", "agent_scratchpad", "tool_names"],
).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_format_instructions)
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