import sqlite3
import threading
from pathlib import Path
from typing import Optional

DB_PATH = Path("agentos.db")
_local = threading.local()

def get_connection() -> sqlite3.Connection:
    """
    Get a thread-local SQLite connection.
    Ensures safe concurrent access in minimal setups.
    """
    if not hasattr(_local, "conn"):
        _local.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        _local.conn.row_factory = sqlite3.Row
    return _local.conn

def init_db():
    """Initialize the SQLite database schema."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            input TEXT NOT NULL,
            agent TEXT NOT NULL,
            status TEXT NOT NULL,
            result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id TEXT PRIMARY KEY,
            task_id TEXT NOT NULL,
            agent TEXT NOT NULL,
            input TEXT NOT NULL,
            output TEXT NOT NULL,
            feedback TEXT NOT NULL,
            processed BOOLEAN DEFAULT FALSE,
            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(task_id) REFERENCES tasks(id)
        )
    ''')
    
    conn.commit()

# Initialize DB on import
init_db()
