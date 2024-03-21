from pydantic import BaseModel, field_validator, Field


class ChatMessage(BaseModel):
    bot_token: str
    chat_id: str = Field(min_length=1)
    message: str = Field(min_length=1)

    @field_validator('bot_token')
    def validate_bot_token(cls, v: str) -> str: # noqa
        """Custom validation of bot_token param"""
        if len(v) != 46:
            raise ValueError("Invalid Bot Token")
        return v
