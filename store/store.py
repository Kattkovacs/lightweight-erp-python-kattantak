""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
               "Get counts by manufacturers",
               "Get average by manufacturer"]

    ui.print_menu("Store menu", options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('store/games.csv')

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
        get_counts_by_manufacturers()
    elif option == "6":
        get_average_by_manufacturer()
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

    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
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
    title = ui.get_inputs(["What is the title?: "], "") 
    manufacturer = ui.get_inputs(["What is the manufacturer adress?: "], "")
    price = ui.get_inputs(["What is the price?: "], "")
    in_stock = ui.get_inputs(["How much is in stock?: "], "")
    new_line[1] = title[0]
    new_line[2] = manufacturer[0]
    new_line[3] = price[0]
    new_line[4] = in_stock[0]
    table.append(new_line)
    data_manager.write_table_to_file('store/games.csv', table)


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
            data_manager.write_table_to_file("store/games.csv", table)


    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    for line in table:
        if line[0] == id_:
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"title\"/\"manufacturer\"/\"price\"): "], "")
            if item_to_be_changed[0] == "title":
                title = ui.get_inputs(["What is the new title: "], "")
                line[1] = title[0]
            elif item_to_be_changed[0] == "manufacturer":
                manufacturer = ui.get_inputs(["What is the new manufacturer: "], "")
                line[2] = manufacturer[0]
            elif item_to_be_changed[0] == "price":
                price = ui.get_inputs(["What is the new price: "], "")
                line[3] = price[0]
            elif item_to_be_changed[0] == "in_stock":
                in_stock = ui.get_inputs(["How much is in stock: "], "")
                line[3] = in_stock[0]

            data_manager.write_table_to_file("store/games.csv", table)    

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): title of manufacturer

    Returns:
         number
    """

    # your code
