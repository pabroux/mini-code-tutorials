# Model Context Protocol Apps (MCP Apps)

This tutorial explains how to create a MCP server offering a MCP Apps.

> [!IMPORTANT]
> This tutorial requires some knowledge of MPC. I highly recommend you to read at least the [Key Concepts and Terminology](https://huggingface.co/learn/mcp-course/unit1/key-concepts) page from the [MCP Course by Hugging Face](https://huggingface.co/learn/mcp-course/) before going further. 

## What?

MCP Apps is the first extension of the MCP. It allows you to build interactive UI applications that render inside MCP hosts like Claude Desktop or VS Code.

> [!TIP]
> Find a tutorial about [MCP server](https://github.com/pabroux/mini-code-tutorials/tree/master/tutorial/ai/llm/mcp).

## How to use the tutorial?

- Script

## Requirements

- [bun](https://bun.com) or [mise](https://mise.jdx.dev).

## Installation

If you have mise installed, you can install bun with the following:
```zsh
mise install
```

Once bun available, install the following packages:
```zsh
bun install @modelcontextprotocol/ext-apps @modelcontextprotocol/sdk
bun install -D vite vite-plugin-singlefile express cors @types/express @types/cors
```

Finally, build with following command:
```zsh
bun run build
```

This last command will output a single file in the `src/dist` folder: `mcp-app.html`. That file is the UI given to a MCP client by a MCP server.

## Usage

Everything is well explained in the scripts of the `src` folder.
You need to run a MCP server and a MCP client to make it work. 

### MCP server

Run the following command:
```zsh
bun run serve
```

## Resources

- [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) by Model Context Protocol
- [MCP Apps documentation](https://modelcontextprotocol.github.io/ext-apps/api/)
