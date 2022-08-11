import datetime

import requests

import config
from utils import log

if __name__ == "__main__":
    week_number = datetime.datetime.now().isocalendar()[1]

    if (config.SYNC_FIRST_WEEK_NUMBER - week_number) % 2 == 0:
        log("Sending notification")
        
        if config.SYNC_ZOOM_SWITCH:
            requests.post(
                config.SYNC_DISCORD_WEBHOOK_URL,
                json={
                    "content": f"<@&{config.SYNC_DISCORD_MENTION_ROLE_ID}> Скоро синхронизация. Сегодня она в ZOOM: {config.SYNC_ZOOM_ROOM}"
                },
            )
        else:
            requests.post(
                config.SYNC_DISCORD_WEBHOOK_URL,
                json={
                    "content": f"<@&{config.SYNC_DISCORD_MENTION_ROLE_ID}> Скоро синхронизация тут: <#{config.SYNC_DISCORD_CHANNEL_ID}>"
                },
            )
        
    else:
        log("Not sending notification")
