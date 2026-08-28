class Luhn:
    def __init__(self, card_num): 
        """Initialize a card with a numeric card number. 
        
        Parameters: 
            card_num (str): The card number to be converted to an integer. 
        
        Raises: 
            ValueError: If card_num cannot be converted to an integer. 
        """

        try:
            self.card_num = int(card_num.replace(" " , ""))
        except ValueError:
            raise("Please enter the integer value.")
        
    def valid(self): 
        """Determine whether the card number is valid according to the Luhn algorithm. 
        
        Returns: 
            bool: True if the card number is valid, otherwise False. 
        """

        num = self.card_num

        if num <= 1:
            return False

