from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CalculatorServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    print(f"Adding {a} and {b}")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    print(f"Subtracting {a} and {b}")
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    print(f"Multiplying {a} and {b}")
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    print(f"Dividing {a} and {b}")
    return a / b

@mcp.tool()
def square(a: int) -> int:
    print(f"Squaring {a}")
    return a * a

@mcp.tool()
def cube(a: int) -> int:
    print(f"Cubing {a}")
    return a * a * a

if __name__ == "__main__":
    mcp.run(transport="stdio")