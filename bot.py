async def check_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # يحذف فقط إذا كان التعديل يحتوي على صورة
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            
            # 1. حذف الرسالة
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            
            # 2. إرسال رسالة التنبيه (هذا السطر الجديد)
            await context.bot.send_message(
                chat_id=chat_id, 
                text="لقطت شخص يعدل وحذفت الرسالة! 🚫"
            )
            
            print("تم حذف رسالة معدلة بنجاح")
        except Exception as e:
            print(f"خطأ في الحذف: {e}")
