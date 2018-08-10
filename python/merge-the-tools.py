def merge_the_tools(string, k):
    begin = 0
    result = []

    for _ in range(len(string) // k):

        result = ""

        for s in list(string[begin:begin+k]):
            if s not in result:
                result += s

        print(result)
        begin += k



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
