def is_first_sounded(first):
    return first == 'a' or 'o' or 'e' or 'i' or 'u'


def encoding_names(name):
    entered_name = name.lower()
    name_list = list(entered_name)
    string_list = ''.join(name_list)

    if is_first_sounded(name_list[0]):
        return string_list[1:] + string_list[0] + 'v'
    else:
        string_two_first = ''.join(name_list[0:2])
        return string_list[2:] + string_two_first


value = encoding_names('Ali')

print(value)
