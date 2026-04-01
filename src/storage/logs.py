from src.utils.logger import get_logger

logger = get_logger("LogsSync")

def flush_logs_to_disk():
    """
    Ensure any buffered standard output or append-only logs are fully written.
    In a simple Python logging setup to append-only files, logging module handles this.
    This acts as a placeholder if explicit flush/sync (fsync) is needed later.
    """
    logger.debug("[WARN] Flushing logs to disk")
    pass
