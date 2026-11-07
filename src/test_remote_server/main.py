from fastmcp import FastMCP
import random 
import json

# Create the FastMCP client instance 
mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:float, b:float) -> float:
    """Add two numbers.
    Args: 
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of the two numbers.
    """
    return a + b

@mcp.tool
def random_number(min:int = 1, max:int = 100) -> int:
    """Generate a random number between min and max.
    Args:
        min (int): The minimum value (inclusive).
        max (int): The maximum value (inclusive).
    Returns:
        int: A random number between min and max.
    """
    return random.randint(min, max)

@mcp.resource("info://server")
def server_info() -> dict:
    """Get server information.
    Returns:
        dict: A dictionary containing server information.
    """
    return {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A simple calculator server that can perform basic arithmetic operations.",
        "tools" : ["add", "random_number"],
        "author" : "Deepak "
    }

# Start the server
if __name__ == "__main__":
    #mcp.start() these means we set the server to run on the default port 8000
    mcp.run(transport="http", host="0.0.0.0", port=8000) # These means we set the server to run on the default port 8000 and listen on all available network interfaces