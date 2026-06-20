"""
===============================================================================
File: request_logging.py

Purpose:
--------
Logs every incoming HTTP request and outgoing HTTP response.

Why do we need it?
------------------
Production systems process thousands of requests.

Request logging helps:
- Debug production issues
- Track API usage
- Measure performance
- Correlate logs using Request ID
- Troubleshoot customer issues

Architecture:
-------------
Cross Cutting Concern

Pattern:
--------
Middleware

SOLID:
------
Single Responsibility Principle

Java Equivalent:
----------------
Spring OncePerRequestFilter
or
HandlerInterceptor

Production Usage:
-----------------
Every serious backend system logs requests.

Future Enhancements:
--------------------
- Request Duration
- User Id
- Client IP
- Trace Id
- OpenTelemetry
===============================================================================
"""

import logging

from fastapi import Request

logger = logging.getLogger(__name__)


async def log_requests(request: Request, call_next):
    """
    Logs incoming request and outgoing response.

    Flow:

        Client
            │
            ▼

      Logging Middleware

            │

      Log Incoming Request

            │

            ▼

        Controller

            │

        Business Logic

            │

      Log Outgoing Response

            │

            ▼

          Client
    """

    request_id = getattr(request.state, "request_id", "UNKNOWN")

    logger.info(
        f"[{request_id}] Incoming Request : {request.method} {request.url.path}"
    )

    response = await call_next(request)

    logger.info(
        f"[{request_id}] Outgoing Response : Status={response.status_code}"
    )

    return response