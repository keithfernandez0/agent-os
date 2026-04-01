from src.storage.db import get_connection

def synchronize_session():
    """
    Ensure memory state matches disk for active session.
    Forces connection commit and pragma sync.
    """
    conn = get_connection()
    conn.commit()
    conn.execute('PRAGMA wal_checkpoint(FULL)')
