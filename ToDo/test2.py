def find(str, ch):
    list = []
    for i, ltr in enumerate(str):
        if ltr == ch:
            list.append(i)
    return list


def en_format(para):
    where_point = find(para, '.')
    for index in where_point:
        if index < len(para) - 1:
            if para[index + 1] == '"':
                para = para[:index] + '".' + para[index + 2:]
    return para

str = '"dwdwdd." dwdwdwd "wegvrgr."'
print(str)
str = en_format(str)
print(str)

print("7".isnumeric())