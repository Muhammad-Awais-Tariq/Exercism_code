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

    if text[0] not in vowels and "qu" in text:
        if text[0:2] == "qu":
            return f"{text[2:]}{text[:2]}ay"
        else:
            count = 0
            for word in range(len(text)):
                if text[word] != "q" and text[word+1] != "u":
                    count += 1
                else:
                    return f"{text[count+2:]}{text[:count+2]}ay"

    if text[0] not in vowels:
        count = 0
        for word in range(len(text)):
            if text[word] not in vowels and text[word] != "y":
                count += 1
            else:
                return f"{text[count:]}{text[:count]}ay"
            
    count = 0
    for word in text:
        if word not in vowels:
            count += 1
        else:
            return f"{text[count:]}{text[:count]}ay"