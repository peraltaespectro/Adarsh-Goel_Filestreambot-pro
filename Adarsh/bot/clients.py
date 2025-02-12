# (c) adarsh-goel

import asyncio
import logging
from ..vars import Var
from pyrogram import Client
from Adarsh.utils.config_parser import TokenParser
from . import multi_clients, work_loads, StreamBot


async def initialize_clients():
    multi_clients[0] = StreamBot
    work_loads[0] = 0
    all_tokens = TokenParser().parse_from_env()
    if not all_tokens:
        print("Nenhum cliente adicional encontrado, usando o cliente padrão")
        return
    
    async def start_client(client_id, token):
        try:
            print(f"Iniciando - Cliente {client_id}")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                print("Isso levará algum tempo, por favor aguarde...")
            client = await Client(
                name=str(client_id),
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=token,
                sleep_threshold=Var.SLEEP_THRESHOLD,
                no_updates=True,
                in_memory=True
            ).start()
            work_loads[client_id] = 0
            return client_id, client
        except Exception:
            logging.error(f"Falha no cliente inicial - {client_id} Erro:", exc_info=True)
    
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    multi_clients.update(dict(clients))
    if len(multi_clients) != 1:
        Var.MULTI_CLIENT = True
        print("Modo Multi-Cliente Ativado")
    else:
        print("Nenhum cliente adicional foi inicializado, usando o cliente padrão")
