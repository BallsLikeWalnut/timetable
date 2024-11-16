from models import Course, Section, Room, Professor
from constraints import is_lunch_break, room_is_available, professor_is_available
from utils import assign_course_session
from typing import List

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TIME_SLOTS = ["9-10 AM", "10-11 AM", "11-12 PM", "12-1 PM", "1-2 PM", "2-3 PM", "3-4 PM"]

def schedule_courses(courses: List[Course], sections: List[Section], rooms: List[Room], professors: List[Professor]):
    for section in sections:  # Iterate through all sections
        for course in courses:
            sessions_needed = course.sessions_per_week
            for day in DAYS_OF_WEEK:
                for time_slot in TIME_SLOTS:
                    if is_lunch_break(time_slot):
                        continue  # Skip lunch slots
                    
                    # Try to find an available room and professor for this course
                    for room in rooms:
                        if not room_is_available(room, day, time_slot):
                            continue  # Skip if the room is not available

                        for professor_name in course.eligible_professors:
                            professor = next((p for p in professors if p.name == professor_name), None)
                            if not professor or not professor_is_available(professor, day, time_slot):
                                continue

                            # Schedule this session
                            assign_course_session(course, section, day, time_slot, room, professor)
                            sessions_needed -= 1

                            if sessions_needed == 0:
                                break
                        if sessions_needed == 0:
                            break
                if sessions_needed == 0:
                    break
