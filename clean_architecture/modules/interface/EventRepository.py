from dataclasses import dataclass
from typing import List
from datetime import datetime
from clean_architecture.modules.entities import Location, Event



@dataclass
class EventRepository:
    data_base_repository: object

    def save(self, event: Event) -> Event:
        return self.data_base_repository.save(event)

    def get(self, event_id: int) -> Event:
        return self.data_base_repository.get(event_id)

    def delete(self, event: Event) -> None:
        return self.data_base_repository.delete(event)

    def get_all(self) -> List[Event]:
        return self.data_base_repository.get_all()

    def get_by_location_and_time(self, location: Location, event_start: datetime, event_end: datetime) -> List[Event]:
        return self.data_base_repository.get_by_location_and_time(location, event_start, event_end)