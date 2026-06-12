async def check_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التأكد من وجود رسالة معدلة وتحتوي على صورة
    if update.edited_message and update.edited_message.photo:
        try:
            chat_id = update.edited_message.chat_id
            message_id = update.edited_message.message_id
            user = update.edited_message.from_user
            
            # 1. حذف الرسالة
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            
            # 2. إرسال التنبيه بطريقة أبسط
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            await context.bot.send_message(
                chat_id=chat_id, 
                text=f"يا {mention}، لقطتك تعدل الصورة! 🚫 تم الحذف.",
                parse_mode='Markdown'
            )
            
            print(f"تم الحذف والتبليغ عن {user.first_name}")
        except Exception as e:
            print(f"خطأ: {e}")
