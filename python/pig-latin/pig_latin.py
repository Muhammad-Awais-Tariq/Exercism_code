def translate(text):
    """Translate the given English text into Pig Latin.

    Parameters:
        text (str): The text to translate.

    Returns:
        str: The translated text in Pig Latin.
    """

    vowels = ["a" , "e" , "i" , "o" , "u"]
    ay_words = ["xr" , "yt"]

    if text[0] in vowels or text[0:2] in ay_words:
        return f"{text}ay"

    count = 0
    for word in text:
        if word not in vowels:
            count += 1
        else:
            return f"{text[count:]}{text[:count]}ay"