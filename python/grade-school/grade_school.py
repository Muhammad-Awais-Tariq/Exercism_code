class School:
    """Represent a school and its student roster."""

    def __init__(self):
        """Initialize an empty school roster."""
        self.students = {}
        self.admitted = []

    def add_student(self, name, grade):
        """Add a student to the specified grade.

        Parameters:
            name (str): The student's name.
            grade (int): The grade the student belongs to.
        """
        all_names = [
            student_name
            for student_names in self.students.values()
            for student_name in student_names
        ]

        if name not in all_names:
            if grade in self.students:
                self.students[grade].append(name)
            else:
                self.students[grade] = [name]

            self.admitted.append(True)
        else:
            self.admitted.append(False)

    def roster(self):
        """Return all students sorted by grade and then by name.

        Returns:
            list: All students in grade and alphabetical order.
        """
        sorted_grades = sorted(self.students.items(), key=lambda item: item[0])
        final_students = []

        for grade, student_names in sorted_grades:
            for student_name in sorted(student_names):
                final_students.append(student_name)

        return final_students

    def grade(self, grade_number):
        """Return students enrolled in a specific grade.

        Parameters:
            grade_number (int): The grade to retrieve.

        Returns:
            list: Students in the specified grade, sorted alphabetically.
        """
        if grade_number not in self.students:
            return []

        return sorted(self.students[grade_number])

    def added(self):
        """Return the results of all student addition attempts.

        Returns:
            list: True for successful additions and False for duplicates.
        """
        return self.admitted