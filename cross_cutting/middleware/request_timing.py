"""
===============================================================================
File: request_timing.py

Purpose:
    Measures and logs the time taken to process each request.

Architecture:
    Cross-Cutting Concern

Pattern:
    Middleware

Java Equivalent:
    OncePerRequestFilter / HandlerInterceptor
===============================================================================
"""

import logging
import time

from fastapi import Request

logger = logging.getLogger(__name__)


async def log_request_timing(request: Request, call_next):
    """
    Purpose:
        Measure total request processing time.

    Why:
        Helps identify slow APIs and performance bottlenecks.

    Java Equivalent:
        OncePerRequestFilter with timing logic.
    """

    start_time = time.perf_counter()

    response = await call_next(request)

    duration_ms = (time.perf_counter() - start_time) * 1000

    request_id = getattr(request.state, "request_id", "UNKNOWN")

    logger.info(
        "RequestID=%s Method=%s Path=%s Duration=%.2f ms",
        request_id,
        request.method,
        request.url.path,
        duration_ms,
    )

    return response