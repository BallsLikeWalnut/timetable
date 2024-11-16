from typing import List

class Course:
    def __init__(self, name: str, sessions_per_week: int, eligible_professors: List[str]):
        self.name = name
        self.sessions_per_week = sessions_per_week
        self.eligible_professors = eligible_professors

class Section:
    def __init__(self, name: str):
        self.name = name
        self.schedule = {}  # {day: [time_slots]}
        
class Room:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.capacity = 60
        self.schedule = {} # {day: [time_slots]}

class Professor:
    def __init__(self, name: str, max_sessions_per_day: int):
        self.name = name
        self.max_sessions_per_day = max_sessions_per_day
        self.schedule = {}  # {day: [time_slots]}
