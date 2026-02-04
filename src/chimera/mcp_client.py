import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import logging

logger = logging.getLogger(__name__)

class ChimeraMCPClient:
    def __init__(self, server_command: str, server_args: list[str]):
        self.server_params = StdioServerParameters(
            command=server_command,
            args=server_args,
            env=None
        )
        self.session: ClientSession | None = None

    async def connect(self):
        """
        Connect to the MCP server.
        Note: The context manager usage in mcp sdk is strict.
        This method is illustrative of the connection logic.
        """
        try:
            async with stdio_client(self.server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    self.session = session
                    logger.info("Connected to MCP Server")
                    # Keep session alive or execute tools here
                    # For persistent connection, architecture needs an event loop handling
        except Exception as e:
            logger.error(f"Failed to connect to MCP server: {e}")

    async def list_tools(self):
        if not self.session:
            return []
        result = await self.session.list_tools()
        return result.tools

    async def call_tool(self, name: str, arguments: dict):
        if not self.session:
            raise RuntimeError("Not connected")
        result = await self.session.call_tool(name, arguments)
        return result
