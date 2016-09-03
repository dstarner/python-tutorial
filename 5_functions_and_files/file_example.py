def file_write(file_name):
    with open(file_name, "w") as file:

        print("Writing 'Hello World' to file...")

        # Write to the file
        file.write("Hello World!")


def file_read(file_name):

    with open(file_name, "r") as file:

        print("Reading to file...")

        # Read all lines from the file
        for line in file.readlines():
            print(line)


def file_example(file):

    file_write(file)

    file_read(file)


if __name__ == '__main__':
    file = "myfile.txt"
    file_example(file)
