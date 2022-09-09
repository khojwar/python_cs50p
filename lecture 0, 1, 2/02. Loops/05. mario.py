'''
# print column
def main():
    print_column(3)



# def print_column(height):
#     for _ in range(height):
#         print("#")

def print_column(height):
    print("#\n" * height, end="")


main()

'''



#print row
def main():
    print_row(4)



def print_row(width):
    print("?" * width)


main()