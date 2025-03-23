#!/usr/bin/env python
"""
Example demonstrating how to send custom telemetry events in browser-use
"""
import os
from dotenv import load_dotenv
from browser_use.telemetry.service import ProductTelemetry
from browser_use.telemetry.views import (
    AgentRunTelemetryEvent,
    AgentStepTelemetryEvent,
    AgentEndTelemetryEvent,
    ControllerRegisteredFunctionsTelemetryEvent,
    RegisteredFunction
)

# Load environment variables
load_dotenv()

# Enable debug logging to see telemetry events
os.environ["BROWSER_USE_LOGGING_LEVEL"] = "debug"

# Uncomment to disable telemetry for testing
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Get the telemetry service instance (singleton)
telemetry = ProductTelemetry()

# Show telemetry configuration
print(f"Telemetry user ID: {telemetry.user_id}")
print(f"Telemetry ID file location: {telemetry.USER_ID_PATH}")
print(f"Telemetry enabled: {telemetry._posthog_client is not None}")
print(f"Debug logging: {telemetry.debug_logging}")

# Create a unique identifier for this agent session
agent_id = "example-groq-agent-123"

# Example 1: Agent Run Event (sent when the agent starts)
run_event = AgentRunTelemetryEvent(
    agent_id=agent_id,
    use_vision=True,
    task="Search with Groq for browser-use documentation",
    model_name="llama3-70b-8192",
    chat_model_library="langchain-groq",
    version="1.1.41",
    source="custom_example"
)

# Example 2: Agent Step Event (sent for each step the agent takes)
step_event = AgentStepTelemetryEvent(
    agent_id=agent_id,
    step=1,
    step_error=[],
    consecutive_failures=0,
    actions=[
        {"type": "go_to_url", "url": "https://github.com/browser-use/browser-use"},
        {"type": "extract_content", "goal": "Find documentation links"}
    ]
)

# Example 3: Agent End Event (sent when the agent completes)
end_event = AgentEndTelemetryEvent(
    agent_id=agent_id,
    steps=3,
    max_steps_reached=False,
    is_done=True,
    success=True,
    total_input_tokens=1500,
    total_duration_seconds=12.3,
    errors=[]
)

# Send the telemetry events
def send_custom_telemetry():
    """Send example telemetry events and print confirmation"""
    print("\nSending custom telemetry events...")
    
    # Send each event
    telemetry.capture(run_event)
    print(f"✓ Sent run event: {run_event.name}")
    
    telemetry.capture(step_event)
    print(f"✓ Sent step event: {step_event.name}")
    
    telemetry.capture(end_event)
    print(f"✓ Sent end event: {end_event.name}")
    
    print("\nAll telemetry events sent!")
    print("Note: These events appear in the logs when debug logging is enabled")
    print("Telemetry data is sent to PostHog and is anonymized")

if __name__ == "__main__":
    send_custom_telemetry() 