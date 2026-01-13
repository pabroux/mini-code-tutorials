from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Stranger Things Service")

# Tool implementation
# ↳ Tools are functions that can be called by the LLM to perform
#   side effects or heavy computation.
@mcp.tool()
def get_location(person: str) -> str:
    """Get the current position of a specified person."""
    return f"{person}: Upside Down, 37°14′0″N 115°48′30″W"

# Resource implementation
# ↳ Resources expose data to LLMs like GET endpoints in REST APIs — they
#   deliver information without heavy computation or side effects.
@mcp.resource("details://{person}")
def get_details(person: str) -> str:
    """Provide details about a specified person."""
    return f"{person}: Green eyes, Driver's licence 126739."

@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{
  "language": "en",
  "debug": false
}"""

# Prompt implementation
# ↳ Prompts that guide interactions between users, AI models, and the
#   available capabilities.
@mcp.prompt()
def get_report(person: str) -> str:
    """Create a location report prompt."""
    return f"""You are a location reporter. Location report for {person}?"""


# Run the server
if __name__ == "__main__":
    mcp.run()
