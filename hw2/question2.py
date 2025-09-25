a. What is the solution space of this problem? 
Solution space is All possible courses schedules
while C are number of courses, R are number of rooms, T are number of time slots
and the maximum number of option per course = R*T
--> The total number of possible course schedules = (R*T)^C


b. What is the time complexity if we use the exhaustive search on this space? 
Time complexity = O((R*T)^C)

c. Describe a greedy algorithm to solve this problem. 
//Greedy method: difficulty level of courses
1. Sort the courses in descending order of their difficulty level.
- Higher piority for courses with large capacity or courses with instructors with limited availability. (they may have fewer options for scheduling or have to teaching many class)

2. For each course in the sorted list, assign it to the first available room and time slot that does not conflict with already scheduled courses.

3. 
- If no available room and time slot is found for a course, move the course to the next available time slot or room.
- If no slot works, backtrack to the previous course and try a different assignment.

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