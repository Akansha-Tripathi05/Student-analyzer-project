class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # list of integers

    def average_score(self):
        return sum(self.scores) / len(self.scores)
