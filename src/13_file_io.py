"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open
# "foo.txt"

# YOUR CODE HERE

with open('src/foo.txt') as f:
    read_data = f.read()
    print(read_data)

print(f"Verification that that file is closed: {f.closed}")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new_file = open('src/bar.txt', 'w')

new_file.write("Hello from the frozen north\n")
new_file.write("I come in peace\n")
new_file.write("Remind me why I live here?\n")


new_file.close()


def read_file(filepath):
    """ Opens a file for reading """
    with open(filepath) as file:
        read_data = file.read()
        print(read_data)

read_file('src/bar.txt')
