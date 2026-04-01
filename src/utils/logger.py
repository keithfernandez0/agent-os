import logging
import sys
from pathlib import Path

# Setup basic logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("AgentOS")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Console handler
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)

# File handler (append-only)
fh = logging.FileHandler(LOG_DIR / "agentos.log", mode='a')
fh.setFormatter(formatter)
logger.addHandler(fh)

def get_logger(name: str) -> logging.Logger:
    return logger.getChild(name)
