import urllib.parse, urllib.request
from pyxelate import Pyx, Pal
from CONFIG import SETTINGS
from skimage import io
import requests

def getAlbumCover(artist, song):
    print("\ngetting album cover from Deezer API")
    response = requests.get(f"https://api.deezer.com/search?q={urllib.parse.quote(artist + ' ' + song)}").json()

    data = response["data"][0]
    coverURL = data["album"]["cover_medium"]

    print(f"downloading cover '{coverURL}'...")
    try:
        urllib.request.urlretrieve(coverURL, "resources/cover.png")
        print("Downloaded album cover!")
    except:
        print("Couldn't download album cover!")
        return False;

    print("Turning album cover into pixel art image")
    image = io.imread("resources/cover.png")

    pallete = Pal.from_rgb([[255, 255, 255], [0, 0, 0]])
    pyx = Pyx(
        height=SETTINGS["DISPLAY"]["album cover size"],
        width=SETTINGS["DISPLAY"]["album cover size"],
        palette=pallete,
        dither=SETTINGS["DISPLAY"]["album cover dithering type"]
    )

    pyx.fit(image)

    newImage = pyx.transform(image)
    io.imsave("resources/cover.png", newImage)

    print("album cover now pixel art!")
    return True;

if __name__ == "__main__":
    getAlbumCover("daft punk", "harder better")