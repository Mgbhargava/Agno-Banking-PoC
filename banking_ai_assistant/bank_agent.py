#open ai
# from agno.agent import Agent
# from agno.models.openai import OpenAIChat
# # from agno.models.openai import GPT4  # You can switch to Groq if preferred
# from agno.tools.reasoning import ReasoningTools
# from dotenv import load_dotenv
# import os
# # Load environment variables from .env
# load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),  # or use Groq if configured
#     tools=[ReasoningTools()],
#     instructions="You are a helpful banking assistant. Explain financial and banking concepts clearly with practical examples."
# )

#groq
from agno.agent import Agent
from agno.models import groq  # Or LLaMA3, Gemma depending on your preference
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  # Set GROQ_API_KEY env var

agent = Agent(
    model=groq.Groq(id="deepseek-r1-distill-llama-70b"),  # Replace with 'llama3-70b-8192' or 'gemma-7b-it' if preferred
    tools=[ReasoningTools()],
    instructions="You are a helpful banking assistant. Explain financial and banking concepts clearly with practical examples."
)
