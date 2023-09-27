import json

class Assistant:
    def __init__(self, assistant_id, assistant_name, assistant_model, persona, likes, dislikes, relationship, expertise, status, tags, last_active, active_conversations, language, version, custom_settings):
        self.data = {
            "assistant_id": assistant_id,
            "assistant_name": assistant_name,
            "assistant_model": assistant_model,
            "persona": persona,
            "likes": likes,
            "dislikes": dislikes,
            "relationship": relationship,
            "expertise": expertise,
            "status": status,
            "tags": tags,
            "last_active": last_active,
            "active_conversations": active_conversations,
            "language": language,
            "version": version,
            "custom_settings": custom_settings
        }

    def to_json(self):
        return json.dumps(self.data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(
            data["assistant_id"],
            data["assistant_name"],
            data["assistant_model"],
            data["persona"],
            data["likes"],
            data["dislikes"],
            data["relationship"],
            data["expertise"],
            data["status"],
            data["tags"],
            data["last_active"],
            data["active_conversations"],
            data["language"],
            data["version"],
            data["custom_settings"]
        )

    def update_status(self, new_status):
        self.data["status"] = new_status

    def update_last_active(self, timestamp):
        self.data["last_active"] = timestamp

    def add_conversation(self, conversation_id):
        self.data["active_conversations"].append(conversation_id)

    def remove_conversation(self, conversation_id):
        self.data["active_conversations"].remove(conversation_id)