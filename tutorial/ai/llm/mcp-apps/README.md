# Model Context Protocol Apps (MCP Apps)

This tutorial explains how to create a MCP server offering a MCP Apps.

> [!IMPORTANT]
> This tutorial requires some knowledge of MPC. I highly recommend you to read at least the [Key Concepts and Terminology](https://huggingface.co/learn/mcp-course/unit1/key-concepts) page from the [MCP Course by Hugging Face](https://huggingface.co/learn/mcp-course/) before going further. 

## What?

MCP Apps is the first major extension of the MCP framework, enabling developers to build interactive UI applications that render directly within MCP hosts such as Claude Desktop or VS Code. Each MCP App connects to an MCP Server, which handles backend logic, data exchange, and communication between the app and the host environment.

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

### MCP Client

Two ways:
- With a MCP host like Claude Desktop
- Simulating it with a simple project

#### With a MCP host

Once your MCP is running (e.g., on `http://localhost:3001`), execute the following:
```zsh
bunx cloudflared tunnel --url http://localhost:3001
```

This will expose your local server to the internet (free) — required for your MCP host to communicate with it.

Copy the generated URL (e.g., `https://random-name.trycloudflare.com`), then follow your MCP host’s instructions to add a custom connector to it.

You can now ask your LLM to run the tool linked to the MCP App.

#### Simulating it with a simple project

The official Model Context Protocol organization developed a test host for development.

Clone the following repository:
```zsh
git clone https://github.com/modelcontextprotocol/ext-apps.git
```

Go to the corresponding folder within it and install the dependencies (not working with bun unfortunately):
```zsh
cd ext-apps/examples/basic-host
npm install
```

Launch the test host:
```zsh
SERVERS='["http://localhost:3001/mcp"]' npm start
```

Now, you can naviguate to `http://localhost:8080` and test the MCP App.

## Resources

- [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) by Model Context Protocol
- [MCP Apps documentation](https://modelcontextprotocol.github.io/ext-apps/api/)
