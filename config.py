# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
ig_did=A324B809-5093-484F-BE2B-2B07A75CC984; csrftoken=IlVIehrImxQHRp159jq1y-; datr=czbiZ-cYaitbu4e2ls96zAfV; mid=Z-I2dAALAAGZ8vEqUuZDKCsUSlZc; ig_nrcb=1; wd=1536x367; dpr=1.25; ds_user_id=74127753671; sessionid=74127753671%3AxtfKhY01BS0bAS%3A19%3AAYfa5I8cjVGLK3IEP-m2LP3wOudaj54Ntuj2eFbVCw; rur="RVA\05474127753671\0541777974698:01f727829bf71b05483d8d44cf4965b0e3121b71d593ac37165a6c72fe56d05edaa47a6c
"""

YTUB_COOKIES = """
SID=g.a000wQjWJ-G5MxAPT-Ded76eh5DTPFtBXlL-AGYIKALpR943Z0Ee6Xqkc0APyIIMO2uXVHkEIAACgYKAUkSARISFQHGX2MiW4kuPAcVqH1zXKCG5C9F9RoVAUF8yKoCa_ZM4FOsG3mMw1ZPvpzu0076; __Secure-1PSIDTS=sidts-CjABjplskM-BftTz85R3aX3_HZrFcu8A1c-gNG8xbSWmGtdbSjH0WtZXwrNXuo1llHkQAA; __Secure-3PSIDTS=sidts-CjABjplskM-BftTz85R3aX3_HZrFcu8A1c-gNG8xbSWmGtdbSjH0WtZXwrNXuo1llHkQAA; __Secure-1PSID=g.a000wQjWJ-G5MxAPT-Ded76eh5DTPFtBXlL-AGYIKALpR943Z0EeT02jQQgHX8FHaGzRD2-OIAACgYKAdMSARISFQHGX2MiJCw8JuhBS7J4Fr-h_rAAEhoVAUF8yKo7E75m2ltx_nNI9s0j2Dg…J6ZGFybVVDRXlhSURQUmZVVDFiTjFzdkRhdXV2NldoRHI2MHdoTWlxOEdtUE9EN1VUY2hqbFZHVUdn; __Secure-ROLLOUT_TOKEN=CL38kZTo7PyFlQEQxd2ru6i2igMYz4D-xImMjQM%3D; YSC=lAQmGpzkl-0; ST-xuwub9=session_logininfo=AFmmF2swRAIgQ8Tj6pvgE_TggB2a411GfSRfTgYYiWpPuej_FdnMZtUCIAMGmFxBJoIcW57bYoQez4DKsGK3ky5IKmAvnmmjSGnE%3AQUQ3MjNmdzNMa0pVLXVGdmFKNWxMaEszUlhyOVhNVVdXZkMwejhNQ3RlelpQVGQ5WHZhSVFpa3BlSEFJUlBoNTFIRzJXSGhGQ2RGRkYxcDFRSlVjRGVGZXdDbjNYU01nUENrSjBlalJ6ZGFybVVDRXlhSURQUmZVVDFiTjFzdkRhdXV2NldoRHI2MHdoTWlxOEdtUE9EN1VUY2hqbFZHVUdn
"""

API_ID = int(getenv("API_ID", "28046715"))
API_HASH = getenv("API_HASH", "203a6455ceb4497e2b6347a14bc45df4")
BOT_TOKEN = getenv("BOT_TOKEN", "7046865433:AAF5CLYrQcwNpBwgitaKzSIap-7c52WNKHI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1231933846").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mxnufz:uDw4CvqYVJ0cDPNI@cluster0.di2hecx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4733927832")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001826519793"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "dafbc32dcebf6faf053d1a783c404d1f583488e4")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
