from telethon import TelegramClient
import os

class TelegramMessageFetcher:
    """
    A class to fetch messages from specified Telegram chat IDs based on search queries
    using the Telegram API.
    """
    
    def __init__(self):
        """
        Initializes the TelegramClient with API credentials from environment variables.
        """
        self.api_id = os.getenv('TELEGRAM_API_ID')
        self.api_hash = os.getenv('TELEGRAM_API_HASH')
        self.session_file = "my_telegram_session"
        self.client = TelegramClient(self.session_file, self.api_id, self.api_hash)
        self.client.start()
        print("Telegram client loaded Successfully.")

    async def fetch_messages(self, entity, msg_search_query, messages_limit):
        """
        Fetches the most recent messages from the entity that match the search query and returns them as a list.
        
        :param entity: The Telegram entity from where messages are to be fetched.
        :param msg_search_query: The query string to search messages for.
        :return: List of messages matching the search query.
        """
        messages = []
        async for message in self.client.iter_messages(entity, limit=messages_limit, search=msg_search_query):
            messages.append((message.id, message.text))
        return messages

    async def get_entity(self, user_id):
        """
        Fetches the Telegram entity based on user ID.

        :param user_id: The user ID of the Telegram entity.
        :return: Returns the Telegram entity if found; otherwise, None.
        """
        async for dialog in self.client.iter_dialogs():
            if dialog.entity.id == user_id:
                return dialog.entity
        print(f"Entity {user_id} not found in recent dialogs.")
        return None

    async def list_chats(self):
        """
        Lists all chats in the Telegram client's dialogs.
        """
        async for dialog in self.client.iter_dialogs():
            print(dialog.name, "has ID", dialog.id)

