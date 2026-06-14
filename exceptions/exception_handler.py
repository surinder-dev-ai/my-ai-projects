from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.custom_exceptions import AIProviderException


async def ai_provider_exception_handler(
    request: Request,
    exc: AIProviderException,
):
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc)
        },
    )