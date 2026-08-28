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

        num = list(map(int , self.card_num))
        
        if len(num) <= 1:
            return False

        for idx in range(len(num) - 2 , -1 , -2):
            num[idx] = int(num[idx]) ** 2

        return sum(num) % 2 == 0