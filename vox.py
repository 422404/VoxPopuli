#!/usr/bin/env python3

import discord
import schedule
import threading
import time
import asyncio

import propaganda

# CHANNEL_22H22 = 407644352236748812 # Test bots
CHANNEL_22H22 = 648637884555067428 # Salon 22h22
HOUR_22H22 = "22:22"
LOOP = None

def do_propaganda():
    co = asyncio.run_coroutine_threadsafe(
            client.get_channel(CHANNEL_22H22) \
                .send(propaganda.random_propaganda()),
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
        schedule.every().day.at(HOUR_22H22).do(do_propaganda)

if __name__ == "__main__":
    with open("./token", "r") as token_file:
        token = token_file.readline().replace("\n", "")
        LOOP = asyncio.new_event_loop()
        asyncio.set_event_loop(LOOP)
        client = VoxPopuli()
        propagandaThread = PropagandaDispenser()
        propagandaThread.start()
        client.run(token)
