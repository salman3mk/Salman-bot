import logging
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تفعيل نظام تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8903189772:AAFEir4RIJUQDKCFYXnWVrqDmejNfK-B914"

async def check_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            print(f"تم حذف صورة معدلة في المجموعة {chat_id}")
        except Exception as e:
            print(f"خطأ أثناء الحذف: {e}")

async def run_bot():
    # بناء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # إضافة المعالج
    application.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, check_edited_message))
    
    # تشغيل البوت
    print("البوت يعمل الآن...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    # البقاء في حالة انتظار
    try:
        await asyncio.Event().wait()
    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()

if __name__ == '__main__':
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        pass
