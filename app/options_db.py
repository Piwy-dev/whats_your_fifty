import app.database as database

def add_option(option_name):
    """
    Add a new option to the database.
    
    Args:
        option_name (str): The name of the option to add.
    """
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO options (name) VALUES (?)", (option_name,))
    db.commit()
    cursor.close()
    
def get_all_options():
    """
    Retrieve all options from the database.
    """
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM options")
    options = cursor.fetchall()
    cursor.close()
    return options

def delete_all_options():
    """
    Delete all options from the database.
    """
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM options")
    db.commit()
    cursor.close()
    
def delete_option(option_id):
    """
    Delete an option from the database by its ID.
    
    Args:
        option_id (int): The ID of the option to delete.
    """
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM options WHERE id = ?", (option_id,))
    db.commit()
    cursor.close()