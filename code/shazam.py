from CONFIG import SETTINGS
import urllib.parse
import aiohttp
import json

async def identify(path:str = "temp.wav", raw:bool = False):
    
    with open(path, "rb") as f:
        data = f.read()

    headers = {
        "key": SETTINGS["GENERAL"]["shared secret"],
        "Content-Type": "application/octet-stream"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{SETTINGS['GENERAL']['server url']}/identify",
            data=data,
            headers=headers
        ) as resp:
            result = await resp.json()

    try:
        if raw:
            return result
        elif len(result["matches"]) == 0:
            print("Song not found!")
            return None
    except Exception as e:
        print("Couldn't find song, error: ", e)
        return None
    track = result["track"]
    released = 0000

    try:
        released = track["sections"][0]["metadata"][2]["text"]
    except:
        print("Couldn't retrieve year of release!")

    data = {
        "title": track["title"],
        "artist": track["subtitle"],
        "album": track["sections"][0]["metadata"][0]["text"],
        "released": released,
        "link": {
            "shazam": track["share"]["href"],
            "spotify": f"https://open.spotify.com/search/{urllib.parse.quote(track['title'] + ' ' + track['subtitle'])}"
        }
    }
    return data