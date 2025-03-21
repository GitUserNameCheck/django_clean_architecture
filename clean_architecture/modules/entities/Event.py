from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from . import Location, Client

@dataclass
class Event:
    location: Location
    client: Client
    event_start: Optional[datetime]
    event_end: Optional[datetime]
    id: Optional[int] = None