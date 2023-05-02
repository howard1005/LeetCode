class Solution:
    def average(self, salary: List[int]) -> float:
        return sum([x for x in salary if x < max(salary) and x > min(salary)]) / (len(salary) -2)