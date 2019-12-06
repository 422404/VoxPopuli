#!/usr/bin/env python3

import discord
import schedule
import threading
import time
import asyncio
import os

from propaganda import random_propaganda

PROPAGANDA_CHANNEL_ID = int(os.environ["PROPAGANDA_CHANNEL_ID"])
TOKEN = os.environ["TOKEN"]
PROPAGANDA_NEWS_REPORT_HOUR = os.environ["PROPAGANDA_NEWS_REPORT_HOUR"]
LOOP = None

def do_propaganda():
    co = asyncio.run_coroutine_threadsafe(
            client.get_channel(PROPAGANDA_CHANNEL_ID) \
                .send(random_propaganda()),
            LOOP)
    co.result()

class PropagandaDispenser(threading.Thread):
    def run(self, *args, **kwargs):
        while True:
            schedule.run_pending()
            time.sleep(1)

class VoxPopuli(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        schedule.every().day.at(PROPAGANDA_NEWS_REPORT_HOUR).do(do_propaganda)

if __name__ == "__main__":
    LOOP = asyncio.new_event_loop()
    asyncio.set_event_loop(LOOP)
    client = VoxPopuli()
    propagandaThread = PropagandaDispenser()
    propagandaThread.start()
    client.run(TOKEN)
