class storing_student_data:
    '''
    This class stores information about the student
    '''
    def __init__(self,studentid, name, address):
        self.studentid = studentid
        self.name = name
        self.address = address
        self.grades = {}

    def add_student_grades(self,mod,grade):
        self.grade[mod] = grade

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades.values())/len(self.grades)
        return 0
