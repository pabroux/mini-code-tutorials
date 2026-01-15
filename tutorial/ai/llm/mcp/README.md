# Model Context Protocol (MCP)

This tutorial explains how to create and run a MCP server.

> [!IMPORTANT]
> This tutorial requires some knowledge of MPC. I highly recommend you to read at least the [Key Concepts and Terminology](https://huggingface.co/learn/mcp-course/unit1/key-concepts) page from the [MCP Course by Hugging Face](https://huggingface.co/learn/mcp-course/) before going further. 

## What?

MCP is an open-source standard developed by Anthropic for connecting large language models (LLMs) to external data sources, tools, and applications.
It uses a client-server architecture with [JSON-RPC 2.0](https://huggingface.co/learn/mcp-course/unit1/communication-protocol#json-rpc-the-foundation) to standardize tool discovery, execution, and context sharing, eliminating custom integrations.

## How to use the tutorial?

- Script

## Requirements

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)

## Installation

Create a virtual environment:
```zsh
uv venv --python 3.11 .venv
```

Activate the environment:
```zsh
.venv/bin/activate
```

Then install the dependencies:
```zsh
uv sync
```

## Usage

Everything is well explained in the scripts of the `src` folder. 

### Development mode

Run the following command:
```zsh
mcp dev src/mcp-server.py
```

Development mode provides a built-in UI for sending/testing requests. Click "Connect" on launch.

### Production mode

Deploy for remote HTTP+SSE access:
```zsh
mcp run src/mcp-server.py
```

Connect via MCP clients like Cursor, Claude Desktop, or VS Code using your `mcp.json` configuration or direct HTTP endpoints.

### Client integration

The `src/mcp.json` file enables automatic discovery and local execution of the `src/mcp-server.py` in compatible MCP clients like Cursor, and Claude Desktop.

Place it in client-specific directories (e.g., `~/.cursor/mcp.json`) to let IDEs spawn the server via stdio when needed—no manual mcp dev required.

> [!important]
> Update the path within `src/mcp.json` to correctly point to `src/mcp-server.py` before use.

## Resources

- [MCP Course](https://huggingface.co/learn/mcp-course/) by Hugging Face
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [What is MCP?](https://cursor.com/docs/context/mcp#what-is-mcp) by Cursor
- [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) by Model Context Protocol
