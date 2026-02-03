import time
from collections import defaultdict
from fastapi import Request, HTTPException
from .config import settings

requests_log = defaultdict(list)

def rate_limit(request: Request):
    ip = request.client.host
    now = time.time()

    window = 60
    max_requests = settings.RATE_LIMIT_PER_MINUTE

    requests_log[ip] = [
        t for t in requests_log[ip] if now - t < window
    ]

    if len(requests_log[ip]) >= max_requests:
        raise HTTPException(
            status_code=429,
            detail="Muitas requisições. Tente novamente em 1 minuto."
        )

    requests_log[ip].append(now)
