from sys import argv

arguments = argv[1:]
print(arguments)
len_arg = len(arguments)
if 'help' in arguments:
    if len_arg == 0:
        exit()
    elif len_arg == 1:
        if arguments[0] == 'help':
            print('Commands:\n- help -\n- division -\n- cadet -\n- officer -')
    elif len_arg == 2:
        if arguments[0] == 'division' and arguments[1] == 'help':
            print('Division module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
        elif arguments[0] == 'cadet' and arguments[1] == 'help':
            print('Cadet module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
        elif arguments[0] == 'officer' and arguments[1] == 'help':
            print('Officer module commands:\n- help -\n- list -\n- add -\n- edit -\n- delete -')
    elif len_arg == 3:
        if arguments[0] == 'division' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Division list command has no parameters')
        elif arguments[0] == 'division' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Division add command parameters:\n-n : division name, required')
        elif arguments[0] == 'division' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Division edit command parameters:\n-i : Division ID, required\n-n : Name, required')
        elif arguments[0] == 'division' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Division delete command parameters:\n-i : Division ID\n-a : Delete all divisions')
        elif arguments[0] == 'cadet' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Cadet list command parameters:\n-i : ID\n-l : last name\n-d : division ID\n-r : rank\n-o : division officer I\n-s : sorting, possible id, lastName\n-p : properties view, combination of i - id, r - rank, f - firstName, m - middleName, l - lastName, b – birthdate')
        elif arguments[0] == 'cadet' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Cadet add command parameters:\n-f : first name, required\n-m : middle name, required\n-l : last name, required\n-b : birth date, required, format yyyy-MM-dd\n-r : rank, required\n-d : division ID, required')
        elif arguments[0] == 'cadet' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Cadet edit command parameters:\n-i : ID, required\n-f : first name\n-m : middle name\n-l : last name\n-b : birth date, format yyyy-MM-dd\n-r : rank\n-d : division ID')
        elif arguments[0] == 'cadet' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Cadet delete command parameters:\n-i : ID\n-d : division ID\n-o : division officer ID\n-a : delete all cadets')
        elif arguments[0] == 'officer' and arguments[1] == 'list' and arguments[2] == 'help':
            print('Officer list command parameters:\n-i : ID\n-l : last name\n-d : division ID\n-r : rank\n-c : cadet ID\n-s : sorting, possible id, lastName\n-p : properties view, combination of i - id, r - rank, f - firstName, m - middleName, l - lastName, b – birthdate')
        elif arguments[0] == 'officer' and arguments[1] == 'add' and arguments[2] == 'help':
            print('Officer add command parameters:\n-f : first name, required\n-m : middle name, required\n-l : last name, required\n-b : birth date, required, format yyyy-MM-dd\n-r : rank, required\n-d : division ID')
        elif arguments[0] == 'officer' and arguments[1] == 'edit' and arguments[2] == 'help':
            print('Officer edit command parameters:\n-i : ID, required\n-f : first name\n-m : middle name\n-l : last name\n-b : birth date, format yyyy-MM-dd\n-r : rank\n-d : division ID')
        elif arguments[0] == 'officer' and arguments[1] == 'delete' and arguments[2] == 'help':
            print('Officer delete command parameters:\n-i : ID\n-a : delete all officers')
