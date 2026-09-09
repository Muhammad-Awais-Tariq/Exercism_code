class School:
    """ The school class. """
    def __init__(self):
        """
        Constructor
        """
        self.students = {}
        self.admitted = []

    def add_student(self, name, grade):
        """Adds the students to the school dict
        
        """

        all_names = [name for names in self.students.values() for name in names]
        if name not in all_names:
            if grade in self.students:
                self.students[grade].append(name)
            else:
                self.students[grade] = [name]
            self.admitted.append(True)
        else:
            self.admitted.append(False)
        

    def roster(self):

        sorted_students = sorted(self.students.items() , key= lambda x : x[0])

        final_students = []

        for student in sorted_students:
            alphabetical_names = sorted(student[1])
            for students in alphabetical_names:
                final_students.append(students)


        return final_students

    def grade(self, grade_number):

        if grade_number not in self.students:
            return []
        else:
            student_names_sorted = []
            sorted_students = sorted(self.students[grade_number])
            for stn in sorted_students:
                student_names_sorted.append(stn)

            return student_names_sorted


    def added(self):
        return self.admitted
