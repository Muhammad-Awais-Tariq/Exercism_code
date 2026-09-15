class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        """Constructor to intilize the digram and students.

        Parameters:
            digram (str): The plants digram.
            students (list): The students names.
        """

        self.diagram = diagram
        self.students = students
        self.digram_rows = diagram.split("\n")

    def plant(self , student):
        """Determines the plant for the student based on the index.

        Parameters:
            student (str): the student name
        """

        plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets",
        }

        plants = []

        required_index = self.students.index(student) * 2

        plants.append(self.digram_rows[0][required_index:required_index+2])
        plants.append(self.digram_rows[1][required_index:required_index+2])

        final_ans = []

        for plant in plants:
            for plan in plant:
                final_ans.append(plant_names[plan])

        return final_ans