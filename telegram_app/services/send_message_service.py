from telegram_app.services.client import SenderMessageTgAPI


async def send_message_service(data):
    """Service for sending message to chat by bot in Telegram"""
    bot_token = data.pop('bot_token')
    data['text'] = data.pop('message')

    client = SenderMessageTgAPI(bot_token)
    response = await client.from_api(data)
    return response
