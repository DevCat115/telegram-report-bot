import time
from telethon import TelegramClient, functions, types

api_id = 20719656
api_hash = 'e8ee9ebff72b97d42356e4f53f258d8c'
session_name = "monbot"


def get_users():
    account_file = open('accounts.txt', 'r')
    accounts = account_file.readlines()
    return [account.strip() for account in accounts if account]


with TelegramClient(session_name, api_id, api_hash) as client:
    client.start()
    users = get_users()
    for user in users:
        peer = client.loop.run_until_complete(client.get_input_entity(user))
        result = client.loop.run_until_complete(client(functions.account.ReportPeerRequest(
            peer=peer,
            reason=types.InputReportReasonSpam(),
            message='Spam account'
        ))
        )
        print(f"{user} report status: {result}")
        time.sleep(1)
