import app.database as db

def add_participant(name):
    """
    Add a new participant to the database.
    
    Args:
        name (str): The name of the participant to add.
    """
    database = db.get_db()
    cursor = database.cursor()
    cursor.execute("INSERT INTO participants (name) VALUES (?)", (name,))
    database.commit()
    cursor.close()
    
def get_all_participants():
    """
    Retrieve all participants from the database.
    """
    database = db.get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM participants")
    participants = cursor.fetchall()
    cursor.close()
    return participants