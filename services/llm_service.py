# ---------------------------------------------------------
# Service Layer
#
# Java equivalent:
# @Service class
#
# Why needed?
# Business logic should not stay inside controller/routes.
#
# Controllers should:
# - receive request
# - validate request
# - call service layer
#
# This improves:
# - maintainability
# - testing
# - scalability
# ---------------------------------------------------------

from app_config.config import MODEL_NAME
from ollama import chat
from app_logging.logger_config import logger
from providers.ollama_provider import ask_model


def ask_llama(question: str):

    return ask_model(question)
# ---------------------------------------------------------
# Summarization Service
#
# Java Equivalent:
# service.summarize(...)
#
# Why?
# Encapsulates AI prompt logic.
# ---------------------------------------------------------

def summarize_text(text: str):

    prompt = f"""
    Summarize the following text in 3 bullet points:

    {text}
    """

    return ask_model(prompt)