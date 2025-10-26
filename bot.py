import os
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 📦 Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🧩 Если вдруг .env не найден — выводим предупреждение
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Убедись, что в .env он прописан корректно.")

# 🪪 Константы
WELCOME_PHOTO_ID = "AgACAgIAAxkBAAMjaKcaj16sGKNtMFqRq3GST0pQttoAAgX1MRuSdDlJFZlWDjJU6jQBAAMCAAN5AAM2BA"

# ⚙️ Настройка логирования
logging.basicConfig(level=logging.INFO)

# 🤖 Создаём бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer_photo(
        photo=WELCOME_PHOTO_ID,
        caption=(
            "<b>Добро пожаловать в SENAT!</b>\n\n"
            "Здесь ценят <b>статус</b>, <b>комфорт</b> и <b>конфиденциальность</b>.\n"
            "Мы предоставляем <b>персонализированный сервис</b> для тех, кто выбирает только лучшее.\n"
            "Ваш <b>персональный менеджер</b> готов ответить на ваши вопросы и подобрать идеальное решение."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="💬 К менеджеру", url="https://t.me/senat_mananger")],
                [InlineKeyboardButton(text="🔒 Закрытый клуб", url="https://t.me/+MpPrz-ngoBUxYWJi")],
                [InlineKeyboardButton(text="ℹ️ О нас", callback_data="about_us")]
            ]
        )
    )

# Кнопка "О нас"
@dp.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    text = (
        "<b>О нашем клубе</b>\n\n"
        "SENAT — это пространство, где ценят стиль, комфорт и уверенность.\n\n"
        "Мы предлагаем гостям атмосферу доверия и элегантного отдыха, "
        "где каждый момент продуман до мелочей.\n\n"
        "Конфиденциальность, качество и внимание к деталям — наши неизменные принципы."
    )
    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()

# Основная функция запуска
async def main():
    logging.info("🚀 Бот запущен и готов к работе.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

