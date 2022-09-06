import requests

import config
from utils import log

if __name__ == "__main__":
    if config.COVID_CONTROL_ENABLED:
        log("COVID control enbled")

        requests.post(
            config.COVID_DISCORD_WEBHOOK_URL,
            json={
                "content": f"<@&{config.SYNC_DISCORD_MENTION_ROLE_ID}> Кого настиг ковид, поставьте, пожалуйста 🦠"
            },
        )
    else:
        log("COVID control disabled")
