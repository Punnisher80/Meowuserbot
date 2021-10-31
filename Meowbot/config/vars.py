# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if os.path.exists("config.py"):
    from mew_config import Development as Config
else:
    from userbot.Config import Config
