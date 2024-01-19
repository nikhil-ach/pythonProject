def nine_1(letters):
    result = []
    for index, item in enumerate(letters):
        output = f'{item}, {index + 1}'
        result.append(output)
    return '\n'.join(result)
