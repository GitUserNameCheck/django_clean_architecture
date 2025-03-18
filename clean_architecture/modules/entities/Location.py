from dataclasses import dataclass
from typing import Optional

@dataclass
class Location:
    id: Optional[int]
    address: Optional[str]
