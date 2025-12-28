from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = "8434877305:AAHM6ZWHVCSeKVkxWRkZcGasxQAT3EXOODc"

REQUIRED_CHANNELS = [
    "@GamblingFlash",
    "@stakescriptchat",
    "@flashbeggar",
    "https://t.me/+YRM32HIE7JA4YTM0"
]

WELCOME_IMAGE = "welcome.jpg"   # save the image you uploaded as this name

async def is_user_member(bot, user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    if not await is_user_member(context.bot, user.id):
        buttons = [
            [InlineKeyboardButton("🔔 Join All Channels", url="https://t.me/GamblingFlash")],
            [InlineKeyboardButton("Check Again ✅", callback_data="check")]
        ]
        await update.message.reply_text(
            "⚠️ Please join all required channels to use this bot.",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    caption = f"""
👋 Welcome *{user.first_name}*  
to *Stake New Flash USDT Software Bot* 🚀

Here you can generate unlimited USDT in your stake account 💸

🔧 Bot is under maintenance during New Year week  
Please wait for updates 🔗
"""
    with open(WELCOME_IMAGE, "rb") as photo:
        await context.bot.send_photo(chat_id, photo, caption=caption, parse_mode="Markdown")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
