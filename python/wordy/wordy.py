def answer(question):
    """Takes the question and returns the answer.

    Parameters:
        question (str): The question that we want solution to.

    Returns:
        int: The answer.
    """

    question_split = question.replace(" by" , "").split(" ")
    question_split[-1] = question_split[-1].replace("?" , "")
    operands = list(map(int, question_split[2::2]))
    operators = question_split[3::2]
    total = operands[0]

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

print(answer("What is 5 plus 13 plus 6?"))