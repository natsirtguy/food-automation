"""Configuration management for food automation system.

Loads API keys and settings from environment variables.
"""

import os
from pathlib import Path
from typing import Literal

# Load .env file if it exists
try:
    from dotenv import load_dotenv

    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass  # python-dotenv not required, but helpful for development


class Config:
    """Application configuration loaded from environment variables."""

    # OpenAI settings
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")

    # Anthropic settings
    ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY")

    # AWS settings
    AWS_ACCESS_KEY_ID: str | None = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str | None = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")

    # Application settings
    AI_SERVICE: Literal["openai", "anthropic", "aws"] = os.getenv(
        "AI_SERVICE",
        "openai",  # type: ignore[assignment]
    )
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate_openai(cls) -> bool:
        """Check if OpenAI configuration is valid.

        Returns
        -------
        bool
            True if OpenAI API key is configured.
        """
        return cls.OPENAI_API_KEY is not None and cls.OPENAI_API_KEY.startswith("sk-")

    @classmethod
    def validate_anthropic(cls) -> bool:
        """Check if Anthropic configuration is valid.

        Returns
        -------
        bool
            True if Anthropic API key is configured.
        """
        return cls.ANTHROPIC_API_KEY is not None and cls.ANTHROPIC_API_KEY.startswith("sk-ant-")

    @classmethod
    def validate_aws(cls) -> bool:
        """Check if AWS configuration is valid.

        Returns
        -------
        bool
            True if AWS credentials are configured.
        """
        return (
            cls.AWS_ACCESS_KEY_ID is not None
            and cls.AWS_SECRET_ACCESS_KEY is not None
            and cls.AWS_ACCESS_KEY_ID.startswith("AKIA")
        )


# Global config instance
config = Config()
