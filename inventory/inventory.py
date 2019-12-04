""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
               "Get available items",
               "Get average durability by manufacturers"]

    ui.print_menu("Inventory menu", options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('inventory/inventory.csv')

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
        get_available_items()
    elif option == "6":
        get_average_durability_by_manufacturers()
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

    title_list = ["id", "name", "manufacturer", "purchase_year", "durability"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_line = ["", "", "", "", ""]
    new_line[0] = common.generate_random(table) 
    name = ui.get_inputs(["What's the name of the game? "], "") 
    manufacturer = ui.get_inputs(["Who is the manufacturer? "], "")
    year = ui.get_inputs(["When was it bought? Year of transaction: "], "")
    durability = ui.get_inputs(["How many years is it still durable? "], "")
    new_line[1] = name[0]
    new_line[2] = manufacturer[0]
    new_line[3] = year[0]
    new_line[4] = durability[0]
    table.append(new_line)
    data_manager.write_table_to_file('inventory/inventory.csv', table)

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
            data_manager.write_table_to_file("inventory/inventory.csv", table)

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
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"name\"/\"manufacturer\"/\"purchase_year\"/\"durability\"): "], "")
            if item_to_be_changed[0] == "name":
                name = ui.get_inputs(["What is the new name: "], "")
                line[1] = name[0]
            elif item_to_be_changed[0] == "manufacturer":
                manufacturer = ui.get_inputs(["Who is the \"new\" manufacturer: "], "")
                line[2] = manufacturer[0]
            elif item_to_be_changed[0] == "purchase_year":
                year_of_purchase = ui.get_inputs(["What is the \"new\" year of purchase: "], "")
                line[3] = year_of_purchase[0]
            elif item_to_be_changed[0] == "durability":
                durability = ui.get_inputs(["What is the new durability (in years): "], "")
                line[4] = durability[0]
            
            data_manager.write_table_to_file("inventory/inventory.csv", table)    

    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
