from ollama import chat

from app_config.config import MODEL_NAME
from providers.base_provider import AIProvider
from exceptions.custom_exceptions import AIProviderException


class OllamaProvider(AIProvider):

    def ask(self, question: str) -> str:

        try:
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

        except Exception as e:
            raise AIProviderException(
                f"Failed to communicate with Ollama: {e}"
            )