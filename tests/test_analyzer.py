import sys
from pathlib import Path

# Add the parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.student import Student
from app.analyzer import ScoreAnalyzer


def test_topper():
    s1 = Student("Akansha", [90, 95, 92])
    s2 = Student("Rahul", [80, 85, 88])
    
    analyzer = ScoreAnalyzer()
    analyzer.add_student(s1)
    analyzer.add_student(s2)
    
    assert analyzer.get_topper() == "Akansha"