from models import Section, Room, Professor

LUNCH_RANGE = ["12-1 PM", "1-2 PM"]

def is_lunch_break(time_slot: str) -> bool:
    return time_slot in LUNCH_RANGE

def room_is_available(room: Room, day: str, time_slot: str) -> bool:
    return time_slot not in room.schedule.get(day, [])

def professor_is_available(professor: Professor, day: str, time_slot: str) -> bool:
    return time_slot not in professor.schedule.get(day, [])
