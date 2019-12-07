#!/usr/bin/env python3

import discord
import schedule
import threading
import time
import asyncio
import os

from propaganda import random_propaganda, speak_as_the_people


TOKEN = os.environ["TOKEN"]
PROPAGANDA_CHANNEL_ID = int(os.environ["PROPAGANDA_CHANNEL_ID"])
PROPAGANDA_NEWS_REPORT_HOUR = os.environ["PROPAGANDA_NEWS_REPORT_HOUR"]
PROPAGANDA_MAKERS = [ int(x) for x in os.environ["PROPAGANDA_MAKERS"].split() ]
LOOP = None


def do_propaganda():
    co = asyncio.run_coroutine_threadsafe(
            client.get_channel(PROPAGANDA_CHANNEL_ID) \
                .send(random_propaganda()),
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
        schedule.every().day.at(PROPAGANDA_NEWS_REPORT_HOUR).do(do_propaganda)
    
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        trimmed = message.content.strip()
        if trimmed.startswith("/as-vox"):
            if is_propagandable(message.author.id):
                trimmed = trimmed.replace("/as-vox", "").strip()
                await speak_as_the_people(self, message, trimmed)


if __name__ == "__main__":
    LOOP = asyncio.new_event_loop()
    asyncio.set_event_loop(LOOP)
    client = VoxPopuli()
    propagandaThread = PropagandaDispenser()
    propagandaThread.start()
    client.run(TOKEN)
