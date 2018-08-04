def count_substring(string, sub_string):

    count = 0
    flag = 0

    for letter in string:
        if letter == sub_string[flag]:
            flag += 1
            if flag == len(sub_string):
                if letter == sub_string[0]:
                    flag = 1
                else:
                    flag = 0
                count += 1
        else:
            flag = 0
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
