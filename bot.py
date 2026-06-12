import logging
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تفعيل نظام تسجيل الأخطاء (Log)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن الجديد الصحيح الخاص بك
TOKEN = "8903189772:AAFEir4RIJUQDKCFYXnWVrqDmejNfK-B914"

async def check_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التحقق من أن التعديل يحتوي على صورة (Photo)
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            
            # حذف الرسالة المعدلة فوراً
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            print(f"تم حذف صورة معدلة في المجموعة {chat_id}")
            
        except Exception as e:
            print(f"الخطأ أثناء الحذف: {e}. تأكد من صلاحيات البوت.")

def main():
    # بناء التطبيق باستخدام التوكن الصحيح
    application = Application.builder().token(TOKEN).build()

    # إضافة معالج للرسائل المعدلة فقط
    application.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, check_edited_message))

    # تشغيل البوت بطريقة متوافقة مع السيرفر والـ event loop
    print("البوت يعمل الآن...")
    
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop.run_until_complete(application.run_polling())

if __name__ == '__main__':
    main()
