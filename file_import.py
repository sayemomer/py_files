file = open('demo.txt', mode = 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()


# Check whether file is closed
print(file.closed)



##import file by line

# Read & print the first 3 lines
with open('demo.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
