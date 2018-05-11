# shopping list proper
shopping_list = []

# output text formatting
def make_line(char='*', length=25):
    print(char*length)

def new_line(times=1):
    while times:
        print(' ')
        times -= 1

def get_longest_item_length(a_list):
    max_length = 0
    for item in a_list:
        if len(item) > max_length:
            max_length = len(item)
        else:
            continue
    return max_length

def print_commands():

    new_line(3)

    print("The list of commands:")
    print("::: ADD    ::: adds one item :::")
    print("::: ADD -M ::: adds multiple items :::")
    print("::: SHOW   ::: prints the current list state :::")
    print("::: QUIT   ::: quits app :::")

def accept_command():

    new_line(3)

    current_command = input('::: Your Command     ::: ').upper()

    if current_command == 'QUIT':
        output = quit_app()
    elif current_command == 'ADD':
        output = add('single')
    elif current_command == 'ADD -M':
        output = add('multiple')
    elif current_command == 'SHOW':
        output = show()
    else:
        output = invalid_command()

    return output

def quit_app():
    return False

def add(argument):
    if argument == 'single':
        add_item()
        return True
    elif argument == 'multiple':
        repeat = True
        while repeat:
            repeat = add_item()
        return True

def show():
    print_list()
    return True

def invalid_command():
    print('There\'s no such command! Please, read instructions above this label.')
    return True

def add_item():
    new_item = input('Enter an item or a to-do option below (or type \'DONE\' to return to main menu):\n')
    if new_item.upper() == 'DONE':
        return False
    shopping_list.append(new_item)
    if new_item in shopping_list:
        print('Item successfully added! There are {} item(s) in your list now.\n'.format(len(shopping_list)))
        return True

def print_list():
    # visual separation of content
    new_line(3)
    # warning message
    warning_message = '--- There are no items in your list ---'
    # list header
    header_message = 'Here is your to-do list'

    # number of characters in list max position
    ## e.g. 333 returns 3 while 1000 returns 4, etc.
    max_char = len(str(len(shopping_list)))

    # visual separator of items, inbetweener
    separator = ' ::: '

    # printing header
    print(header_message)

    if shopping_list == []:
        # empty list case
        make_line(length = len(warning_message))
        print(warning_message)
        make_line(length = len(warning_message))
    else:
        # top and bottom separator calculations
        def_line = len(header_message)
        max_line = get_longest_item_length(shopping_list)
        max_combo = max_line + max_char + len(separator)
        if max_combo > def_line:
            def_line = max_combo
        # printing out line
        make_line(length = def_line)
        for item in shopping_list:
            ordinar = shopping_list.index(item) + 1
            ordinar_length = len(str(ordinar))
            offset_length = max_char - ordinar_length
            offset = ' ' * offset_length

            print('{}{}{}{}'.format(offset, ordinar, separator, item))
        make_line(length = def_line)

# program flow
make_line()
print('*** Shopping List App ***')
print('* by Alexei Parphyonov **')
make_line()

print_commands()
do_continue = accept_command()
while do_continue:
    print_commands()
    do_continue = accept_command()

print_list()
new_line(3)
