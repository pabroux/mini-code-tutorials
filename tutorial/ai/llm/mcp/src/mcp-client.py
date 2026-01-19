import gradio as gr
import os

from mcp import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, MCPClient

# Define the server parameters
# ↳ Here we call a Python script that runs a MCP server (stdio mode).
#   To run in HTTP streamable mode, do like the following:
#   ```
#   server_parameters = {
#       "url": "http://my-mcp-server:8000/mcp",
#       "transport": "streamable-http",
#   }
#   ```
server_parameters = StdioServerParameters(
    command="python",
    args=["/path/to/mcp-server.py"],
)

try:
    # Connect to the MCP server
    mcp_client = MCPClient(server_parameters)
    
    # Get the available tools
    tools = mcp_client.get_tools()

    # Create the agent
    model = InferenceClientModel() # Requires HF_TOKEN environment variable
    agent = CodeAgent(tools=[*tools], model=model, additional_authorized_imports=["json", "ast", "urllib", "base64"])

    # Create the Gradio demo
    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        examples=["Analyze the sentiment of the following text 'This is awesome'"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    # Launch the Gradio demo
    demo.launch()
finally:
    # Disconnect from the MCP server
    mcp_client.disconnect()

