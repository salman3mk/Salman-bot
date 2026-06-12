import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
import asyncio

# سنستخدم المتغير الذي وضعناه في موقع Render
TOKEN = os.environ.get("BOT_TOKEN")

async def handle_edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.edited_message and update.edited_message.photo:
        chat_id = update.edited_message.chat_id
        message_id = update.edited_message.message_id
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception as e:
            print(f"Error: {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Update.EDITED_MESSAGE, handle_edit))
    
    print("البوت يعمل الآن...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # إبقاء البوت يعمل
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())

