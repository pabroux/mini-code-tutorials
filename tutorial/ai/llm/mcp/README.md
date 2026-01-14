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

- Python 3.11+
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

To execute the MCP server in development mode, run the following command:
```zsh
mcp dev src/mcp-server.py
```

> [!NOTE]
> In the development mode, you'll have an UI that you can use to send and test requests to the server.
> Don't forget to click on the "Connect" button at the launch!

To execute the MCP server in production mode, run the following command:
```zsh
mcp run src/mcp-server.py
```

Once the server is up and running, you c

Once the server is in pro

## Resources

- [MCP Course by Hugging Face](https://huggingface.co/learn/mcp-course/)
