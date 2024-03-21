from fastapi import APIRouter
from fastapi.responses import JSONResponse

from starlette import status

from .models import ChatMessage
from .services import send_message_service

telegram_router = APIRouter(prefix="/api/v1/telegram", tags=["telegram"])


@telegram_router.post('/send-message/',
                      status_code=status.HTTP_202_ACCEPTED)
async def send_message_controller(body: ChatMessage) -> JSONResponse:
    """
    Get your message and send to chat_id from bot in Telegram
    :param: body: data for sending message in Telegram
    :return: response: message about status of sending
    """
    await send_message_service(data=body.model_dump())
    return JSONResponse({'detail': 'Message was successfully send'})
