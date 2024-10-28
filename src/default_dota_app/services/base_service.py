class BaseService:
    @staticmethod
    def _generate_error_message(message: str) -> dict:
        return {"details": message}