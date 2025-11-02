import pytest
import os
# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent))

from screenshot import capture

@pytest.mark.asyncio
async def test_capture_valid_url_file_created():
    test_url = "https://example.com"
    output_path = "test_screenshot.png"
    if os.path.exists(output_path):
        os.remove(output_path)
    result = await capture(test_url, output_path)
    assert result == output_path
    assert os.path.exists(output_path), "Screenshot file should be created"
    assert os.path.getsize(output_path) > 0, "Screenshot file should not be empty"
    if os.path.exists(output_path):
        os.remove(output_path)

@pytest.mark.asyncio
async def test_capture_invalid_url_file_not_created():
    invalid_url = "not-a-valid-url"
    output_path = "test_screenshot_invalid.png"
    if os.path.exists(output_path):
        os.remove(output_path)
    result = await capture(invalid_url, output_path)
    assert result is None
    assert not os.path.exists(output_path), "Screenshot file should not be created for invalid URL"

@pytest.mark.asyncio
async def test_capture_no_output_path_saves_to_default():
    test_url = "https://example.com"
    default_path = "screenshot.png"
    if os.path.exists(default_path):
        os.remove(default_path)
    result = await capture(test_url)
    assert result == default_path
    assert os.path.exists(default_path), "Default screenshot file should be created"
    if os.path.exists(default_path):
        os.remove(default_path)
