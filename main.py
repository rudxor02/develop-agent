import logging
import os

from dotenv import load_dotenv
from langchain.agents import AgentType, get_all_tool_names, initialize_agent, load_tools
from langchain.llms import OpenAI
from langchain.tools import ShellTool

prompt = """Please develop a webpage that displays hello world.
You should develop a localhost website and return the URL of the website.
"""

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY", "")

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    llm = OpenAI(openai_api_key=openai_api_key)
    shell_tool = ShellTool()

    agent = initialize_agent([shell_tool], llm ,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    

    agent.run(prompt)
    


if __name__ == "__main__":
    main()