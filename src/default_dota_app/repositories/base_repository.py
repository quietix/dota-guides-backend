from functools import wraps
from typing import Callable, Any, Tuple, Optional
import logging

logger = logging.getLogger(__name__)

class BaseRepository:
    @staticmethod
    def _generate_error_message(message: str) -> dict:
        return {"details": message}

    @classmethod
    def handle_repository_exceptions(cls, error_description: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Tuple[Optional[Any], Optional[dict]]:
                try:
                    res, error = func(*args, **kwargs)

                    if res:
                        return res, None
                    elif error:
                        return None, cls._generate_error_message(error)
                    else:
                        return None, cls._generate_error_message(error_description)

                except Exception as e:
                    logger.error(f"{error_description} {e}")
                    return None, cls._generate_error_message(error_description)

            return wrapper
        return decorator