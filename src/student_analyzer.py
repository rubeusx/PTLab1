from typing import List, Tuple, Dict
# DataType = Dict[str, List[Tuple[str,int]]]


class StudentAnalyzer:

    def __init__(self, data: Dict[str, List[Tuple[str, int]]]):
        self.data = data

    def count_excellent_students(self) -> int:
        """Количество студентов, у которых все предметы ≥ 90."""
        count = 0
        for subjects in self.data.values():
            # subjects — список кортежей (предмет, балл)
            if all(score >= 90 for _, score in subjects):
                count += 1
        return count
