
# Creates our Checklist
checklist = []

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[int(index)] = str(item)

def destroy (index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[int(index)] = "{}{}".format("√", checklist[int(index)])
    # update(index, "{}{}".format("√", checklist[index])

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
    user_value = user_input("Please Enter a value:")
    print(user_value)

def select(function_code):
    # Create item
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)

        # Read item
    elif function_code == "R":
        # remove from list
        item_index = user_input("Index number?: ")
        destroy(item_index)

    elif function_code == "U":
        # update item

        item_index = user_input("Index number?: ")
        input_item = user_input("Input Item: ")
        update(item_index, input_item)



    elif function_code == "C":
        # Mark as complete
        item_index = user_input("Which index number did you want to check off?: ")
        mark_completed(item_index)
    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return false

    else:
        # Catch all
        print("Unknown Option")
    return True

# def test():
#     create("purple sox")
#     create("red cloak")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple socks")
#     destroy(1)
#
#     print(read(0))
#
#
# # Run Tests
# test()

running = True
while running:
    selection = user_input(
        "Press A to add to list, R to Remove from list, U to update item, C to mark as complete, and P to show list. Press Q to Exit ")
    running = select(selection)
