from datetime import datetime
import texts


def random_propaganda(override):
    if override:
        report = texts.__getattribute__(override)
    else:
        report = texts.get_random_news_report()
    return format_propaganda(report)


def format_propaganda(text):
    date = datetime.now().strftime("%d/%m/%Y")
    year = datetime.now().strftime("%Y")
    return text.format(date=date, year=year)


async def speak_as_the_people(client, message, text):
    await message.delete()
    await message.channel.send(text)
