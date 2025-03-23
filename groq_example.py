import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from browser_use import Agent

# Load environment variables from .env file
load_dotenv()

# Check if GROQ API key is set
if "GROQ_API_KEY" not in os.environ:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please add it to your .env file.")

# Initialize the Groq model
llm = ChatGroq(
    model="llama3-70b-8192",  # You can also use "mixtral-8x7b-32768" 
    temperature=0.0,
)

# Define a task for the browser agent
task = "Search for 'What is browser-use library' and summarize the first three results"

# Create the browser agent with Groq as the LLM
agent = Agent(
    task=task,
    llm=llm,
)

async def main():
    # Run the agent to complete the task
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main()) 