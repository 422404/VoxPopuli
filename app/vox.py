#!/usr/bin/env python3

import discord
import schedule
import threading
import time
import asyncio
import os
import logging

from propaganda import random_propaganda, speak_as_the_people, format_propaganda
from debug import exception_log, startup_log


TOKEN = os.environ["TOKEN"]
OWNER_ID = os.environ["OWNER_ID"]
PROPAGANDA_CHANNEL_ID = int(os.environ["PROPAGANDA_CHANNEL_ID"])
PROPAGANDA_NEWS_REPORT_HOUR = os.environ["PROPAGANDA_NEWS_REPORT_HOUR"]
PROPAGANDA_NEWS_REPORT_OVERRIDE = os.environ.get("PROPAGANDA_NEWS_REPORT_OVERRIDE")
PROPAGANDA_MAKERS = [ int(x) for x in os.environ["PROPAGANDA_MAKERS"].split() ]
LOOP = None


def do_news_propaganda():
    co = asyncio.run_coroutine_threadsafe(
            client.get_channel(PROPAGANDA_CHANNEL_ID) \
                .send(random_propaganda(PROPAGANDA_NEWS_REPORT_OVERRIDE)),
            LOOP)
    co.result()


def is_propagandable(id):
    return id in PROPAGANDA_MAKERS


class PropagandaDispenser(threading.Thread):
    def run(self, *args, **kwargs):
        while True:
            schedule.run_pending()
            time.sleep(1)


class VoxPopuli(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await startup_log(self, OWNER_ID)
        schedule.every().day.at(PROPAGANDA_NEWS_REPORT_HOUR).do(do_news_propaganda)
    
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        trimmed = message.content.strip()
        if trimmed.startswith("/as-vox"):
            if is_propagandable(message.author.id):
                trimmed = trimmed.replace("/as-vox", "").strip()
                await speak_as_the_people(self, message, trimmed)
        
        elif trimmed.startswith("/vox-news"):
            if is_propagandable(message.author.id):
                trimmed = trimmed.replace("/vox-news", "").strip()
                text = format_propaganda(random_propaganda(
                        PROPAGANDA_NEWS_REPORT_OVERRIDE))
                await speak_as_the_people(self, message, text)
    
    
    async def on_error(self, *args, **kwargs):
        exc_str = logging.traceback.format_exc()
        await exception_log(self, OWNER_ID, exc_str)


if __name__ == "__main__":
    LOOP = asyncio.new_event_loop()
    asyncio.set_event_loop(LOOP)
    client = VoxPopuli()
    propagandaThread = PropagandaDispenser()
    propagandaThread.start()
    client.run(TOKEN)
