def reverse(str):
    str_length = len(str)
    if type(str) != str or str_length < 2:
        return 'hmm that is not good'
    
    result = ''
    for i in range(str_length - 1, -1, -1):
        result = result + str[i]

    return result

print(reverse("Hi My name is Andrei"))