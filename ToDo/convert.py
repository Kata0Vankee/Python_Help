para = []
start_write_para = False
this_para = []

with open("file/trang.txt", "r") as f:
    while True:
        line = f.readline()
        para.append(line)
        if (not line): break

print(para)

file_result = open("ForTrang.txt", "w")


def find(str, ch):
    list = []
    for i, ltr in enumerate(str):
        if ltr == ch:
            list.append(i)
    return list


def de_format(sentence):
    sentence = sentence.replace('#', '.')
    return sentence


def en_format(para):
    where_point = find(para, '.')
    for index in where_point:
        if index < len(para) - 1:
            if para[index+1] != ' ' and ((para[index + 1].islower() and para[index-1].islower()) or para[index + 1].isnumeric() and para[index-1].isnumeric()):
                para = para[:index] + '#' + para[index+1:]
    where_point = find(para, '.')
    for index in where_point:
        if index < len(para) - 1:
            if para[index + 1] == '"':
                para = para[:index] + '".' + para[index + 2:]
    while ".. " in para:
        para = para.replace(".. ", ".")

    return para


def write_para(para):
    para = en_format(para)
    to_write_arr = para.split('.')
    for count in range(len(to_write_arr)):
        sentence = to_write_arr[count]
        sentence = de_format(sentence)
        file_result.writelines('\t' + str(count+1) + '. ' + sentence)
        file_result.writelines('\n')
        file_result.writelines('\n')


def combine_line2para(this_para):
    print(this_para)
    count_para = 0
    count = 0
    new_para = ""
    while count < len(this_para):
        line = this_para[count]
        if (count != len(this_para) - 1):
            if line[-1] == '\n' and this_para[count + 1][0].isupper() and (line[0].isupper() or line[0] == ' '):
                new_para += " " + line.replace('\n', "") + "."
                count += 1
                continue
        new_para += " " + line.replace('\n', "")
        count += 1
    print("###new para: "+ new_para)
    write_para(new_para)

'''
for num_line in range(len(para)):
    line = para[num_line]
    if not start_write_para:
        if line == '\n':
            continue
        if line[0] == '1' and len(line) == 8:
            print("count label")
            file_result.writelines(line)
            start_write_para = True
            continue
    else:
        if line == '\n':
            if num_line != len(para) - 1 and para[num_line + 1][0] == '1':
                print("start print")
                combine_line2para(this_para)
                start_write_para = False
                continue
            else:
                continue
        if num_line != len(para) - 1 and para[num_line + 1][0] == '1':
            print("start print")
            combine_line2para(this_para)
            start_write_para = False
            this_para = []
            continue
        this_para.append(line)
'''

text_len = len(para)
print(text_len)
count = 0

while count < text_len:
    line = para[count]
    if line == '\n':
        count += 1
        continue
    if line[0] == '1':
        file_result.writelines(line + '\n')
        print("title: "+line, count)
        count += 1
        while count < text_len - 1 and para[count][0] != '1':
            if para[count] == '\n':
                count += 1
                continue
            this_para.append(para[count])
            count += 1
        combine_line2para(this_para)
        this_para = []


file_result.close()