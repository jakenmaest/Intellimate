# Import necessary modules and classes
from typing import List
from Assistant import Assistant
from User import User
from DatabaseUtils import DatabaseUtils
from Conversation import Conversation

#  TODO: Fill in the rest this 'data' object, it must contain
#  everything in the session, plus an internal info object

## An example of IntelliMateClient data object here
## It includes all data in the current session, along with
## and internal info object with session level data in it

data = {
    'info' : {
        'name': 'default',
        'filename': 'Default.db',
        'filepath': './'
    },
    'users': {}, # All user data in session database
    'assistants': {}, # All Assistants in user database
    'conversations': {}, # 
}

# This is the class for all of the Client management
class IntelliMateClient:

    def __init__(self): pass
        # Choose a session to load, or create a new one

    ## Session (database) management
    def list_sessions(self) -> List[str]: pass
        # List sessions(databases) in session path

    def new_session(self, sessionName: str): pass
        # Create new session database DatabaseUtils called 'sessionName.db'
        # close current session (with saving option) and load the newly created one 
    
    def load_session(self, sessionName: str): pass
        # Create new session database

    def close_session(self): pass
        # Logic to close current database

    ## Login management
    def login(self, user_id: str): pass
        # User login logic

    def logout(self, user_id: str): pass
        # User login logic

    def select_assistant(self): pass
        # Assistant selection logic

    def start_conversation(self): pass
        # Start a new conversation

    def manage_conversation(self): pass
        # Manage ongoing conversation

    def end_conversation(self): pass
        # End the conversation

    def update_preferences(self): pass
        # Update user and assistant preferences

    def show_stats(self): pass
        # Show usage statistics

    def main_loop(self): pass
        # Main loop for user interaction
