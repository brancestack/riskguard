from fastapi import Request
from fastapi.responses import JSONResponse


async def not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={
            "error": "NOT_FOUND",
            "message": str(exc)
        }
    )


async def bad_request_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "error": "BAD_REQUEST",
            "message": str(exc)
        }
    )


async def conflict_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=409,
        content={
            "error": "CONFLICT",
            "message": str(exc)
        }
    )


async def unauthorized_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=401,
        content={
            "error": "UNAUTHORIZED",
            "message": str(exc)
        }
    )