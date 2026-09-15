class Garden:
    """Represent a kindergarten garden and its assigned plants."""

    def __init__(self, diagram, students = None):

        """Initialize the garden with a diagram and student roster.

        Parameters:
            diagram (str): The two-row garden diagram.
            students (list): The names of the students.
        """

        self.diagram = diagram
        if students is not None:
            self.students = sorted(students)
        else:
            self.students = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]
        self.diagram_rows = diagram.split("\n")

    def plants(self, student):
        """Return the four plants assigned to a student.

        Parameters:
            student (str): The name of the student.

        Returns:
            list: The four plant names assigned to the student.
        """
        plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets",
        }

        plants = []

        required_index = self.students.index(student) * 2

        plants.append(
            self.diagram_rows[0][required_index : required_index + 2]
        )
        plants.append(
            self.diagram_rows[1][required_index : required_index + 2]
        )

        final_answer = []

        for plant in plants:
            for plant_code in plant:
                final_answer.append(plant_names[plant_code])

        return final_answer