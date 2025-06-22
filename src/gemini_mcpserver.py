"""
Model Context Protocol (MCP) gemini api Server implementation.

This module sets up an MCP-compliant server and registers gemini api tools
that follow Anthropic's Model Context Protocol specification. These tools can be
accessed by Claude and other MCP-compatible AI models.
"""
from mcp.server.fastmcp import FastMCP
import argparse
import tools_gemini_api
from mylogging import logger
DEFAULT_PORT = 3001
DEFAULT_CONNECTION_TYPE = "stdio"  # Alternative: "stdio"
def create_mcp_server(port=DEFAULT_PORT):
    """
    Create and configure the Model Context Protocol server.

    Args:
        port: Port number to run the server on

    Returns:
        Configured MCP server instance
    """
    mcp = FastMCP("GeminiApiService", port=port)

    # Register MCP-compliant tools
    register_tools(mcp)

    return mcp


def register_tools(mcp):
    """
    Register all tools with the MCP server following the Model Context Protocol specification.

    Each tool is decorated with @mcp.tool() to make it available via the MCP interface.

    Args:
        mcp: The MCP server instance
    """


    @mcp.tool()
    async def instruction_to_gemini_flash_model(prompt: str):
        """
        Send the instruction to Gemini flash model

        This MCP tool allows AI models to send the prompt to Gemini flash model

        Args:
            prompt: the instruction that need to be send to Gemini flash model(e.g., please summarize this text)
        Returns:
            after processing by gemini, return the response from Gemini
        """
        return await tools_gemini_api.get_response_from_flash_model(prompt)
    @mcp.tool()
    async def instruction_to_gemini_youtube_model(prompt: str, youtubeURL: str):
        """
        Send the instruction to Gemini youtube model

        This MCP tool allows AI models to send the prompt to Gemini youtube model

        Args:
            prompt: the instruction that need to be send to Gemini youtube model(e.g., please summarize this video)
            youtubeURL : the url to the youtube video (e.g., https://www.youtube.com/watch?v=0lJKucu6HJc)
        Returns:
            after processing by gemini, return the response from Gemini
        """
        return await tools_gemini_api.get_response_from_gemini_youtube(prompt, youtubeURL)
    #
    # @mcp.tool()
    # async def instruction_to_gemini_pro_model(prompt: str):
    #     """
    #     Send the instruction to Gemini pro model
    #
    #     This MCP tool allows AI models to send the prompt to Gemini pro model
    #
    #     Args:
    #         prompt: the instruction that need to be send to Gemini pro model(e.g., please summarize this text)
    #     Returns:
    #         after processing by gemini, return the response from Gemini
    #     """
    #     return await tools_gemini_api.get_response_from_pro_model(prompt)

    @mcp.tool()
    async def instruction_to_gemini_TTS_model(prompt: str):
        """
        Send the instruction to Gemini text to speech model

        This MCP tool allows AI models to send the prompt to Gemini text to speech model

        Args:
            prompt: the instruction that need to be send to Gemini text to speech model(e.g., please read this text : hello world)

        Returns:
            after processing by gemini, return wave file name
        """
        return await tools_gemini_api.get_response_from_text_to_sppech_model(prompt)



    @mcp.tool()
    def server_status():
        """
        Check if the Model Context Protocol server is running.

        This MCP tool provides a simple way to verify the server is operational.

        Returns:
            A status message indicating the server is online
        """
        return {"status": "online", "message": "MCP gemini api Server is running"}

    logger.debug("Model Context Protocol tools registered")


def main():
    """
    Main entry point for the Model Context Protocol gemini api Server.
    """
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Model Context Protocol gemini api Server")
    parser.add_argument("--connection_type", type=str, default=DEFAULT_CONNECTION_TYPE,
                        choices=["http", "stdio"], help="Connection type (http or stdio)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Port to run the server on (default: {DEFAULT_PORT})")
    args = parser.parse_args()

    # Initialize MCP server
    mcp = create_mcp_server(port=args.port)

    # Determine server type
    server_type = "sse" if args.connection_type == "http" else "stdio"

    # Start the server
    logger.info(
        f"🚀 Starting Model Context Protocol gemini api Server on port {args.port} with {args.connection_type} connection")
    mcp.run(server_type)


if __name__ == "__main__":
    main()