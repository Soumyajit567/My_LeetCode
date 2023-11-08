class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        reduced_damage = min(armor, max_damage)
        total_damage = sum(damage) - reduced_damage
        return total_damage + 1