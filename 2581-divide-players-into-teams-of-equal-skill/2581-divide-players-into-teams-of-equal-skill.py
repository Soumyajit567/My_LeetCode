class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) <= 1:
            return -1
        
        skill.sort()
        n = len(skill)
        total_skill = skill[0] + skill[-1]
        
        _sum = 0
        
        for i in range(n // 2):
            if skill[i] + skill[~i] != total_skill:
                return -1
            
            _sum += skill[i] * skill[~i]
        
        return _sum



"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) <= 1:
            return -1
        elif len(skill) == 2:
            return skill[0] * skill[1]
        else:
            skill.sort()
            distribution_count = 0
            mid = len(skill) // 2
            lower = skill[:mid]
            higher = skill[mid:]
            max_partition = lower[0] + higher[-1]
            
            final = []
            for l, h in zip(lower, higher[::-1]):
                if l + h != max_partition:
                    return -1
                final.append((l, h))
        
            _sum = 0
            for a, b in final:
                _sum += (a * b)
        
            return _sum
"""