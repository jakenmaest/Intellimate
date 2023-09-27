

### The App Overview

Our application aims to be a comprehensive client for interacting with OpenAI's API, specifically designed to manage multiple users, assistants, and conversations. It will offer a range of functionalities, from executing queries to monitoring usage stats and managing preferences.

### The Classes

1. **`Conversation`**: Manages individual conversations, keeping track of messages, timestamps, token counts, and other metadata. It's the go-to class for anything related to a single conversation thread.

2. **`Assistant`**: Manages individual assistant profiles, including their persona, likes, dislikes, expertise, and more. This class will be used to personalize the assistant's behavior and responses.

3. **`User`**: Manages user profiles and settings, including account info, usage stats, and preferences. This class will be the backbone for personalized interactions and account management.

### Future Developments

1. **`Profile` Class**: If we decide to allow multiple profiles per user, this class could manage those.

2. **`Notification` Class**: To manage notifications, alerts, or messages to the user.

3. **`Billing` Class**: If a financial aspect is added, this could manage transactions, invoices, etc.

4. **`Client` Class**: The grand orchestrator that will tie all the other classes together. It will handle user management, assistant management, conversation management, data persistence, query execution, and possibly notification handling.

5. **Data Persistence**: We'll need to implement methods to save and load the entire state of the application.

6. **Advanced Features**: Things like language translation, bulk queries, and an interactive mode could be added later.

7. **UI/UX**: Eventually, we might want to develop a user interface for a more interactive experience.

# Conversation Class Documentation

## Overview

The `Conversation` class is designed to manage individual conversations in an application that interacts with OpenAI's API. It keeps track of messages, timestamps, token counts, and other metadata related to a single conversation thread.

---

## Data Object

The `data` object within the `Conversation` class holds all the relevant information for a single conversation. It is structured as a JSON-compatible dictionary with the following keys:

- **`messages`**: A list of dictionaries, each representing a message in the conversation.
  - `role`: The role of the message sender. Can be "system", "user", or "assistant".
  - `content`: The actual content of the message.
  - `timestamp`: The time the message was sent, in ISO 8601 format.
  - `model`: The model used for generating the message (relevant for the assistant role).
  - `token_count`: The number of tokens used in the message.
  - `message_id`: A unique identifier for the message.
  - `response_time`: The time taken by the assistant to generate the message.

- **`info`**: A dictionary for storing conversation-specific information.
  - `conversation_id`: A unique identifier for the conversation.
  - `start_time`: The time the conversation started, in ISO 8601 format.
  - `end_time`: The time the conversation ended, in ISO 8601 format (if applicable).
  - `status`: The current status of the conversation ("active", "inactive", "archived").

---

## Member Functions

### `__init__(self, conversation_id, start_time)`

Initializes a new `Conversation` object with a unique `conversation_id` and `start_time`.

### `add_message(self, role, content, model=None)`

Adds a new message to the `messages` list in the `data` object.

### `get_messages(self)`

Returns the list of all messages in the conversation.

### `get_last_message(self)`

Returns the most recent message in the conversation.

### `get_message_by_id(self, message_id)`

Returns a specific message by its unique `message_id`.

### `update_message(self, message_id, new_content)`

Updates the content of a message identified by its `message_id`.

### `delete_message(self, message_id)`

Deletes a message identified by its `message_id`.

### `end_conversation(self, end_time)`

Ends the conversation and sets its `status` to "inactive" or "archived".

### `get_info(self)`

Returns the `info` dictionary containing conversation-specific information.

### `to_json(self)`

Serializes the `data` object to a JSON-formatted string.

### `from_json(self, json_str)`

Deserializes a JSON-formatted string to populate the `data` object.

---

This documentation should provide a comprehensive understanding of the `Conversation` class and its functionalities. Feel free to add, remove, or modify any parts based on your specific needs.


# Assistant Class Documentation

## Overview

The `Assistant` class is designed to manage individual assistant profiles in an application that interacts with OpenAI's API. It keeps track of the assistant's persona, likes, dislikes, expertise, and other relevant metadata.

---

## Data Object

The `data` object within the `Assistant` class holds all the relevant information for a single assistant. It is structured as a JSON-compatible dictionary with the following keys:

- **`assistant_id`**: A unique identifier for the assistant.
- **`assistant_name`**: The name of the assistant.
- **`assistant_model`**: The OpenAI model used for generating responses (e.g., "gpt-3.5-turbo").
- **`persona`**: A string describing the assistant's persona (e.g., "helpful, witty").
- **`likes`**: A string of things the assistant likes (e.g., "python, pandas, music").
- **`dislikes`**: A string of things the assistant dislikes (e.g., "emacs, politics").
- **`relationship`**: A string describing the assistant's relationship with the user (e.g., "AI assistant/project partner").
- **`expertise`**: A list of areas where the assistant has expertise (e.g., ["data analytics", "research"]).
- **`status`**: The current status of the assistant ("active", "inactive").
- **`tags`**: A list of tags for categorizing the assistant (e.g., ["general"]).
- **`last_active`**: The last time the assistant was active, in ISO 8601 format.
- **`active_conversations`**: A list of active conversation IDs.
- **`language`**: The language in which the assistant communicates (e.g., "en").
- **`version`**: The version of the assistant.
- **`custom_settings`**: A dictionary for any custom settings or configurations.

---

## Member Functions

### `__init__(self, assistant_id, assistant_name, assistant_model, language, version)`

Initializes a new `Assistant` object with essential attributes.

### `activate(self)`

Activates the assistant and sets its status to "active".

### `deactivate(self)`

Deactivates the assistant and sets its status to "inactive".

### `update_name(self, new_name)`

Updates the assistant's name.

### `add_expertise(self, area)`

Adds a new area of expertise to the assistant's profile.

### `remove_expertise(self, area)`

Removes an area of expertise from the assistant's profile.

### `get_expertise(self)`

Returns the list of the assistant's areas of expertise.

### `join_conversation(self, convo_id)`

Adds a conversation ID to the assistant's list of active conversations.

### `leave_conversation(self, convo_id)`

Removes a conversation ID from the assistant's list of active conversations.

### `get_active_conversations(self)`

Returns the list of active conversations the assistant is part of.

### `to_json(self)`

Serializes the `data` object to a JSON-formatted string.

### `from_json(self, json_str)`

Deserializes a JSON-formatted string to populate the `data` object.

---

This documentation should provide a comprehensive understanding of the `Assistant` class and its functionalities.


# User Class Documentation

## Overview

The `User` class is designed to manage individual user profiles in an application that interacts with OpenAI's API. It keeps track of the user's account information, usage statistics, preferences, and other relevant metadata.

---

## Data Object

The `data` object within the `User` class holds all the relevant information for a single user. It is structured as a JSON-compatible dictionary with the following keys:

- **`user_id`**: A unique identifier for the user.
- **`username`**: The username of the user.
- **`password`**: The password for the user account (stored securely).
- **`status`**: The current status of the user ("active", "inactive").
- **`last_login`**: The last time the user logged in, in ISO 8601 format.
- **`last_updated`**: The last time the user's information was updated, in ISO 8601 format.
- **`active_conversations`**: A list of active conversation IDs.
- **`usage_stats`**: A dictionary containing usage statistics.
  - `total_tokens`: The total number of tokens used.
  - `total_queries`: The total number of queries made.
  - `credit_balance (USD)`: The remaining credit balance in USD.
- **`preferences`**: A dictionary containing user preferences.
  - `language`: Preferred language for interaction (e.g., "en").
  - `notifications`: Notification settings ("on" or "off").
- **`tags`**: A list of tags for categorizing the user (e.g., ["premium", "developer"]).
- **`version`**: The version of the user profile.
- **`custom_settings`**: A dictionary for any custom settings or configurations.

---

## Member Functions

### `__init__(self, user_id, username, password, language, version)`

Initializes a new `User` object with essential attributes.

### `login(self)`

Logs the user in and updates the `last_login` timestamp.

### `logout(self)`

Logs the user out and updates the `status` to "inactive".

### `update_password(self, new_password)`

Updates the user's password.

### `update_preferences(self, language, notifications)`

Updates the user's preferences.

### `get_usage_stats(self)`

Returns the `usage_stats` dictionary containing usage statistics.

### `add_conversation(self, convo_id)`

Adds a conversation ID to the user's list of active conversations.

### `remove_conversation(self, convo_id)`

Removes a conversation ID from the user's list of active conversations.

### `get_active_conversations(self)`

Returns the list of active conversations the user is part of.

### `to_json(self)`

Serializes the `data` object to a JSON-formatted string.

### `from_json(self, json_str)`

Deserializes a JSON-formatted string to populate the `data` object.

---

This documentation should provide a comprehensive understanding of the `User` class and its functionalities

# DatabaseUtils Class Documentation

## Overview

The `DatabaseUtils` class serves as an internal utility for handling database operations within the IntelliMateClient application. It provides CRUD (Create, Read, Update, Delete) functionalities for the `User`, `Assistant`, and `Conversation` tables in the SQLite database. This class ensures data persistence and integrity across sessions.

## Data Structure

### SQLite Tables

1. **Users Table**
    - `user_id`: Unique identifier for the user (Primary Key).
    - `username`: Username of the user.
    - `password`: Hashed password for secure login.
    - `status`: Account status (active/inactive).
    - `last_login`: Timestamp of the last login.
    - `last_updated`: Timestamp of the last update.
    - `active_conversations`: JSON-serialized list of active conversations.
    - `usage_stats`: JSON-serialized dictionary of usage statistics.
    - `preferences`: JSON-serialized dictionary of user preferences.
    - `tags`: JSON-serialized list of tags.
    - `version`: Version of the user profile.
    - `custom_settings`: JSON-serialized dictionary of custom settings.

2. **Assistants Table**
    - `assistant_id`: Unique identifier for the assistant (Primary Key).
    - `assistant_name`: Name of the assistant.
    - `assistant_model`: Model type (e.g., gpt-3.5-turbo).
    - `persona`: Persona description.
    - `likes`: JSON-serialized list of likes.
    - `dislikes`: JSON-serialized list of dislikes.
    - `relationship`: Relationship description.
    - `expertise`: JSON-serialized list of expertise areas.
    - `status`: Status (active/inactive).
    - `tags`: JSON-serialized list of tags.
    - `last_active`: Timestamp of the last activity.
    - `active_conversations`: JSON-serialized list of active conversations.
    - `language`: Preferred language.
    - `version`: Version of the assistant profile.
    - `custom_settings`: JSON-serialized dictionary of custom settings.

3. **Conversations Table**
    - `conversation_id`: Unique identifier for the conversation (Primary Key).
    - `messages`: JSON-serialized list of messages.
    - `info`: JSON-serialized dictionary of conversation metadata.

## Methods

### Initialization

- `__init__`: Initializes the SQLite database connection and cursor.

### CRUD Operations

- `create_user(user_data)`: Inserts a new user record into the Users table. Checks for unique primary key.
- `read_user(user_id)`: Retrieves a user record by user ID.
- `update_user(user_data)`: Updates an existing user record.
- `delete_user(user_id)`: Deletes a user record by user ID.

- `create_assistant(assistant_data)`: Inserts a new assistant record into the Assistants table. Checks for unique primary key.
- `read_assistant(assistant_id)`: Retrieves an assistant record by assistant ID.
- `update_assistant(assistant_data)`: Updates an existing assistant record.
- `delete_assistant(assistant_id)`: Deletes an assistant record by assistant ID.

- `create_conversation(conversation_data)`: Inserts a new conversation record into the Conversations table. Checks for unique primary key.
- `read_conversation(conversation_id)`: Retrieves a conversation record by conversation ID.
- `update_conversation(conversation_data)`: Updates an existing conversation record.
- `delete_conversation(conversation_id)`: Deletes a conversation record by conversation ID.

### Utility Methods

- `close()`: Closes the database connection.

## Usage

The `DatabaseUtils` class is intended for internal use within other classes functions, not alone.
---

## Future Development

    IntelliMateClient Class
        Will tie everything together.
        Will manage User, Assistant, and Conversation instances.
        Will handle data persistence through DatabaseUtils.

    Profile Class
        Planned for future to manage multiple profiles for a user.

Overall Status:

    We've laid a solid foundation with well-defined classes and responsibilities.
    Each class has a data object that can be easily serialized to JSON, making it convenient for database storage.
    The code is modular, making it easier to extend and maintain.

Next Steps:

    Implement the IntelliMateClient class.
    Add more advanced features like multiple profiles, notifications, etc.
    Thoroughly test each component and the system as a whole.