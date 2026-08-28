class Luhn:
    def __init__(self, card_num): 
        """Initialize a card with a numeric card number. 
        
        Parameters: 
            card_num (str): The card number to be converted to an integer. 
        
        Raises: 
            ValueError: If card_num cannot be converted to an integer. 
        """

        self.card_num = card_num.replace(" " , "")
        
    def valid(self): 
        """Determine whether the card number is valid according to the Luhn algorithm. 
        
        Returns: 
            bool: True if the card number is valid, otherwise False. 
        """

        try:
            num = list(map(int , self.card_num))

        except ValueError:
            return False
        
        if len(num) <= 1:
            return False

        for idx in range(len(num) - 2 , -1 , -2):
            current_num =  int(num[idx]) * 2
            if current_num > 9:
                current_num -= 9

            num[idx] = current_num

        return sum(num) % 10 == 0