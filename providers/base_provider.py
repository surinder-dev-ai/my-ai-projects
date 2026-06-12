"""
====================================================

PURPOSE

Defines a common contract for all AI providers.

Java Equivalent:

public interface AIProvider {
    String ask(String question);
}

ARCHITECTURAL PATTERN

Strategy Pattern

WHY?

Service layer should depend on abstraction,
not on Ollama/OpenAI implementation.

SOLID Principle:

Dependency Inversion Principle

====================================================
"""

from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def ask(self, question: str) -> str:
        """
        Every provider must implement this.

        Java Equivalent:

        interface AIProvider {
            String ask(String question);
        }
        """
        pass