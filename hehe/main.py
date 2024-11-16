from models import Course, Section, Room, Professor
from scheduler import schedule_courses

# Create sample data
courses = [Course("Mathematics", 3, ["Prof. A", "Prof. B"])]
sections = [Section("Year 1, Section A"), Section("Year 1, Section B")]
rooms = [Room("Room 101"), Room("Room 102")]
professors = [Professor("Prof. A", 3), Professor("Prof. B", 3)]

# Run the scheduler
schedule_courses(courses, sections, rooms, professors)