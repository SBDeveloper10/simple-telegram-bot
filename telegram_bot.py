from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("How May I Help You?")


def reply(update: Update, context: CallbackContext) -> None:
    query = update.message.text.lower()
    user_name = update.effective_user.first_name
    replies = {
        "hi": f"Hello, {user_name}",
        "how are you?": "I'm fine thank you.",
        "what's your name?": "My name is SB Developer.",
        "bye": "See you!"
    }
    for key, value in replies.items():
        if query in key:
            update.message.reply_text(value)
            break
    else:
        update.message.reply_text("Sorry, I didn't get that.")


def main():
    api = "5955133468:AAE_OwbAUagQ1k5OEMBARoq_GRPG5FJyjb8"
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
