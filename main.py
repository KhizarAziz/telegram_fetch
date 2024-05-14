from tele_msg_fetcher import TelegramMessageFetcher
fetcher = TelegramMessageFetcher()

chat_id = 307373020 # TO GET IDs RUN: fetcher.client.loop.run_until_complete(fetcher.list_chats())
msg_search_query = "TLDR AI"
messages_to_fetch = 5

# Chat cannot be found with just name, so using entity object.
entity = fetcher.client.loop.run_until_complete(fetcher.get_entity(chat_id))

if entity:
    # Fetching messages for the entity and printing them.
    messages = fetcher.client.loop.run_until_complete(fetcher.fetch_messages(entity, msg_search_query,messages_to_fetch))
    for message_id, text in messages:
        print(f"Message ID: {message_id}")# - Text: {text}")
else:
    print("Failed to load entity.")