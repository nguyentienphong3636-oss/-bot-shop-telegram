import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Lấy token bảo mật từ môi trường hệ thống của Render (Không sợ lộ token trên GitHub)
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

def main_menu(name):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🛒 Cửa Hàng", callback_data="cua_hang"),
        InlineKeyboardButton("💵 Nạp Tiền", callback_data="nap_tien"),
        InlineKeyboardButton("📜 Lịch Sử Nạp", callback_data="lich_su_nap"),
        InlineKeyboardButton("🔑 Key Đã Mua", callback_data="key_da_mua"),
        InlineKeyboardButton("👤 Tài Khoản", callback_data="tai_khoan"),
        InlineKeyboardButton("📞 Liên Hệ & Hỗ Trợ ↗️", callback_data="lien_he")
    )
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name.upper()
    welcome_text = f"💎 Chào {user_name} ( CHÍNH CHỦ ) !\n\nChọn chức năng bên dưới:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(user_name))

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cua_hang":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🛒 Mua Ngay (2.000đ)", callback_data="mua_acc_clone"))
        markup.add(InlineKeyboardButton("⬅️ Quay Lại", callback_data="back_to_main"))
        
        shop_text = (
            "THÔNG BÁO: HÀNG MỚI ĐÃ VỀ KHO\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📦 Danh Mục: Acc Clone Free Fire\n"
            "📦 Gói: Acc Clone Lv5\n"
            "🔢 Số lượng bổ sung: +2 sản phẩm\n"
            "💰 Giá bán: 2.000đ\n\n"
            "Vào Bot ngay để chọn và mua trước khi hết hàng nhé!"
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=shop_text, reply_markup=markup)

    elif call.data == "nap_tien":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("⬅️ Quay Lại", callback_data="back_to_main"))
        nap_text = (
            "💵 HƯỚNG DẪN NẠP TIỀN TỰ ĐỘNG\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "🏦 Ngân hàng: MB BANK\n"
            "💳 Số tài khoản: 123456789999\n"
            "👤 Chủ tài khoản: NGUYEN VAN A\n"
            f"✏️ Nội dung chuyển khoản: NAP {call.from_user.id}\n\n"
            "⚠️ Hệ thống tự động cộng tiền sau 1-3 phút khi đúng nội dung!"
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nap_text, reply_markup=markup)

    elif call.data == "tai_khoan":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("⬅️ Quay Lại", callback_data="back_to_main"))
        user_text = (
            "👤 THÔNG TIN TÀI KHOẢN\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"🆔 ID Telegram: {call.from_user.id}\n"
            f"📛 Tên: {call.from_user.first_name}\n"
            "💰 Số dư: 0đ\n"
            "🌟 Cấp độ: Thành viên"
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=user_text, reply_markup=markup)

    elif call.data == "back_to_main":
        user_name = call.from_user.first_name.upper()
        welcome_text = f"💎 Chào {user_name} ( CHÍNH CHỦ ) !\n\nChọn chức năng bên dưới:"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=welcome_text, reply_markup=main_menu(user_name))
        
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("⬅️ Quay Lại", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Chức năng '{call.data}' đang cấu hình...", reply_markup=markup)

print("Bot đang chạy...")
bot.infinity_polling()
