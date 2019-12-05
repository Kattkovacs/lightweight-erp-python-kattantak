""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
               "Which year max",
               "Avg_amount"]

    ui.print_menu("Accounting menu", options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('accounting/items.csv')

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
        which_year_max()
    elif option == "6":
        avg_amount()
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

    title_list = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_line = ["", "", "", "", "", ""]
    new_line[0] = common.generate_random(table) 
    month = ui.get_inputs(["When was it bought? Month of transaction: "], "") 
    day = ui.get_inputs(["When was it bought? Day of transaction: "], "")
    year = ui.get_inputs(["When was it bought? Year of transaction: "], "")
    in_out = ui.get_inputs(["Was it input or outflaw? (\"in\"/\"out\") "], "")
    amount = ui.get_inputs(["Amount of transaction: "], "")
    new_line[1] = month[0]
    new_line[2] = day[0]
    new_line[3] = year[0]
    new_line[4] = in_out[0]
    new_line[5] = amount[0]
    table.append(new_line)
    data_manager.write_table_to_file('accounting/items.csv', table)

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
            data_manager.write_table_to_file("accounting/items.csv", table)

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
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"month\"/\"day\"/\"year\"/\"type\"/\"amount\"): "], "")
            if item_to_be_changed[0] == "month":
                month = ui.get_inputs(["What is the new month of transaction: "], "")
                line[1] = month[0]
            elif item_to_be_changed[0] == "day":
                day= ui.get_inputs(["What is the new day of transaction: "], "")
                line[2] = day[0]
            elif item_to_be_changed[0] == "year":
                year = ui.get_inputs(["What is the new year of transaction: "], "")
                line[3] = year[0]
            elif item_to_be_changed[0] == "type":
                if line[4] == "in":
                    line[4] = "out"
                elif line[4] == "out":
                    line[4] = "in"
            elif item_to_be_changed[0] == "amount":
                amount = ui.get_inputs(["What is the new amount: "], "")
                line[5] = amount[0]

            data_manager.write_table_to_file("accounting/items.csv", table)    

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
