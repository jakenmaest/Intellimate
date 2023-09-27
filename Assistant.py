import json
from typing import List, Dict, Any, Union

class Assistant:
    def __init__(self, 
                 assistant_id: str, 
                 assistant_name: str, 
                 assistant_model: str, 
                 persona: str, 
                 likes: List[str], 
                 dislikes: List[str], 
                 relationship: str, 
                 expertise: str, 
                 status: str, 
                 tags: List[str], 
                 last_active: str, 
                 active_conversations: List[str], 
                 language: str, 
                 version: str, 
                 custom_settings: Dict[str, Any]) -> None:
        self.data: Dict[str, Union[str, List[str], Dict[str, Any]]] = {
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

    def to_json(self) -> str:
        return json.dumps(self.data)

    @classmethod
    def from_json(cls, json_str: str) -> 'Assistant':
        data: Dict[str, Any] = json.loads(json_str)
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

    def update_status(self, new_status: str) -> None:
        self.data["status"] = new_status

    def update_last_active(self, timestamp: str) -> None:
        self.data["last_active"] = timestamp

    def add_conversation(self, conversation_id: str) -> None:
        self.data["active_conversations"].append(conversation_id)

    def remove_conversation(self, conversation_id: str) -> None:
        self.data["active_conversations"].remove(conversation_id)
