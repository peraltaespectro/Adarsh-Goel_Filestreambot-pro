#(c) Adarsh-Goel
import os
import asyncio
from asyncio import TimeoutError
from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


MY_PASS = os.environ.get("MY_PASS",None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")


@StreamBot.on_message((filters.regex("Login") | filters.command("login")) , group=4)
async def login_handler(c: Client, m: Message):
    try:
        try:
            ag = await m.reply_text("Agora me mande a senha.\n\nSe você não sabe verifique o MY_PASS Variável no heroku \n\n(Você pode usar /cancel comando para cancelar o processo)")
            _text = await c.listen(m.chat.id, filters=filters.text, timeout=90)
            if _text.text:
                textp = _text.text
                if textp=="/cancel":
                   await ag.edit("Processo cancelado com sucesso")
                   return
            else:
                return
        except TimeoutError:
            await ag.edit("Não posso esperar mais pela senha, tente novamente")
            return
        if textp == MY_PASS:
            await pass_db.add_user_pass(m.chat.id, textp)
            ag_text = "Você digitou a senha corretamente \n\nAGORA VOCÊ PODE USAR O BOT"
        else:
            ag_text = "Senha errada, tente novamente \n\nEnvie /login Novamente"
        await ag.edit(ag_text)
    except Exception as e:
        print(e)

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(m.chat.id)
        if check_pass== None:
            await m.reply_text("Faça login primeiro usando o comando /login \nNão sabe a senha? solicite ao desenvolvedor")
            return
        if check_pass != MY_PASS:
            await pass_db.delete_user(m.chat.id)
            return
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"Novo usuário associado : \n\n Nome : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Começou Seu Bot !!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "Banido":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__DESCULPE, SENHOR, VOCÊ ESTÁ BANIDO DE ME USAR.__\n\n  **ENTRE EM CONTATO COM O DESENVOLVEDOR [@adarsh-goel](https://github.com/adarsh-goel) ELE VAI TE AJUDAR**",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>INSCREVA-SE NO CANAL DE ATUALIZAÇÕES PARA ME USAR 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ENTRAR 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**ALGO DEU ERRADO. ENTRE EM CONTATO COMIGO** [@adarsh-goel](https://github.com/adarsh-goel)",
                
                disable_web_page_preview=True)
            return
    try:

        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
       
        
        

        msg_text ="""
<i><u>Seu Link Foi Gerado !</u></i>

<b>📂 NOME DO ARQUIVO: </b> 
<i>{}</i>

<b>📦 TAMANHO DO ARQUIVO: </b> 
<i>{}</i>

<b>📥 DOWNLOAD: </b> 
<i>{}</i>

<b>🖥 ASSISTIR: </b>
<i>{}</i>

<b>🚸 NOTA 🚸</b>
<b>O LINK NÃO VAI EXPIRAR ATÉ QUE EU O DELETE</b>"""

        await log_msg.reply_text(text=f"**REQUERIDO POR :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**ID DO USUÁRIO :** `{m.from_user.id}`\n**Link de Streaming :** {stream_link}", disable_web_page_preview=True,  quote=True)
        await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥  ASSISTIR  🖥", url=stream_link), #Stream Link
                                                InlineKeyboardButton('📥  BAIXAR  📥', url=online_link)]]) #Download Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Tenho um Flood {str(e.x)}s a partir de [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**Id De Usuário :** `{str(m.from_user.id)}`", disable_web_page_preview=True)


@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(broadcast.chat.id)
        if check_pass == None:
            await broadcast.reply_text("Faça login primeiro usando o comando /login \nNão sabe a senha? solicite ao desenvolvedor!")
            return
        if check_pass != MY_PASS:
            await broadcast.reply_text("Senha errada, tente novamente \n\nEnvie /login Novamente")
            await pass_db.delete_user(broadcast.chat.id)
            return
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        await log_msg.reply_text(
            text=f"**Nome do Canal:** `{broadcast.chat.title}`\n**ID do Canal:** `{broadcast.chat.id}`\n**URL de solicitação:** {stream_link}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🖥  ASSISTIR  🖥", url=stream_link),
                     InlineKeyboardButton('📥  BAIXAR  📥', url=online_link)] 
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Tenho um Flood {str(w.x)}s a partir de {broadcast.chat.title}\n\n**ID do Canal:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#Error_Traceback:** `{e}`", disable_web_page_preview=True)
        print(f"Não é possível editar a mensagem de transmissão!\nErro:  **Dê-me permissão para editar as atualizações no Canal{e}**")
