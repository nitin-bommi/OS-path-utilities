# Operations on Files.

# Opening a textfile and writing data or replacing the content in that textfile.
f = open("textfile.txt", "w+")
f.write("Hey...\r\nThis is a text-file.\r\n")
# closing the file after used.
f.close()

# appending text to the textfile.
f = open("textfile.txt", "a")
f.write("I have already told you that this is a textfile.")
f.close()

# reading the data in a textfile.
f = open("textfile.txt", "r")
f.read()
