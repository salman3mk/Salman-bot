async def check_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            user = update.edited_message.from_user
            
            # 1. حذف الرسالة
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            
            # 2. إرسال تنبيه مع منشن للشخص (استخدام الـ mention_html)
            user_mention = user.mention_html(user.first_name)
            await context.bot.send_message(
                chat_id=chat_id, 
                text=f"لقطت {user_mention} يعدل الصورة.. حذفتها! 🚫",
                parse_mode='HTML'
            )
            
            print(f"تم حذف صورة معدلة لـ {user.first_name}")
        except Exception as e:
            print(f"خطأ أثناء الحذف: {e}")
