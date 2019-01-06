def main():
    """
        主函数
    """
    a = ('a', 'b', 'c')
    b = (1, 2, 3)

    x = zip(a, b)
    print(list(x))

    x = zip(a, b)
    print(dict(x))


    c = zip(*zip(a, b))
    print(list(c))

    a1, a2 = zip(*zip(a, b))
    print(tuple(a1))
    print(tuple(a2))


if __name__ == '__main__':
    main()