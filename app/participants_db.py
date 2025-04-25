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

def delete_all_participants():
    """
    Delete all participants from the database.
    """
    database = db.get_db()
    cursor = database.cursor()
    cursor.execute("DELETE FROM participants")
    database.commit()
    cursor.close()
    
def delete_participant(participant_id):
    """
    Delete a participant from the database by their ID.
    
    Args:
        participant_id (int): The ID of the participant to delete.
    """
    database = db.get_db()
    cursor = database.cursor()
    cursor.execute("DELETE FROM participants WHERE id = ?", (participant_id,))
    database.commit()
    cursor.close()