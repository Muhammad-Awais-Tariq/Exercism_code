
import string

class PhoneNumber:
    def __init__(self, number):
        """
        Constuctor for storing the number.
        """

        temp_num = number
        new_num = ""
        allowed_punctuations = set([" " , "-" , "." , "(" , ")" , "+"])
        all_punctuations = set(string.punctuation)
        all_letters = set(string.ascii_letters)

        for num in temp_num:
            if num in allowed_punctuations:
                continue

            if num in all_punctuations:
                raise ValueError("punctuations not permitted")

            if num in all_letters:
                raise ValueError("letters not permitted")

            new_num += num

        if len(new_num) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(new_num) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(new_num) == 11 and new_num[0] != "1":
            raise ValueError("11 digits must start with 1")

        if len(new_num) == 11:
            new_num = new_num[1:]

        if new_num[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif new_num[0] == "1":
            raise ValueError("area code cannot start with one")

        if new_num[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if new_num[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = new_num

    def area_code(self):
        """
        Returns the area code the number
        """