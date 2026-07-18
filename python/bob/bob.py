def response(hey_bob):
    """Determine how Bob responds to a given statement.

    Parameters:
        hey_bob (str): The statement addressed to Bob.

    Returns:
        str: Bob's response.

    Response rules:
        - "Sure." if the statement is a question.
        - "Whoa, chill out!" if the statement is yelled.
        - "Calm down, I know what I'm doing!" if the statement is a yelled question.
        - "Fine. Be that way!" if the statement is empty or contains only whitespace.
        - "Whatever." for anything else.
    """

    if hey_bob.strip().endswith("?"):
        return "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"