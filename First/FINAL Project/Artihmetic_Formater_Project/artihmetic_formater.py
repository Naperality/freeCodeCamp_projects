# Solution 

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate width
        width = max(len(num1), len(num2)) + 2

        # Format each line
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))

    # Join lines with 4 spaces between
    arranged = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)

    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')