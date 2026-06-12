from providers.base_provider import AIProvider
from providers.ollama_provider import OllamaProvider

# =====================================================
#
# - Factory Pattern
# - Dependency Injection
#
# so that llm_service does not create providers itself.
# =====================================================

from providers.provider_factory import get_provider

provider = get_provider()


def ask_llama(question: str) -> str:
    """
    Business operation:
    Ask AI a question.

    Java Equivalent:
    aiProvider.ask(question)
    """
    return provider.ask(question)


def summarize_text(text: str) -> str:
    """
    Business operation:
    Summarize text.

    Currently implemented by prompt engineering.

    Architect Note:
    We are reusing the same provider instead of
    duplicating Ollama-specific code.

    This follows DRY (Don't Repeat Yourself).
    """

    prompt = f"""
Summarize the following text in a concise way:

{text}
"""

    return provider.ask(prompt)