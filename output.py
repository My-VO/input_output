my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

my_file = open("output.txt", "r+") # "r+" : read & write
print (my_file.read())
my_file.close()

## Reading Between the Lines
my_file = open("output.txt", "r")

print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()

## Buffering Data
# During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()


# Try to read from the file
print (read_file.read())
read_file.close()

# The "with" and "as" Keywords
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

with open("text.txt", "w") as my_file:
  my_file.write("Here is with ... as")

# Check file closed
if my_file.closed != True:
  my_file.close()
print (my_file.closed)