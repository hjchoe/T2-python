# create/open a text file using: var = open("filename.txt", "type")
# there are many types, but the basics are:
#      r: open and ONLY read the file
#      w: creates a new file or overwrites an existing file (if same name) to ONLY write
#      w+: open a file to read and write
#      a: open a file to append to an existing file (starts at the end)
#      a+: open a file to append and read
f = open("statescapitals.txt", "w")

# prompt + directions for the user on how to input
print("\nEnter States and Capitals. When finished enter: done")

# while loop set to run forever until broken using: break
while True:
    # input for state
    state = input("\nEnter State:\n")

    # checking if user entered done to finish entering states and capitals
    if state == "done":
        # break: to break the while loop if user entered: done
        break

    # input for capital
    capital = input("\nEnter Capital:\n")

    # use var.write(stuff) to write into the txt file opened earlier (use same var)
    #       to move to the next line in the txt file use "\n"
    f.write(f"{state}:{capital}\n")
    # in order to facilitate reading the states and capitals later on, I used a symbol that otherwise wouldn't be in either
    # a state or capital's name ":" to separate the state and capital

f.close()