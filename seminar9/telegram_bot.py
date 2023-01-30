
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

count = 221
player = 2

async def chat_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player
    global base
    if base > 0:
        await update.message.reply_text(f'Осталось {count} конфет')
        await update.message.reply_text(f'Игрок {player} введите, сколько конфет вы возьмете: ')
        text = update.message.text.split()
        text = int(text[1])
        count-= text
        if count<= 0:
            await update.message.reply_text(f'Конфет больше нет! вы выиграли!')
        else:
            await update.message.reply_text(f'Осталось {count} конфет')
        player = 3-player
    else:
        await update.message.reply_text('Конфет не осталось')


def finish():
    return count 