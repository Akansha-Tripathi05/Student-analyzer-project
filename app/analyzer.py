from .student import Student

class ScoreAnalyzer:
    def __init__(self):
        self.students = {}  # dictionary

    def add_student(self, student):
        self.students[student.name] = student

    def get_topper(self):
        topper = max(self.students.values(), key=lambda s: s.average_score())
        return topper.name

    def unique_scores(self):
        score_set = set()
        for student in self.students.values():
            score_set.update(student.scores)
        return score_set