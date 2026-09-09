class School:
    """ The school class. """
    def __init__(self):
        """
        Constructor
        """
        self.students = {}

    def add_student(self, name, grade):
        """Adds the students to the school dict
        
        """

        all_names = [name for names in self.students.values() for name in names]
        if name not in all_names:
            if grade in self.students:
                self.students[grade].append(name)
            else:
                self.students[grade] = [name]
        

    def roster(self):

        sorted_students = sorted(self.students.items() , key= lambda x : x[0])

        final_students = []

        for student in sorted_students:
            alphabetical_names = sorted(student[1])
            for students in alphabetical_names:
                final_students.append(students)


        return final_students

    def grade(self, grade_number):
        pass

    def added(self):
        pass
