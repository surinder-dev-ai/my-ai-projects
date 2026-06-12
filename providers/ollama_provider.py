"""
=========================================================

PURPOSE

Concrete implementation of AIProvider.

Java Equivalent:

public class OllamaProvider implements AIProvider {

    @Override
    public String ask(String question) {
        ...
    }
}

ARCHITECTURAL PATTERN

Strategy Pattern

This is one strategy (Ollama).

Tomorrow we can add:

- OpenAIProvider
- GeminiProvider
- ClaudeProvider

without changing business logic.

=========================================================
"""

from ollama import chat

from app_config.config import MODEL_NAME

from providers.base_provider import AIProvider


class OllamaProvider(AIProvider):

    def ask(self, question: str) -> str:

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]