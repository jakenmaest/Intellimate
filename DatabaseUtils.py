import sqlite3
import os
import json
from typing import Dict, List, Any, Tuple, Union

class DatabaseUtils:
    def __init__(self, db_name: str = "IntelliMateClient.db") -> None:
        self.db_name: str = db_name
        self.conn: sqlite3.Connection = sqlite3.connect(self.db_name)
        self.cursor: sqlite3.Cursor = self.conn.cursor()

    def create_database(self) -> None:
        # Create Users Table
        self.cursor.execute("""
            CREATE TABLE Users (
                user_id TEXT PRIMARY KEY,
                username TEXT,
                password TEXT,
                status TEXT,
                last_login TEXT,
                last_updated TEXT,
                active_conversations TEXT,
                usage_stats TEXT,
                preferences TEXT,
                tags TEXT,
                version TEXT,
                custom_settings TEXT
            );
        """)

        # Create Assistants Table
        self.cursor.execute("""
            CREATE TABLE Assistants (
                assistant_id TEXT PRIMARY KEY,
                assistant_name TEXT,
                assistant_model TEXT,
                persona TEXT,
                likes TEXT,
                dislikes TEXT,
                relationship TEXT,
                expertise TEXT,
                status TEXT,
                tags TEXT,
                last_active TEXT,
                active_conversations TEXT,
                language TEXT,
                version TEXT,
                custom_settings TEXT
            );
        """)

        # Create Conversations Table
        self.cursor.execute("""
            CREATE TABLE Conversations (
                conversation_id TEXT PRIMARY KEY,
                messages TEXT,
                info TEXT
            );
        """)

        # Commit changes and close connection
        self.conn.commit()
        self.conn.close()
        print("Database and tables created successfully.")
    def create_user(self, user_data: Dict[str, Any]) -> None:
        sql = """
            INSERT INTO Users (user_id, username, password, status, last_login, last_updated,
                               active_conversations, usage_stats, preferences, tags, version, custom_settings)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (
            user_data['user_id'], user_data['username'], user_data['password'], user_data['status'],
            user_data['last_login'], user_data['last_updated'], json.dumps(user_data['active_conversations']),
            json.dumps(user_data['usage_stats']), json.dumps(user_data['preferences']), json.dumps(user_data['tags']),
            user_data['version'], json.dumps(user_data['custom_settings'])
        ))
        self.conn.commit()

    def update_user(self, user_id: str, updates: List[Tuple[str, Any]]) -> None:
        sql = "SELECT * FROM Users WHERE user_id = ?"
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def delete_user(self, user_id: str) -> None:
        sql = "DELETE FROM Users WHERE user_id = ?"
        self.cursor.execute(sql, (user_id,))
        self.conn.commit()

    def create_conversation(self, conversation_data: Dict[str, Any]) -> None:
        sql = """
            INSERT INTO Conversations (conversation_id, messages, info)
            VALUES (?, ?, ?)
        """
        self.cursor.execute(sql, (
            conversation_data['conversation_id'],
            json.dumps(conversation_data['messages']),
            json.dumps(conversation_data['info'])
        ))
        self.conn.commit()

    def read_conversation(self, conversation_id: str) -> Tuple[Any, ...]:
        sql = "SELECT * FROM Conversations WHERE conversation_id = ?"
        self.cursor.execute(sql, (conversation_id,))
        return self.cursor.fetchone()

    def update_conversation(self, conversation_id: str, updates: List[Tuple[str, Any]]) -> None:
        for field, value in updates:
            sql = f"UPDATE Conversations SET {field} = ? WHERE conversation_id = ?"
            self.cursor.execute(sql, (json.dumps(value) if isinstance(value, (list, dict)) else value, conversation_id))
        self.conn.commit()

    def delete_conversation(self, conversation_id: str) -> None:
        sql = "DELETE FROM Conversations WHERE conversation_id = ?"
        self.cursor.execute(sql, (conversation_id,))
        self.conn.commit()

    def create_assistant(self, assistant_data: Dict[str, Any]) -> None:
        sql = """
            INSERT INTO Assistants (assistant_id, assistant_name, assistant_model, persona,
                                    likes, dislikes, relationship, expertise, status, tags,
                                    last_active, active_conversations, language, version, custom_settings)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (
            assistant_data['assistant_id'], assistant_data['assistant_name'], assistant_data['assistant_model'],
            assistant_data['persona'], json.dumps(assistant_data['likes']), json.dumps(assistant_data['dislikes']),
            assistant_data['relationship'], json.dumps(assistant_data['expertise']), assistant_data['status'],
            json.dumps(assistant_data['tags']), assistant_data['last_active'], json.dumps(assistant_data['active_conversations']),
            assistant_data['language'], assistant_data['version'], json.dumps(assistant_data['custom_settings'])
        ))
        self.conn.commit()

    def read_assistant(self, assistant_id: str) -> Tuple[Any, ...]:
        sql = "SELECT * FROM Assistants WHERE assistant_id = ?"
        self.cursor.execute(sql, (assistant_id,))
        return self.cursor.fetchone()

    def update_assistant(self, assistant_id: str, updates: List[Tuple[str, Any]]) -> None:
        for field, value in updates:
            sql = f"UPDATE Assistants SET {field} = ? WHERE assistant_id = ?"
            self.cursor.execute(sql, (json.dumps(value) if isinstance(value, (list, dict)) else value, assistant_id))
        self.conn.commit()

    def delete_assistant(self, assistant_id: str) -> None:
        sql = "DELETE FROM Assistants WHERE assistant_id = ?"
        self.cursor.execute(sql, (assistant_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
