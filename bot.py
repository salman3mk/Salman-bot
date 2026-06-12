from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "8884861151:AAHnuEI8tLuXLTwK9X7KSIkim6lNDorFUoc"

async def check_edited_message(update, context):
    if update.edited_message and update.edited_message.photo:
        try:
            await context.bot.delete_message(
                chat_id=update.edited_message.chat_id, 
                message_id=update.edited_message.message_id
            )
            # تم حذف المنشن مؤقتاً عشان نتأكد أن الكود يشتغل بدون أخطاء إرسال
            print("تم الحذف بنجاح")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, check_edited_message))
    print("البوت يعمل الآن...")
    app.run_polling()
