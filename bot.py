import asyncio
from config import BOT_TOKEN, WEB_APP_URL
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handler(message: Message):
    # данные из Web App
    if message.web_app_data:
        await message.answer(
            f"📦 Данные из Web App:\n{message.web_app_data.data}"
        )
        return

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Открыть Web App",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "Нажми кнопку, чтобы открыть тестовое Web App",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
