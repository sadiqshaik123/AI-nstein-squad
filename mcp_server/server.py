from fastmcp import FastMCP

# Import MCP tools
from tools.news_tool import get_supplier_news
from tools.compliance_tool import get_compliance_data

# Create MCP Server
mcp = FastMCP("SupplierMaster")

# Register Tools
mcp.tool()(get_supplier_news)
mcp.tool()(get_compliance_data)


@mcp.tool()
def health_check():
    """
    MCP Health Check
    """
    return {
        "status": "healthy",
        "server": "SupplierMaster",
        "tools": [
            "get_supplier_news",
            "get_compliance_data"
        ]
    }


if __name__ == "__main__":
    print("Starting SupplierMaster MCP Server...")
    mcp.run()
