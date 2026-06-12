import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8884861151:AAHnuEI8tLuXLTwK9X7KSIkim6lNDorFUoc"

async def check_edited_message(update, context):
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            user = update.edited_message.from_user
            
            # حذف الرسالة
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            
            # إرسال التنبيه
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            await context.bot.send_message(
                chat_id=chat_id, 
                text=f"يا {mention}، لقطتك تعدل الصورة! 🚫 تم الحذف.",
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, check_edited_message))
    print("البوت يعمل الآن...")
    app.run_polling()
