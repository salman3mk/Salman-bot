from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = "8910932956:AAGxBUawRUJN3DHtHWuifcsSgtCpWLjlMSk"

async def handle_edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # نتحقق إذا كانت الرسالة المعدلة تحتوي على صورة
    if update.edited_message and update.edited_message.photo:
        user_name = update.edited_message.from_user.first_name
        chat_id = update.edited_message.chat_id
        message_id = update.edited_message.message_id
        
        try:
            # حذف الرسالة
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            # إرسال رسالة التنبيه
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"🚫 تم حذف رسالة نصية تم تعديلها إلى صورة بواسطة: {user_name}"
            )
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # ربط البوت بحدث "تعديل الرسائل"
    app.add_handler(MessageHandler(filters.Update.EDITED_MESSAGE, handle_edit))
    
    print("البوت يعمل الآن...")
    app.run_polling()
