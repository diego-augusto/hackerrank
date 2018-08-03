if __name__ == '__main__':

    m_dict = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in m_dict.keys():
            m_dict[score].append(name)
        else:
            m_dict[score] = [name]

    for name in sorted(m_dict[sorted(list(set(m_dict.keys())))[1]]):
        print(name)
