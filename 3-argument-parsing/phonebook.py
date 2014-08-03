import sys


def create_phonebook(phonebook_name):
    """Create a new phonebook.

    Args:
        phonebook_name (str): the name of the phonebook to create
    """
    pass


def add_entry(name, number, phonebook_name):
    """Add a new name and number to the given phonebook.

    Args:
        name (str): name of the entry to add
        number (str): phone number of the entry to add
        phonebook_name (str): name of the phonebook
    """
    pass


def update_entry(name, new_number, phonebook_name):
    """Update an entry with the given name in the given phonebook
    with the new phone bumber.

    Args:
        name (str): name of the entry to update
        new_number (str): new phone number of the entry
        phonebook_name (str): name of the phonebook
    """
    pass


def remove_entry(name, phonebook_name):
    """Remove an entry with the given name in the given phonebook.

    Args:
        name (str): name of the entry to delete
        phonebook_name (str): name of the phonebook
    """
    pass


def lookup_name(name, phonebook_name):
    """Look up an entry by name in the given phonebook.

    Args:
        name (str): name to look up
        phonebook_name (str): name of the phonebook
    """
    pass


def lookup_number(number, phonebook_name):
    """Look up an entry by number in the given phonebook.

    Args:
        number (str): phone number to look up
        phonebook_name (str): name of the phonebook
    """
    pass


if __name__ == '__main__':
    args = sys.argv[:]
    script = args.pop(0)    # name of script is first arg
    command = args.pop(0)   # the next arg will be the main command

    if command == 'create':
        phonebook_name = args.pop(0)
        create_phonebook(phonebook_name)

    elif command == 'add':
        name, number, phonebook_name = args
        add_entry(name, number, phonebook_name)

    elif command == 'update':
        name, new_number, phonebook_name = args
        update_entry(name, new_number, phonebook_name)

    elif command == 'remove':
        name, phonebook_name = args
        remove_entry(name, phonebook_name)

    elif command == 'lookup':
        name, phonebook_name = args
        lookup_name(name, phonebook_name)

    elif command == 'reverse-lookup':
        phonebook_name, phonebook_name = args
        lookup_number(number, phonebook_name)