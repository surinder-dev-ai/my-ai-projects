"""
===============================================================================
File: json_logger.py

Purpose:
    Utility for writing structured JSON logs.

Architecture:
    Cross-Cutting

Java Equivalent:
    Logback JSON Encoder / Logstash Encoder
===============================================================================
"""

import json
import logging

logger = logging.getLogger(__name__)


def log_json(**kwargs):
    """
    Purpose:
        Write structured JSON logs.

    Why:
        Machine-readable logs are easier to search and analyze.

    Java Equivalent:
        logger.info(objectMapper.writeValueAsString(...))
    """

    logger.info(json.dumps(kwargs))