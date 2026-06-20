"""
===============================================================================
File: request_id.py

Purpose:
--------
This middleware generates (or later reuses) a unique Request ID for every
incoming HTTP request.

The Request ID helps us:
- Trace requests in logs
- Debug production issues
- Correlate logs across multiple services
- Support distributed tracing in the future

Why do we need it?
------------------
Imagine 100 users hitting our API simultaneously.

Without a Request ID:
    INFO Request received
    INFO Calling Ollama
    INFO Returning response

It becomes impossible to know which log belongs to which request.

With a Request ID:
    [8a7c2d] Request received
    [8a7c2d] Calling Ollama
    [8a7c2d] Returning response

Architecture:
-------------
Cross-Cutting Concern

This is NOT business logic.
It applies to every request irrespective of endpoint.

Pattern:
--------
Architectural Pattern:
    Middleware / Interceptor

SOLID:
------
- Single Responsibility Principle
- Open/Closed Principle

Java Equivalent:
----------------
Spring Boot:
    OncePerRequestFilter

or

    HandlerInterceptor

Production Examples:
--------------------
- Authentication
- JWT Validation
- Logging
- Metrics
- Distributed Tracing
- Request Correlation
===============================================================================
"""

import uuid

from fastapi import Request


async def add_request_id(request: Request, call_next):
    """
    Executed automatically for every incoming HTTP request.

    Flow:

        Client
           │
           ▼

      Request ID Middleware

           │

      Generate UUID

           │

      Store in request.state

           │

      Continue Request

           │

      Controller
           │
      Service
           │
      Provider

           │

      Add X-Request-ID Response Header

           │

           ▼

         Client
    """

    # Generate unique request id
    request_id = str(uuid.uuid4())

    # Store it for downstream layers
    request.state.request_id = request_id

    # Continue request processing
    response = await call_next(request)

    # Include request id in response headers
    response.headers["X-Request-ID"] = request_id

    return response