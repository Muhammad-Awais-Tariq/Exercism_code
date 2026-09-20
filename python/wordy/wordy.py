def answer(question):
    """Takes the question and returns the answer.

    Parameters:
        question (str): The question that we want solution to.

    Returns:
        int: The answer.
    """

    question_split = question.replace(" by" , "").split(" ")
    question_split[-1] = question_split[-1].replace("?" , "")
    try:
        operands = list(map(int, question_split[2::2]))
    except ValueError:
        raise ValueError("syntax error")
    
    operators = question_split[3::2]
    if len(operands) < 1:
        raise ValueError("syntax error")
    
    total = operands[0]

    for operator in operators:
        if operator.isnumeric():
            raise ValueError("syntax error")
        if operator not in ["plus" , "minus" , "multiplied" , "divided"]:
            raise ValueError("unknown operation")

    if len(operands) != len(operators) + 1:
        raise ValueError("syntax error")

    for i in range(len(operands)-1):
        operator = operators[i]
        operand_2 = operands[i+1]

        if operator == "plus":
            total += operand_2
        elif operator == "minus":
            total -= operand_2
        elif operator == "multiplied":
            total *= operand_2
        elif operator == "divided":
            division = total / operand_2
            total = int(division)

    return total