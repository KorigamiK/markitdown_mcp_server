[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/korigamik-markitdown-mcp-server-badge.png)](https://mseep.ai/app/korigamik-markitdown-mcp-server)

# MarkItDown MCP Server

[![smithery badge](https://smithery.ai/badge/@KorigamiK/markitdown_mcp_server)](https://smithery.ai/server/@KorigamiK/markitdown_mcp_server)

A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

<a href="https://glama.ai/mcp/servers/sbc6bljjg5"><img width="380" height="200" src="https://glama.ai/mcp/servers/sbc6bljjg5/badge" alt="MarkItDown Server MCP server" /></a>

## Supported Formats

- PDF
- PowerPoint
- Word
- Excel
- Images (EXIF metadata and OCR)
- Audio (EXIF metadata and speech transcription)
- HTML
- Text-based formats (CSV, JSON, XML)
- ZIP files (iterates over contents)

## Installation

### Installing via Smithery

To install MarkItDown MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@KorigamiK/markitdown_mcp_server):

```bash
npx -y @smithery/cli install @KorigamiK/markitdown_mcp_server --client claude
```

### Manual Installation

1. Clone this repository
2. Install dependencies:
```bash
uv install
```

## Usage

### As MCP Server

The server can be integrated with any MCP client. Here are some examples:

#### Zed Editor

Add the following to your `settings.json`:

```json
"context_servers": {
  "markitdown_mcp": {
    "settings": {},
    "command": {
      "path": "uv",
      "args": [
        "--directory",
        "/path/to/markitdown_mcp_server",
        "run",
        "markitdown"
      ]
    }
  }
}
```

### Commands

The server responds to the following MCP commands:

- `/md <file>` - Convert the specified file to Markdown

Example:
```bash
/md document.pdf
```

## Supported MCP Clients

Works with any MCP-compliant client listed at [modelcontextprotocol.io/clients](https://modelcontextprotocol.io/clients), including:

- Zed Editor
- Any other MCP-compatible editors and tools

## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

https://github.com/microsoft/markitdown#readme
