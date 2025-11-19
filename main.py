import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8255428232:AAHU1852cCMnB8XIBx_UXKpGZlrYZjGwn3Y")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to ProServe Bot!\n\n"
        "✨ Tools Available:\n"
        "• Background Remover\n"
        "• HD Photo Enhance\n"
        "• PDF Tools\n"
        "• File Converter\n\n"
        "Send me any photo/file to begin!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Received! Working on your file… 🔄")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, echo))

    application.run_polling()

if __name__ == "__main__":
    main()
