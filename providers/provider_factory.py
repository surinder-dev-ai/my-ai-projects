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

    return OllamaProvider()