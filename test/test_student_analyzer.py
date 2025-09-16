# tests/test_student_analyzer.py
from student_analyzer import StudentAnalyzer


def test_count_excellent_students():
    data = {
        "Иванов": [("математика", 90), ("литература", 92)],
        "Петров": [("математика", 100), ("литература", 89)],
    }
    analyzer = StudentAnalyzer(data)
    assert analyzer.count_excellent_students() == 1
