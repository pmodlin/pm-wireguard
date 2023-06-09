import asyncio

from aiogram import executor, types
from loader import dp, logger
import handlers


async def set_default_commands(dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("menu", "Меню"),
            types.BotCommand("help", "Помощь"),
        ]
    )


async def on_startup(dispatcher):
    await asyncio.sleep(1)
    await set_default_commands(dispatcher)
    logger.info("Бот запущен")


async def on_shutdown(dispatcher):
    logger.info("Бот остановлен")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
