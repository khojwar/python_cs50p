

'''
def main():
    print_square(3)


def print_square(size):
    # for each row in square
    for i in range(size):

        # for each brickk in row
        for j in range(size):
            # print brick
            print("#", end="")
        print()


main()

'''



'''
# alternative and short method
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * size)


main()

'''


# Alternative
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)

main()





