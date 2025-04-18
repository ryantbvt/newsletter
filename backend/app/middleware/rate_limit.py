''' Rate limiter middleware'''

from fastapi import FastAPI, Request, Response
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from typing import Callable, Awaitable, Any

from app.schemas.config import Config

def setup_rate_limiter(app: FastAPI, config: Config) -> Limiter:
    '''
    Description: Setup rate limiter with configuration.

    Args:
        app: FastAPI app instance.
        config: Config instance.

    Returns:
        Limiter instance.
    '''
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    return limiter

async def rate_limit_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Any]],
    config: Config
) -> Any:
    """
    Apply rate limiting based on the request path and configuration.
    """
    # Skip rate limiting for excluded paths
    if request.url.path in config.rate_limits.exclude_paths:
        return await call_next(request)

    # Get the rate limit for the specific path if defined
    rate_limit = config.rate_limits.custom_paths.get(request.url.path, config.rate_limits.default)

    # Apply the rate limit
    limiter = request.app.state.limiter
    
    # Create a dummy function that will be rate limited
    async def dummy_handler(request: Request):
        return await call_next(request)
    
    # Apply the rate limit to the dummy handler
    rate_limited_handler = limiter.limit(rate_limit)(dummy_handler)
    
    # Call the rate limited handler
    return await rate_limited_handler(request)