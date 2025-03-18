import logging
from datetime import datetime
from http import HTTPStatus
from typing import Tuple, Dict

from clean_architecture.modules.useсases import EventUseCases
from clean_architecture.modules.entities import Client, Location

logger = logging.getLogger(__name__)

class EventController:
    def __init__(self, event_use_cases: EventUseCases):
        self.event_use_cases = event_use_cases

    def create_event(self, params: Dict) -> Tuple[Dict, int]:
        logger.info("Creating event with params: %s", str(params))
        
        try:
            location = Location(id=params['location_id'], address="")
            client = Client(id=params['client_id'], name="")
            event_start = datetime.fromisoformat(params['event_start'])
            event_end = datetime.fromisoformat(params['event_end'])

            event = self.event_use_cases.create_event(location, client, event_start, event_end)
            logger.info("Event successfully created: %s", str(event))
            return {"message": "Event created successfully", "event": vars(event)}, HTTPStatus.CREATED.value
        
        except ValueError as e:
            logger.error("Error creating event: %s", str(e))
            return {"error": str(e)}, HTTPStatus.BAD_REQUEST.value

    def update_event(self, event_id: int, params: Dict) -> Tuple[Dict, int]:
        logger.info("Updating event ID %d with params: %s", event_id, str(params))
        
        try:
            location = Location(id=params['location_id'], address="")
            client = Client(id=params['client_id'], name="")
            event_start = datetime.fromisoformat(params['event_start'])
            event_end = datetime.fromisoformat(params['event_end'])

            event = self.event_use_cases.update_event(event_id, location, client, event_start, event_end)
            logger.info("Event successfully updated: %s", str(event))
            return {"message": "Event updated successfully", "event": vars(event)}, HTTPStatus.OK.value
        
        except ValueError as e:
            logger.error("Error updating event: %s", str(e))
            return {"error": str(e)}, HTTPStatus.BAD_REQUEST.value

    def delete_event(self, event_id: int) -> Tuple[Dict, int]:
        logger.info("Deleting event ID %d", event_id)

        try:
            self.event_use_cases.delete_event(event_id)
            logger.info("Event ID %d successfully deleted", event_id)
            return {"message": "Event deleted successfully"}, HTTPStatus.NO_CONTENT.value
        
        except ValueError as e:
            logger.error("Error deleting event: %s", str(e))
            return {"error": str(e)}, HTTPStatus.BAD_REQUEST.value

    def view_events(self) -> Tuple[Dict, int]:
        logger.info("Fetching all events")

        events = self.event_use_cases.view_events()
        events_data = [vars(event) for event in events]

        logger.info("Retrieved %d events", len(events))
        return {"events": events_data}, HTTPStatus.OK.value