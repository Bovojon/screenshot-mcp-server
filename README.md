# screenshot-mcp-server
An MCP server to let agents capture website screenshots 

## Installations
```bash
uv pip install playwright
uv run playwright install           # install all Playwright browsers
uv run playwright install chromium  # individually
```

## Run tests
```bash
pytest tests/
pytest tests/test_screenshot.py::test_capture_success # Running specific test
```
