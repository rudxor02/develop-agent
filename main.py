import logging
import os

from dotenv import load_dotenv
from langchain.agents import AgentType, get_all_tool_names, initialize_agent, load_tools
from langchain.llms import OpenAI
from langchain.tools import ShellTool, DuckDuckGoSearchRun
from repl import python_repl

from Q1 import prompt as q1_prompt
from Q2 import prompt as q2_prompt



def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY", "")

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.7, model="text-davinci-003")
    shell_tool = ShellTool()
    search_tool = DuckDuckGoSearchRun()

    agent = initialize_agent(
        [
            shell_tool, 
            search_tool, 
            # python_repl
            ], llm ,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    

    # agent.run(q1_prompt)
    agent.run(q2_prompt)
    


if __name__ == "__main__":
    main()