""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show table",
                "Add item",
                "Remove item",
                "Update item",
                "Get oldest person",
                "Get persons closest to average"]

    ui.print_menu("HR menu", options, "Exit to main menu")    

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('hr/persons.csv')

    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = input("Add an ID: ")
        remove(table, id_)
    elif option == "4":
        id_ = input("Add an ID: ")
        update(table, id_)
    elif option == "5":
        get_oldest_person()
    elif option == "6":
        get_persons_closest_to_average()
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["id", "name", "birth_year"]
    ui.print_table(table, title_list)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_line = ["", "", ""]
    new_line[0] = common.generate_random(table) 
    actor = ui.get_inputs(["What's the name of main actor/actress? "], "")
    year = ui.get_inputs(["When was the film made? "], "")
    new_line[1] = actor[0]
    new_line[2] = year[0]
    table.append(new_line)
    data_manager.write_table_to_file("hr/persons.csv", table)

    return table



def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
 
    for line in table:
        if line[0] == id_:
            table.remove(line)
            data_manager.write_table_to_file("hr/persons.csv", table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    for line in table:
        if line[0] == id_:
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"name\"/\"birth year\"): "], "")
            if item_to_be_changed[0] == "name":
                name = ui.get_inputs(["What is the new name: "], "")
                line[1] = name[0]
            if item_to_be_changed[0] == "birth year":
                year = ui.get_inputs(["What is the new birth year: "], "")
                line[2] = year[0]
            
            data_manager.write_table_to_file("hr/persons.csv", table)    

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
