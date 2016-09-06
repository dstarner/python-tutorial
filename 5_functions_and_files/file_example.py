def file_write(file_name):
    with open(file_name, "w+") as file:

        print("Writing 'Hello World' to file...")

        # TRY WRITING TO A FILE BELOW HERE

        # Write to the file
        file.write("Hello World!")


def file_read(file_name):

    with open(file_name, "r+") as file:

        print("Reading to file...")

        # TRY READING FROM A FILE BELOW HERE

        # Read all lines from the file
        for line in file.readlines():
            print(line)


def file_example(file):  # The file_example function definition which gets passed a parameter 'file'

    file_write(file)  # Calling the 'file_write' function, passing the 'file' variable to it
    file_read(file)   # Calling the 'file_read' function, passing the 'file' variable to it


if __name__ == '__main__':

    file = "myfile.txt"  # Create a variable to hold file name
    file_example(file)   # Calling the 'file_example' function, passing the 'file' variable to it
