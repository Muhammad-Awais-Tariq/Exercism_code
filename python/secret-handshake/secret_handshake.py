def commands(binary_str):
    """Return the actions represented by the given binary string.

    Parameters:
        binary_str (str): The binary string to decode.

    Returns:
        list: The decoded actions in the order they should be performed.
    """

    code_dict = {
        0 : "wink",
        1 : "double blink",
        2 : "close your eyes",
        3 : "jump"
    }

    one_index = [i for i,char in enumerate(binary_str) if char == "1"]