import logging
import configparser
import os
import calcgame
import candygame
import config

#try:
   
 #   conf = configparser.ConfigParser()
  #  conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
   # TOKEN = ['6066683041:AAFqGbzCRpqbRti3kMxxemVchBe6nk2ZxxM']['telegram']

#except IndexError:
#    print('Error, cant read .ini file')

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    filename='bot.log', filemode='a'
)
logger = logging.getLogger(__name__)

class bot():
    def __init__(self):
        self.project = False
        self.current_gamer = dict() 
        self.current_user_game = dict()
        self.delete_msg_id = 0
        self.current_user_id = '1'
        self.msg_update = ()
        self.msg_context = ()
        self.game_dict = dict({'nogame': {'function': self.start, 'help': 'Игра не выбрана', 'command': '/start'},
                               'candy': {'function': self.GameCandy, 'help': 'Сколько конфет возьмете?', 'command': '/candy'},
                               'calc': {'function': self.GameCalc, 'help': 'Введите выражение', 'command': '/calc'}
                               })

        self.commands_dict = dict({'/start': '-перезапуск бота',
                                   '/help': '- помощь',
                                   '/candy': '-игра в конфетки',
                                   '/calc': 'калькулятор'})
        
        self.start_keyboard = [
            [
                InlineKeyboardButton("Start", callback_data="command /start"),
                InlineKeyboardButton("Help", callback_data="command /help"),
            ],

            [InlineKeyboardButton("Конфетки", callback_data="command /candy")],
            [InlineKeyboardButton("Калькулятор", callback_data="command /calc")],
        ]
        self.NewBot()


    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

        self.msg_update = update
        self.msg_context = context
        self.current_user_id = update.message.from_user.id
        keyboard = self.start_keyboard
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Меню:", reply_markup=reply_markup)


    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        

        query = update.callback_query
       
        await query.answer()
        query_game, query_data = query.data.split()
        print(f"{query_game}, {query_data}")

        if query_game == 'command':
            if query_data == '/start':
                await self.start_button(query_data=query_data)
            elif query_data == '/candy':
                await self.GameCandy(self.msg_update, self.msg_context)
            elif query_data == '/calc':
                await self.GameCalc(self.msg_update, self.msg_context)

        else:
            await query.edit_message_text(text=f"Selected option: {query.data}")

    async def start_button(self, query_data='/start') -> None:
        """обработчик нажатий кнопок на стартовом меню"""
        if query_data == '/start':
            await self.start(self.msg_update, self.msg_context)
        elif query_data == '/help':
            await self.help_command(self.msg_update, self.msg_context)
        elif query_data == '/candy':
            await self.GameCandy(self.msg_update, self.msg_context)
        elif query_data == '/calc':
            await self.GameCalc(self.msg_update, self.msg_context)
        else:
            await self.start(self.msg_update, self.msg_context)


    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        

        temp_msg = self.game_dict.get(self.current_gamer[update.message.from_user.id], self.game_dict['nogame'])['help']
        await update.message.delete()
        await update.message.reply_text(f"{temp_msg}")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        logging.info(msg=f"message from: {update.message.chat.first_name}, text: {update.message.text} ")
        self.msg_update = update
        self.msg_context = context
        self.current_user_id = update.message.from_user.id
        current_user_game = self.current_gamer[update.message.from_user.id]
        if current_user_game == 'nogame':
            await update.message.reply_text(f"Hi {update.message.from_user.first_name}({update.message.from_user.id}) "
                                            f"and you wrote {update.message.text}")
        else:
            print(update.message.text)
            result = self.current_user_game[update.message.from_user.id].UserTurn(update.message.text)
            await update.message.reply_text(result[1])
            if result[0] == 'end':
                self.current_gamer[update.message.from_user.id] = 'nogame'
                await update.message.reply_text("Игра закончена!")
                await self.start(update, context)

    async def GameCandy(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        self.current_gamer[update.message.from_user.id] = 'candy'
        self.current_user_game[update.message.from_user.id] = candygame.CandyGame(user_name=update.message.from_user.id)
        start_msg = self.current_user_game[update.message.from_user.id].StartMessage()
        await update.message.reply_text(start_msg[1])
        await update.message.reply_text("Сколько  возьмете  конфет?")

    async def GameCalc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    
        self.current_gamer[update.message.from_user.id] = 'calc'
        self.current_user_game[update.message.from_user.id] = calcgame.CalcGame(user_name=update.message.from_user.id)
        await update.message.reply_text("Введите выражение для вычисления")






    def NewBot(self) -> None:

    
        self.application = Application.builder().token ("6066683041:AAFqGbzCRpqbRti3kMxxemVchBe6nk2ZxxM").build()

        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("calc", self.GameCalc))
        self.application.add_handler(CommandHandler("candy", self.GameCandy))
        self.application.add_handler(CommandHandler("stop", self.start))

        self.application.add_handler(CallbackQueryHandler(self.button))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        self.application.run_polling()


if __name__ == "__main__":
    bot_run = bot()