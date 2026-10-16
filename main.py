import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Токен берется из переменных окружения (безопасно)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ВАЖНО: ЗАМЕНИ ЭТУ ССЫЛКУ на реальную ссылку Telegram Александра!
ALEXANDER_LINK = "https://t.me/otecalexander 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="🎁 Получить материалы", callback_data="materials")
    kb.button(text="♟️ О занятиях", callback_data="about")
    kb.button(text="🗓️ Расписание", callback_data="schedule")
    kb.button(text="✍️ Записаться к Александру", url=ALEXANDER_LINK)
    kb.adjust(1) # Кнопки в один столбик
    
    await message.answer(
        "Привет! Я бот-помощник Александра по шахматам. ♟️\n\n"
        "Здесь ты можешь получить полезные материалы и записаться на пробное занятие.",
        reply_markup=kb.as_markup()
    )

@dp.callback_query(F.data == "materials")
async def send_materials(callback: types.CallbackQuery):
    await callback.message.answer("🎁 Ссылка на полезные материалы: https://youtu.be/пример_ссылки\n\nТакже подписывайся на канал: https://t.me/пример_канала")
    await callback.answer()

@dp.callback_query(F.data == "about")
async def send_about(callback: types.CallbackQuery):
    await callback.message.answer("♟️ **О занятиях:**\n\nПровожу индивидуальные и групповые занятия для детей и взрослых. Помогу развить логику, мышление и уверенность в себе! Первое занятие — бесплатное.")
    await callback.answer()

@dp.callback_query(F.data == "schedule")
async def send_schedule(callback: types.CallbackQuery):
    await callback.message.answer("🗓️ **Расписание:**\n\nПн-Пт: 16:00 - 20:00\nСб: 10:00 - 14:00\n\nЗапись открыта!")
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
