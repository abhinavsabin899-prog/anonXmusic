import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API Credentials
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

# Database
MONGO_DB_URI = getenv("MONGO_DB_URI", None) or getenv("MONGO_URL", None)

# Durations & Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 180))

# Owners and Loggers
OWNER_ID = int(getenv("OWNER_ID", "0"))
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

# Heroku / Server configurations
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support & Channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AnonXSupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AnonXSupportChat")

# Auto Clean & Cache
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify Credentials (Optional)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlists limits
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram Audio/Video File Size Limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# String Sessions (Auto Fallback Support)
_raw_session = (
    getenv("STRING1")
    or getenv("SESSION1")
    or getenv("STRING_SESSION")
    or getenv("SESSION")
    or None
)

STRING1 = _raw_session
SESSION1 = _raw_session
STRING_SESSION = _raw_session

STRING2 = getenv("STRING_SESSION2", None) or getenv("STRING2", None)
STRING3 = getenv("STRING_SESSION3", None) or getenv("STRING3", None)
STRING4 = getenv("STRING_SESSION4", None) or getenv("STRING4", None)
STRING5 = getenv("STRING_SESSION5", None) or getenv("STRING5", None)

# Custom Cookies URL (Optional)
COOKIES_URL = getenv("COOKIES_URL", None)

# Extra Bot Configurations
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/20641be20772719a7e289.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/20641be20772719a7e289.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/20641be20772719a7e289.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL ka URL invalid hai. Kripya http:// ya https:// ke sath likhein."
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHAT ka URL invalid hai. Kripya http:// ya https:// ke sath likhein."
        )
