# 1
values = [1, 2, 3, 4, 5, "hello", 6, 7, 8, 9, "10"]
for cur in values:
    print("The value is :", values[cur])
    if type(values[cur]) == str:
        raise ValueError("This is a string!")

# 3
filename = input("Enter filename: ")
try:
    infile = open(filename, "r")
    try:
        line = infile.readline()
        value = int(line)
    finally:
        infile.close()
except IOError as exception:
    print("Error:", str(exception))
except ValueError as exception:
    print("Error:", str(exception))
