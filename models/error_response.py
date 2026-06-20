"""
===============================================================================

File:
    error_response.py

Purpose:
    Standard response model for API errors.

Why created:
    Ensures all endpoints return a consistent error structure.

Architecture Layer:
    DTO / API Contract

Pattern:
    Data Transfer Object (DTO)

SOLID:
    Single Responsibility Principle

Java Equivalent:
    public record ErrorResponse(...)

or

    class ErrorResponseDto

Production Use:
    Standardized API contracts
    Client integrations
    Mobile apps
    External consumers

===============================================================================
"""
from pydantic import BaseModel


class ErrorDetails(BaseModel):
    code: str
    message: str
    request_id: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetails