import os


def get_token():
    if "TELEGRAM_TOKEN" not in os.environ:
        exit("Error: Is required a telegram token...\nExit...")
    return {
        "telegram": os.environ["TELEGRAM_TOKEN"]
    }
