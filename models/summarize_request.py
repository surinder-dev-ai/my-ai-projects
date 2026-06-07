# ---------------------------------------------------------
# Request DTO for Summary API
#
# Java Equivalent:
# SummarizeRequest.java
#
# Purpose:
# Defines expected JSON payload
# ---------------------------------------------------------

from pydantic import BaseModel


class SummarizeRequest(BaseModel):

    # Text that needs summarization
    text: str