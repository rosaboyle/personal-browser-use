#!/usr/bin/env python
"""
Example demonstrating browser-use with Groq, logging and telemetry
"""
import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from browser_use import Agent
from browser_use.telemetry.service import ProductTelemetry

# Load environment variables from .env file
load_dotenv()

# Configure logging level: 'debug', 'info', or 'result'
# 'debug' - Shows all details including telemetry
# 'info' - Shows general operation info
# 'result' - Shows only the final results
os.environ["BROWSER_USE_LOGGING_LEVEL"] = "debug"

# Uncomment to disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"


async def run_agent_with_logging_telemetry():
    """Run a Groq-powered agent with logging and telemetry enabled"""
    # Display telemetry information
    telemetry = ProductTelemetry()
    print(f"Telemetry user ID: {telemetry.user_id}")
    print(f"Telemetry enabled: {telemetry._posthog_client is not None}")
    print(f"Telemetry user ID file location: {telemetry.USER_ID_PATH}")
    
    # Where logs will be shown
    print(f"Logs are being sent to stdout with level: {os.getenv('BROWSER_USE_LOGGING_LEVEL', 'info')}")
    
    # Initialize the Groq model
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.0,
    )
    
    # Create agent (this will automatically send telemetry events)
    agent = Agent(
        task="Search for 'What is browser-use library' and summarize the first result",
        llm=llm,
    )
    
    print("\nRunning agent... (telemetry events will be captured in logs)")
    # Run the agent (this will generate various telemetry events)
    # You'll see the logs in the console output
    await agent.run(max_steps=5)  # Limit to 5 steps for demo purposes
    
    print("\nAgent run complete. All logs have been displayed in the console.")
    print("Telemetry events were automatically sent for:")
    print("1. Agent initialization")
    print("2. Each agent step")
    print("3. Agent completion")


if __name__ == "__main__":
    asyncio.run(run_agent_with_logging_telemetry()) 