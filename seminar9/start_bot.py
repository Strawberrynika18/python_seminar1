from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import telegram_bot

app = ApplicationBuilder().token("6066683041:AAFqGbzCRpqbRti3kMxxemVchBe6nk2ZxxM").build()

app.add_handler(CommandHandler("chat_bot", telegram_bot.chat_bot))


app.run_polling()