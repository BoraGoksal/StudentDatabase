import csv
import matplotlib.pyplot as plt
import seaborn as sns
from student import storing_student_data
class StudManager:
    def __init__(self):
        self.students = {}

    def adding_student(self, studentid,name,address):
        if studentid not in self.students:
            self.students[studentid] = storing_student_data(studentid,name,address)
            self.saveChanges()
