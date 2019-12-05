""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
               "Get longest name id",
               "Get subscribed emails"]

    ui.print_menu("CRM menu", options, "Exit to main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")

    table = data_manager.get_table_from_file('crm/customers.csv')

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
        get_longest_name_id()
    elif option == "6":
        get_subscribed_emails()
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

    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    
    new_line = ["", "", "", ""]
    new_line[0] = common.generate_random(table) 
    name = ui.get_inputs(["What is the name?: "], "") 
    email = ui.get_inputs(["What is the email adress?: "], "")
    subscribed = ui.get_inputs(["When it was subscribed?: "], "")
    new_line[1] = name[0]
    new_line[2] = email[0]
    new_line[3] = subscribed[0]
    table.append(new_line)
    data_manager.write_table_to_file('crm/customers.csv', table)

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
            data_manager.write_table_to_file("crm/customers.csv", table)

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
            item_to_be_changed = ui.get_inputs(["What do you want to update (\"name\"/\"email\"/\"subscribed\"): "], "")
            if item_to_be_changed[0] == "name":
                name = ui.get_inputs(["What is the new name: "], "")
                line[1] = name[0]
            elif item_to_be_changed[0] == "email":
                email = ui.get_inputs(["What is the new email: "], "")
                line[2] = email[0]
            elif item_to_be_changed[0] == "subscribed":
                subscribed = ui.get_inputs(["Who is the new subscriber: "], "")
                line[3] = subscribed[0]

            data_manager.write_table_to_file("crm/customers.csv", table)    

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
