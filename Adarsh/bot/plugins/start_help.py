# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["Start","Help","login"],
                ["Follow","Ping","Status","Maintainers"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["/start","/help","/login"],
                ["/follow","/ping","/status","/maintainers"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('/start')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Novo Usuário Associado:** \n\n__Meu Novo Amigo__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Começou Seu Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "BANIDO":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__DESCULPE, VOCÊ ESTÁ PROIBIDO DE ME USAR. ENTRE EM CONTATO COM O DESENVOLVEDOR__\n\n  **ELE VAI TE AJUDAR**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/9d94fc0af81234943e1a9.jpg",
                caption="<i>INSCREVA-SE NO CANAL PARA ME USAR🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ENTRAR 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>ALGO DEU ERRADO</i> <b> <a href='https://github.com/adarsh-goel'>CLIQUE AQUI PARA OBTER APOIO</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
        caption =f'Oi {m.from_user.mention(style="md")}!,\nEu Sou um Bot do Telegram Gerador de Arquivo Para Link com suporte para canal.\nEnvie-me qualquer arquivo e obtenha um link de Download Direto e um link para streaming.!',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('/help')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Novo Usuário Associado **\n\n__Meu Novo Amigo__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Começou Seu Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "BANIDO":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>DESCULPE, SENHOR, VOCÊ ESTÁ BANIDO DE ME USAR. ENTRE EM CONTATO COM O DESENVOLVEDOR</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                Caption="**PARTICIPE DO CANAL DE UPDATES PARA USAR ESTE BOT!**\n\n__POR SOBRECARGA, SOMENTE INSCRITOS DO CANAL PODEM USAR O BOT!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ENTRAR NO CANAL DE UPDATES", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__SUPORTE. CONTATE-ME__ [ADARSH GOEL](https://github.com/adarsh-goel/-pro/issues).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>Envie-me qualquer arquivo ou vídeo que eu lhe darei o link para stream e o link para download.</b>\n
<b>Eu também apoio Canais, me adicione no seu Canal e mande qualquer arquivo de mídia e veja o milagre✨. \nMe envie também /list para conhecer todos os comandos""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ Desenvolvedor", url="https://github.com/adarsh-goel")],
                [InlineKeyboardButton("💥 Código Fonte", url="https://github.com/adarsh-goel/-pro/")]
            ]
        )
    )
