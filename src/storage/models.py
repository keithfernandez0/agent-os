import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: str
    input: str
    agent: str
    status: str
    result: Optional[str] = None
    created_at: Optional[str] = None

@dataclass
class Feedback:
    id: str
    task_id: str
    agent: str
    input: str
    output: str
    feedback: str # e.g. "like", "dislike", or textual
    processed: bool = False
    ts: Optional[str] = None
