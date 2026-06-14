from app_config.config import PROVIDER

from providers.base_provider import AIProvider
from providers.ollama_provider import OllamaProvider


def get_provider() -> AIProvider:
    """
    Returns the configured AI provider.

    For now:
        -> OllamaProvider

    Later:
        -> OpenAIProvider
        -> GeminiProvider
        -> ClaudeProvider
    """

    if PROVIDER.lower() == "ollama":
        return OllamaProvider()

    raise ValueError(f"Unsupported provider: {PROVIDER}")