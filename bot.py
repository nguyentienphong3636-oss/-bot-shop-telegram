import telebot
from telebot import types

# Thay đoạn chữ bên dưới bằng API Token bạn lấy từ BotFather
API_TOKEN = '8642960409:AAEc_y8aoE-i2UJvMAIwDSZt8d4BZjmF7n8'

bot = telebot.TeleBot(API_TOKEN)

# Xử lý khi người dùng bấm /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name.upper()
    
    # Tạo các nút bấm dạng bàn phím dưới khung chat (ReplyKeyboardMarkup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    
    btn1 = types.KeyboardButton("Cửa Hàng")
    btn2 = types.KeyboardButton("Nạp Tiền")
    btn3 = types.KeyboardButton("Lịch Sử Nạp")
    btn4 = types.KeyboardButton("Key Đã Mua")
    btn5 = types.KeyboardButton("Tài Khoản")
    btn6 = types.KeyboardButton("Liên Hệ & Hỗ Trợ")
    
    # Sắp xếp thứ tự các nút xuất hiện
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    # Gửi lời chào giống trong ảnh
    welcome_text = f"🙋‍♂️ Chào {user_name} ( CHÍNH CHỦ ) !\n\nChọn chức năng bên dưới:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Xử lý phản hồi khi người dùng bấm vào các nút
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Cửa Hàng":
        bot.reply_to(message, "🏪 Danh Mục: Acc Clone Free Fire\nGiá bán: 2.000đ...\n(Bạn có thể viết thêm code xử lý tại đây)")
    elif message.text == "Nạp Tiền":
        bot.reply_to(message, "💳 Vui lòng chuyển khoản theo cú pháp...")
    # Tương tự cấu hình cho các nút còn lại...

# Chạy bot liên tục
print("Bot đang chạy...")
bot.infinity_polling()
