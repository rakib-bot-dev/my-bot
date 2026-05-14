import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- সেটিংস ---
TOKEN = '8391685404:AAHUw4nncxHzRqE0W0AHHbAos27Vnl64uik'
ADMIN_ID = 7208807208    
SUPPORT_ID = "@BD_RH_Support"
BIKASH_NO = "01322656036"
CHANNEL_LINK = "https://t.me/BD_topup_shop_R"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- মেইন মেনু ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['📧 জিমেইল সেল (Gmail Sale)', '💎 ডায়মন্ড লিস্ট (Diamond List)'],
        ['💰 আমার ওয়ালেট (My Wallet)', '🛍️ আমার অর্ডার (My Orders)'],
        ['💸 ডিপোজিট (Deposit)', '🏦 উইথড্র (Withdraw)'],
        ['📢 জয়েন চ্যানেল (Join Channel)', '🤝 রেফার (Referral)'],
        ['🎧 সাপোর্ট এডমিন (Support)', '🕒 Selling Time']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👋 স্বাগতম! আপনার প্রয়োজনীয় বাটনটি সিলেক্ট করুন।", reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # বাটনগুলোর জন্য ছোট মেসেজ রেসপন্স
    app.add_handler(MessageHandler(filters.Regex('🎧 সাপোর্ট এডমিন'), lambda u, c: u.message.reply_text(f"সাপোর্টের জন্য যোগাযোগ করুন: {SUPPORT_ID}")))
    app.add_handler(MessageHandler(filters.Regex('🕒 Selling Time'), lambda u, c: u.message.reply_text("আমাদের সেলিং টাইম: সকাল ৮টা - রাত ১০টা")))
    app.add_handler(MessageHandler(filters.Regex('📢 জয়েন চ্যানেল'), lambda u, c: u.message.reply_text(f"আমাদের চ্যানেলে জয়েন করুন: {CHANNEL_LINK}")))
    
    print("Bot is running...")
    app.run_polling()
