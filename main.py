from fastmcp import FastMCP
import random
import json
import os

#create the FastMCP server instance

#tool: Add two numbers
mcp=FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int,b:int) -> int:
    """
    Add two numbers together.
    
    Args:
    a:First number
    b:Second number

    Returns:
    The sum of a and b
    
    """
    return a+b


#Tool : Generate a random number
@mcp.tool
def random_number(min_val:int=1, max_val:int=100) ->int:
    """
    Generate a random number within a range.

    Args:
    min_val: Minimum value (defaul: 1)
    max_val: Maximum value (default: 100)

    Return:
    A random integer between min_val and max_val
    """

    return random.randint(min_val,max_val)

#resources: Server information
@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server"""
    info={
        "name":"Sample Calculator Server",
        "version":"1.0.0",
        "description":"A basic mcp server with math tool",
        "tools":["add","random_number"],
        "author":"Sudheesh"
    }

    return json.dumps(info,indent=2)





if __name__ == "__main__":
    mcp.run(transport="sse",host="0.0.0.0", port=3001)
