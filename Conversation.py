import json
import datetime
from typing import List, Dict, Any, Optional

class Conversation:
    def __init__(self, conversation_id: str, start_time: str) -> None:
        self.data: Dict[str, Any] = {
            'messages': [],
            'info': {
                'conversation_id': conversation_id,
                'start_time': start_time,
                'end_time': None,
                'status': 'active'
            }
        }

    def add_message(self, role: str, content: str, model: Optional[str] = None) -> None:
        message: Dict[str, Any] = {
            'role': role,
            'content': content,
            'timestamp': datetime.datetime.now().isoformat(),
            'model': model,
            'token_count': len(content.split()),
            'message_id': len(self.data['messages']) + 1,
            'response_time': None  # This can be updated later
        }
        self.data['messages'].append(message)

    def get_messages(self) -> List[Dict[str, Any]]:
        return self.data['messages']

    def get_last_message(self) -> Optional[Dict[str, Any]]:
        return self.data['messages'][-1] if self.data['messages'] else None

    def get_message_by_id(self, message_id: int) -> Optional[Dict[str, Any]]:
        for message in self.data['messages']:
            if message['message_id'] == message_id:
                return message
        return None

    def update_message(self, message_id: int, new_content: str) -> None:
        message: Optional[Dict[str, Any]] = self.get_message_by_id(message_id)
        if message:
            message['content'] = new_content
            message['token_count'] = len(new_content.split())

    def delete_message(self, message_id: int) -> None:
        self.data['messages'] = [msg for msg in self.data['messages'] if msg['message_id'] != message_id]

    def end_conversation(self, end_time: str) -> None:
        self.data['info']['end_time'] = end_time
        self.data['info']['status'] = 'inactive'

    def get_info(self) -> Dict[str, Any]:
        return self.data['info']

    def to_json(self) -> str:
        return json.dumps(self.data)

    def from_json(self, json_str: str) -> None:
        self.data = json.loads(json_str)