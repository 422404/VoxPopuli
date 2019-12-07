# How to add it to your server
https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot

# Config
Configure the bot through environment variables.

| Variable name                         | Value                                            |
|:--------------------------------------|:-------------------------------------------------|
| TOKEN                                 | The bot discord API token                        |
| PROPAGANDA_CHANNEL_ID                 | The ID of the channel where to output propaganda |
| PROPAGANDA_NEWS_REPORT_HOUR           | The hour of the news report                      |

# Installation

Build a docker image or push it to heroku !

If using Heroku, don't forget to set your timezone!
> Ex: heroku config:add TZ="America/Los_Angeles"
