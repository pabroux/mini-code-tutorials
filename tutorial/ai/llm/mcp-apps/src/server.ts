import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import {
  registerAppTool,
  registerAppResource,
  RESOURCE_MIME_TYPE,
} from "@modelcontextprotocol/ext-apps/server";
import cors from "cors";
import express from "express";
import fs from "node:fs/promises";
import path from "node:path";

// Create the MCP server
const server = new McpServer({
  name: "My MCP App Server",
  version: "1.0.0",
});

// The `ui://` scheme tells hosts this is an MCP App resource
// ↳ The path structure is arbitrary.
const resourceUri = "ui://get-time/mcp-app.html";

// Register the tool `get-time` that returns the current time of the server
// ↳ `_meta: { ui: { resourceUri } }`, during the discovery phase, informs
//   the host that this tool is associated with the resource `resourceUri`
//   and it should load the associated ui resource beforehand. The returned
//   function will be called when the host requests the tool and should be
//   passed to the ui resource.
registerAppTool(
  server,
  "get-time",
  {
    title: "Get Time",
    description: "Returns the current server time.",
    inputSchema: {},
    _meta: { ui: { resourceUri } },
  },
  async () => {
    const time = new Date().toISOString();
    return {
      content: [{ type: "text", text: `🕐 ${time}` }],
    };
  },
);

// Register the resource that serves the bundled HTML
registerAppResource(
  server,
  resourceUri,
  resourceUri,
  { mimeType: RESOURCE_MIME_TYPE },
  async () => {
    // Read the HTML file
    const html = await fs.readFile(
      path.join(import.meta.dirname, "dist", "mcp-app.html"),
      "utf-8",
    );
    // Return the HTML content to the MCP client
    return {
      contents: [
        { uri: resourceUri, mimeType: RESOURCE_MIME_TYPE, text: html },
      ],
    };
  },
);

// Expose the MCP server over HTTP
const expressApp = express();
expressApp.use(cors());
expressApp.use(express.json());

expressApp.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
    enableJsonResponse: true,
  });
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

console.log("Starting MCP App server...");

// Start the server
expressApp.listen(3001, (err) => {
  if (err) {
    console.error("Error starting server:", err);
    process.exit(1);
  }
  console.log("Server listening on http://localhost:3001/mcp");
});
