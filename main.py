from typing import Any
from mcp.server.fastmcp import FastMCP

import constants
import screenshot

mcp = FastMCP(constants.SERVER_NAME)

@mcp.tool()
async def take_screenshot(url: str) -> dict[str, Any] | None:
    screenshot_url: str = await screenshot.capture(url)
    if not screenshot_url:
        return "Unable to take screenshot of given url."
    return screenshot_url

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
