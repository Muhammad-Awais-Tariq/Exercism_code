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
        pass

    def grade(self, grade_number):
        pass

    def added(self):
        pass
