async def exception_log(client, owner_id, exc_str):
    user = await client.fetch_user(owner_id)
    await user.send("```\n{}\n```".format(exc_str))

async def startup_log(client, owner_id):
    user = await client.fetch_user(owner_id)
    await user.send("```diff\n+ Just started!\n```")
