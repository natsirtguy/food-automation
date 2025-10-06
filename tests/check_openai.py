"""Connectivity check script for OpenAI Vision API - FA-3.

This script tests the OpenAI API connection and demonstrates basic image analysis
for food identification.
"""

import base64
import sys
from pathlib import Path

from openai import OpenAI

from food_automation.config import config


def encode_image(image_path: Path) -> str:
    """Encode image to base64 string.

    Parameters
    ----------
    image_path : Path
        Path to the image file.

    Returns
    -------
    str
        Base64-encoded image data.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def test_openai_connection() -> bool:
    """Test OpenAI API connectivity with a simple text request.

    Returns
    -------
    bool
        True if connection successful, False otherwise.
    """
    if not config.validate_openai():
        print("❌ OpenAI API key not configured")
        print("Set OPENAI_API_KEY in .env file or environment")
        return False

    try:
        client = OpenAI(api_key=config.OPENAI_API_KEY)

        # Simple test request
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Say 'API connection successful'"}],
            max_tokens=10,
        )

        result = response.choices[0].message.content
        print(f"✅ OpenAI API connection successful: {result}")
        return True

    except Exception as e:
        print(f"❌ OpenAI API connection failed: {e}")
        return False


def test_openai_vision(image_path: Path) -> dict:
    """Test OpenAI Vision API with a food image.

    Parameters
    ----------
    image_path : Path
        Path to a fridge/food image.

    Returns
    -------
    dict
        Analysis results with food items identified.
    """
    if not config.validate_openai():
        print("❌ OpenAI API key not configured")
        return {}

    try:
        client = OpenAI(api_key=config.OPENAI_API_KEY)

        # Encode image
        base64_image = encode_image(image_path)

        # Analyze image
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
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
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                                "detail": "high",
                            },
                        },
                    ],
                }
            ],
            max_tokens=1000,
        )

        result = response.choices[0].message.content
        print("✅ OpenAI Vision analysis complete")
        print(f"Response: {result}")

        return {"model": "gpt-4o", "response": result, "success": True}

    except Exception as e:
        print(f"❌ OpenAI Vision analysis failed: {e}")
        return {"success": False, "error": str(e)}


def main() -> None:
    """Run OpenAI API connectivity tests."""
    print("=" * 60)
    print("OpenAI Vision API Connectivity Test - FA-3")
    print("=" * 60)
    print()

    # Test 1: Basic connection
    print("Test 1: Basic API connectivity")
    print("-" * 60)
    connection_ok = test_openai_connection()
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
        test_openai_vision(image_path)
    else:
        print("Test 2: Skipped (no image provided)")
        print("Usage: python test_openai.py <path-to-image>")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
