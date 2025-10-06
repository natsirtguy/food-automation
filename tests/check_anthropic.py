"""Connectivity check script for Anthropic Claude Vision API - FA-3.

This script tests the Anthropic API connection and demonstrates basic image analysis
for food identification.
"""

import base64
import sys
from pathlib import Path

from anthropic import Anthropic
from anthropic.types import TextBlock

from food_automation.config import config


def encode_image(image_path: Path) -> tuple[str, str]:
    """Encode image to base64 string and detect media type.

    Parameters
    ----------
    image_path : Path
        Path to the image file.

    Returns
    -------
    tuple[str, str]
        Base64-encoded image data and media type.
    """
    with open(image_path, "rb") as image_file:
        image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")

    # Detect media type from extension
    ext = image_path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    media_type = media_types.get(ext, "image/jpeg")

    return image_data, media_type


def test_anthropic_connection() -> bool:
    """Test Anthropic API connectivity with a simple text request.

    Returns
    -------
    bool
        True if connection successful, False otherwise.
    """
    if not config.validate_anthropic():
        print("❌ Anthropic API key not configured")
        print("Set ANTHROPIC_API_KEY in .env file or environment")
        return False

    try:
        client = Anthropic(api_key=config.ANTHROPIC_API_KEY)

        # Simple test request
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=10,
            messages=[{"role": "user", "content": "Say 'API connection successful'"}],
        )

        # Extract text from response with type checking
        content_block = response.content[0]
        if isinstance(content_block, TextBlock):
            result = content_block.text
            print(f"✅ Anthropic API connection successful: {result}")
            return True
        else:
            print(f"❌ Unexpected response type: {type(content_block)}")
            return False

    except Exception as e:
        print(f"❌ Anthropic API connection failed: {e}")
        return False


def test_anthropic_vision(image_path: Path) -> dict:
    """Test Anthropic Vision API with a food image.

    Parameters
    ----------
    image_path : Path
        Path to a fridge/food image.

    Returns
    -------
    dict
        Analysis results with food items identified.
    """
    if not config.validate_anthropic():
        print("❌ Anthropic API key not configured")
        return {}

    try:
        client = Anthropic(api_key=config.ANTHROPIC_API_KEY)

        # Encode image
        image_data, media_type = encode_image(image_path)

        # Analyze image
        # pyright: ignore[reportArgumentType]
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": """Analyze this image and identify all food items visible.
For each item, provide:
- item_name: specific food product
- quantity: count of discrete items
- confidence: 0-1 score
- is_leftover: boolean for containers/homemade food

Return results as a JSON list.""",
                        },
                    ],
                }
            ],
        )

        # Extract text from response with type checking
        content_block = response.content[0]
        if isinstance(content_block, TextBlock):
            result = content_block.text
            print("✅ Anthropic Vision analysis complete")
            print(f"Response: {result}")
            return {"model": "claude-sonnet-4-5-20250929", "response": result, "success": True}
        else:
            error_msg = f"Unexpected response type: {type(content_block)}"
            print(f"❌ {error_msg}")
            return {"success": False, "error": error_msg}

    except Exception as e:
        print(f"❌ Anthropic Vision analysis failed: {e}")
        return {"success": False, "error": str(e)}


def main() -> None:
    """Run Anthropic API connectivity tests."""
    print("=" * 60)
    print("Anthropic Claude Vision API Connectivity Test - FA-3")
    print("=" * 60)
    print()

    # Test 1: Basic connection
    print("Test 1: Basic API connectivity")
    print("-" * 60)
    connection_ok = test_anthropic_connection()
    print()

    if not connection_ok:
        print("Fix the API key issue before proceeding to vision test")
        sys.exit(1)

    # Test 2: Vision analysis (if image provided)
    if len(sys.argv) > 1:
        image_path = Path(sys.argv[1])
        if not image_path.exists():
            print(f"❌ Image file not found: {image_path}")
            sys.exit(1)

        print("Test 2: Vision analysis")
        print("-" * 60)
        print(f"Analyzing image: {image_path}")
        test_anthropic_vision(image_path)
    else:
        print("Test 2: Skipped (no image provided)")
        print("Usage: python test_anthropic.py <path-to-image>")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
