from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import credentials


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    await update.message.reply_text(f'Hi {username}, Welcome to Chikhordam bot!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("....................")


def main():
    application = Application.builder().token(credentials.API_TOKEN).build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()