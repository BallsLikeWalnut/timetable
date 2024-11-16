def assign_course_session(course, section, day, time_slot, room, professor):
    # Update each entity’s schedule to reflect this assignment
    section.schedule.setdefault(day, []).append(time_slot)
    room.schedule.setdefault(day, []).append(time_slot)
    professor.schedule.setdefault(day, []).append(time_slot)
    print(f" {course.name} -- {section.name} in {room.room_id} with {professor.name} at {time_slot} on {day}")
