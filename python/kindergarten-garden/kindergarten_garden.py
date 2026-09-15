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