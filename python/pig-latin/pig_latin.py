def translate(text):
    """Translate the given English text into Pig Latin.

    Parameters:
        text (str): The text to translate.

    Returns:
        str: The translated text in Pig Latin.
    """

    vowels = ["a", "e", "i", "o", "u"]
    ay_words = ["xr", "yt"]

    translated_words = []

    for word in text.split():

        if word[0] in vowels or word[:2] in ay_words:
            translated_words.append(f"{word}ay")
            continue

        qu_index = word.find("qu")

        if qu_index != -1:
            first_vowel = next(
                (i for i, char in enumerate(word) if char in vowels),
                len(word)
            )

            if qu_index <= first_vowel:
                split_index = qu_index + 2
                translated_words.append(
                    f"{word[split_index:]}{word[:split_index]}ay"
                )
                continue

        y_index = word.find("y")

        if y_index > 0:
            first_vowel = next(
                (i for i, char in enumerate(word) if char in vowels),
                len(word)
            )

            if y_index <= first_vowel:
                translated_words.append(
                    f"{word[y_index:]}{word[:y_index]}ay"
                )
                continue

        count = 0

        for char in word:
            if char in vowels:
                break
            count += 1

        translated_words.append(
            f"{word[count:]}{word[:count]}ay"
        )

    return " ".join(translated_words)