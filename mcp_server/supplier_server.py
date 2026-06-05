
from fastmcp import FastMCP
mcp=FastMCP('SupplierMaster')

@mcp.tool()
def get_supplier(name:str):
    return {'supplier':name,'country':'India','delivery_score':88}

if __name__=='__main__':
    mcp.run()
