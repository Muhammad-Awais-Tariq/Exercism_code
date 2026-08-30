
import random
import string

class Robot:

    all_names = set()

    def __init__(self):
        """
        Initializes the robot name attribute.
        """

        self.robot_name = None


    def name(self):
        """Return the robot's name, generating one if necessary.

        Returns:
            str: The robot's name.
        """

        if self.robot_name:
            return self.robot_name

        while True:
            random_name = "".join(random.choices(string.ascii_uppercase , k = 2))
            random_name += str(random.randint(100 , 999 ))

            if random_name not in self.all_names:
                self.robot_name = random_name
                self.all_names.add(random_name)
                return self.robot_name


    def reset(self):
        """
        Resets the robot name so its eligible for a new one
        """

        if self.robot_name:
            self.robot_name = None