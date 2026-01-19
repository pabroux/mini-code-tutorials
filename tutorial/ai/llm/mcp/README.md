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

- [uv](https://docs.astral.sh/uv/)

## Installation

Create a virtual environment:
```zsh
uv venv --python 3.11
```

Install the dependencies:
```zsh
uv sync
```

Finally, activate the virtual environment:
```zsh
source .venv/bin/activate
```

## Usage

Everything is well explained in the scripts of the `src` folder.
You need to run a MCP server and a MCP client to make it work. 

### MCP server

Run the following command:
```zsh
mcp run src/mcp-server.py
```

> [!TIP]
> Use the following command to run in development mode:
> ```zsh
> mcp dev src/mcp-server.py
> ```
> That mode provides a built-in UI for sending/testing requests. Click "Connect" on launch.

### MCP client

Two ways:
- Passing the `mcp.json` to a host like Cursor or Claude Desktop
- Programmatically through MCP client implementation

#### Using the `mcp.json` file

The `src/mcp.json` file enables automatic discovery and local execution of the `src/mcp-server.py` in compatible MCP clients like Cursor, and Claude Desktop.

Place it in client-specific directories (e.g., `~/.cursor/mcp.json`) to let IDEs spawn the server via stdio when needed—no manual mcp dev required.

> [!IMPORTANT]
> Update the path within `src/mcp.json` to correctly point to `src/mcp-server.py` before use.

#### Programmatically

The `src/mcp-client.py` file is a simple [Gradio](https://www.gradio.app/) example using the Hugging Face's `smolagents` agent library.
That library offers a simple way to create agents with MCP integrations.

Run the following command:
```zsh
python src/mcp-client.py
```

> [!IMPORTANT]
> Update the path within `src/mcp-client.py` to correctly point to `src/mcp-server.py` before use.

## Resources

- [MCP Course](https://huggingface.co/learn/mcp-course/) by Hugging Face
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [What is MCP?](https://cursor.com/docs/context/mcp#what-is-mcp) by Cursor
- [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) by Model Context Protocol
