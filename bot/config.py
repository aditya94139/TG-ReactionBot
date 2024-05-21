from os import environ as env

class Telegram:
    API_ID = int(env.get("TG_API_ID", 25586552))
    API_HASH = env.get("TG_API_HASH", "f265cba9d76dc6ad70914accbe758f47")
    BOT_TOKEN = env.get("TG_BOT_TOKEN", "6848378332:AAEoqWcliC0bGu_8dKPpS04AY4pnNoA-aQA")
    BOT_USERNAME = env.get("TG_BOT_USERNAME", "rxnwbot")
    EMOJIS = [
        "👍", "❤", "🔥", "🥰", 
        "👏", "🎉", "🤩", "🙏", 
        "👌", "🕊", "🥱", "😍", 
        "❤‍🔥", "💯", "💔", "💋", 
        "🙈", "😇", "🤗", "🆒",
        "💘", "🙉", "😘"
        
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
