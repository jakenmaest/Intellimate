## User class
import json

class User:
    def __init__(self, user_id, username, password, language, version):
        self.data = {
            "user_id": user_id,
            "username": username,
            "password": password,  # In a real-world application, this should be hashed
            "status": "active",
            "last_login": None,
            "last_updated": None,
            "active_conversations": [],
            "usage_stats": {
                "total_tokens": 0,
                "total_queries": 0,
                "credit_balance": 0.0
            },
            "preferences": {
                "language": language,
                "notifications": "on"
            },
            "tags": [],
            "version": version,
            "custom_settings": {}
        }

    def login(self):
        # Update the last_login timestamp and set status to active
        # Placeholder for actual timestamp
        self.data["last_login"] = "current_timestamp"
        self.data["status"] = "active"

    def logout(self):
        # Update the status to inactive
        self.data["status"] = "inactive"

    def update_password(self, new_password):
        # Update the password
        self.data["password"] = new_password  # Again, this should be hashed in a real-world application

    def update_preferences(self, language, notifications):
        # Update user preferences
        self.data["preferences"]["language"] = language
        self.data["preferences"]["notifications"] = notifications

    def get_usage_stats(self):
        # Return the usage_stats dictionary
        return self.data["usage_stats"]

    def add_conversation(self, convo_id):
        # Add a conversation ID to the list of active conversations
        self.data["active_conversations"].append(convo_id)

    def remove_conversation(self, convo_id):
        # Remove a conversation ID from the list of active conversations
        self.data["active_conversations"].remove(convo_id)

    def to_json(self):
        # Serialize the data object to a JSON-formatted string
        return json.dumps(self.data)

    def from_json(self, json_str):
        # Deserialize a JSON-formatted string to populate the data object
        self.data = json.loads(json_str)
