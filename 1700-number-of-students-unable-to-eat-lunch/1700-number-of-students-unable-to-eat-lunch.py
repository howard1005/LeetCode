class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q1 = deque(students)
        q2 = deque(sandwiches)
        
        while q2 and q2[0] in q1:
            if q2[0] == q1[0]:
                q1.popleft()
                q2.popleft()
            else:
                q1.append(q1.popleft())
        
        return len(q1)