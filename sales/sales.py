""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
               "Get lowest price item id",
               "Get items sold between"]

    ui.print_menu("Sales menu", options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('sales/sales.csv')

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
        get_lowest_price_item_id()
    elif option == "6":
        get_items_sold_between()
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

    title_list = ["id", "title", "price", "month", "day", "year"]
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
    title = ui.get_inputs(["What's the title of the game? "], "")
    price = ui.get_inputs(["What's the actual sale price of the game? "], "")
    month = ui.get_inputs(["When was it sold? Month of transaction: "], "")
    day = ui.get_inputs(["When was it sold? Day of transaction: "], "")
    year = ui.get_inputs(["When was it sold? Year of transaction: "], "")
    new_line[1] = title[0]
    new_line[2] = price[0]
    new_line[3] = month[0]
    new_line[4] = day[0]
    new_line[5] = year[0]
    table.append(new_line)
    data_manager.write_table_to_file('sales/sales.csv', table)


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
            data_manager.write_table_to_file("sales/sales.csv", table)

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
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"title\"/\"price\"/\"month\"/\"day\"/\"year\"): "], "")
            if item_to_be_changed[0] == "title":
                title = ui.get_inputs(["What is the new title: "], "")
                line[1] = title[0]
            elif item_to_be_changed[0] == "price":
                price = ui.get_inputs(["What is the new price: "], "")
                line[2] = price[0]
            elif item_to_be_changed[0] == "month":
                month = ui.get_inputs(["What is the new month: "], "")
                line[3] = month[0]
            elif item_to_be_changed[0] == "day":
                day = ui.get_inputs(["What is the new day: "], "")
                line[4] = day[0]
            elif item_to_be_changed[0] == "year":
                year = ui.get_inputs(["What is the new year: "], "")
                line[5] = year[0]

            data_manager.write_table_to_file("sales/sales.csv", table)    

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
