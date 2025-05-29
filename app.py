
import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

# Change this to the path of the MCP server file
CALCULATOR_MCP_SERVER_FILE_PATH = "/Users/ravisreeraman/python/mcp-server/mcp-server/server.py"

def create_client():
    return  MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            "args": [CALCULATOR_MCP_SERVER_FILE_PATH],
            "transport": "stdio"
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http"
        }
    }
)


async def main():
    # Add your OpenAI API key here
    os.environ["OPENAI_API_KEY"] = ""
    client = create_client()
    tools = await client.get_tools()
    agent = create_react_agent(
    # "anthropic:claude-3-7-sonnet-latest",
        'gpt-3.5-turbo',
        tools
    )

    math_response = await agent.ainvoke(
        {'messages': [{'role': 'user', 'content': 'what is the value of (3 + 5) * 12?'}]}
    )

    print(math_response)

    weather_response = await agent.ainvoke(
        {'messages': [{'role': 'user', 'content': 'how is the weather in nyc?'}]}
    )

    print(weather_response)


if __name__ == "__main__":
  asyncio.run(main())