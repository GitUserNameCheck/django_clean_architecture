from typing import List
from datetime import datetime
from dataclasses import dataclass
from clean_architecture.modules.entities import Client, Location, Event

@dataclass
class EventUseCases:
    event_repository: object
    
    def create_event(self, location: Location, client: Client, event_start: datetime, event_end: datetime) -> Event:
        if self._is_event_conflict(location, event_start, event_end):
            raise ValueError("An event is already scheduled at this location during the specified time.")
        event = Event(location=location, client=client, event_start=event_start, event_end=event_end)
        return self.event_repository.save(event)

    def delete_event(self, event_id: int):
        return self.event_repository.delete(event_id)

    def update_event(self, event_id: int, location: Location, client: Client, event_start: datetime, event_end: datetime) -> Event:
        if self._is_event_conflict(location, event_start, event_end):
            raise ValueError("An event is already scheduled at this location during the specified time.")
        event = self.event_repository.get(event_id)
        if not event:
            raise ValueError(f"Event with id {event_id} not found.")
        event.location = location
        event.client = client
        event.event_start = event_start
        event.event_end = event_end
        return self.event_repository.save(event)

    def view_events(self, quantity: int) -> List[Event]:
        return self.event_repository.get_all()

    def _is_event_conflict(self, location: Location, event_start: datetime, event_end: datetime) -> bool:
        events = self.event_repository.get_by_location_and_time(location, event_start, event_end)
        return len(events) > 0