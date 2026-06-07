from ollama import chat

from app_config.config import MODEL_NAME


def ask_model(prompt: str):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]