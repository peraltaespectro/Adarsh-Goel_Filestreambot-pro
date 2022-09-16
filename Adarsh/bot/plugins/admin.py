# (c) @adarsh-goel
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from Adarsh.utils.broadcast_helper import send_msg
from Adarsh.utils.database import Database
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.name)
broadcast_ids = {}

@StreamBot.on_message(filters.command("users") & filters.private )
async def sts(c: Client, m: Message):
    user_id=m.from_user.id
    if user_id in Var.OWNER_ID:
        total_users = await db.total_users_count()
        await m.reply_text(text=f"Total de usuários no banco de dados: {total_users}", quote=True)
        
        
@StreamBot.on_message(filters.command("broadcast") & filters.private  & filters.user(list(Var.OWNER_ID)))
async def broadcast_(c, m):
    user_id=m.from_user.id
    out = await m.reply_text(
            text=f"Transmissão iniciada! Você será notificado com o arquivo de log quando todos os usuários forem notificados."
    )
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"transmissão concluída em `{completed_in}`\n\nTotal de usuários {total_users}.\nTotal feito {done}, {success} Com sucesso e {failed} fracassado.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"transmissão concluída em `{completed_in}`\n\nTotal de usuários {total_users}.\nTotal feito {done}, {success} Com sucesso e {failed} fracassado.",
            quote=True
        )
    os.remove('broadcast.txt')
