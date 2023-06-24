from telethon import TelegramClient
from telethon import functions, types

session_name = "monbot"
api_id = 20719656
api_hash = 'e8ee9ebff72b97d42356e4f53f258d8c'
report_id = "@EskandarAtrakchi"
with TelegramClient(session_name, api_id, api_hash) as client:
    client.start()
    peer = client.loop.run_until_complete(client.get_input_entity(report_id))
    print(peer)

    result = client.loop.run_until_complete(client(functions.account.ReportPeerRequest(
        peer=peer,
        reason=types.InputReportReasonSpam(),
        message='Spam accoount'
    ))
    )
    print("result", result)
