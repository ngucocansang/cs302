"""
Input: 
    C = list of courses (each with capacity, instructor, major)
    R = list of rooms (each with capacity)
    T = list of time slots

Output:
    Schedule mapping course → (room, time slot)

Algorithm:
1. Sort C by "difficulty":
       - Larger course capacity first
       - Or instructors/majors with many conflicts
       (this makes hard-to-schedule courses go first)

2. For each course in sorted C:
       For each (room, time) in (R × T):
           If room.capacity ≥ course.capacity
              AND instructor of course not already teaching at 'time'
              AND no course of same major at 'time'
           Then:
              Assign course → (room, time)
              Mark room + instructor + major as occupied at this time
              Break

       If no suitable (room, time) found:
           Place course in earliest available slot 
           (even if it is 8:00am or 6:00pm)

3. Return Schedule
"""