from omni_epd import displayfactory
from PIL import Image, ImageDraw
from datetime import datetime
import socket
import funcs

displayedSong = "None"
mode = "music"

def drawTopBar(draw:ImageDraw.Draw, status:str):
    

    if funcs.hasInternet():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # doesn't actually send anything, relax
        ip = s.getsockname()[0]
        s.close()

        draw.text((7, 2), f"WIFI-{ip}", fill=0)

    draw.text((163, 2), f"{datetime.now().strftime('%H:%M')}-{status}", fill=0)

    draw.line([(0,15), (250,15)], fill=0, width=1)

    return draw

def displaySong(draw:ImageDraw.Draw, songimformation:dict):
    return draw

def displayList(draw:ImageDraw.Draw):
    return draw

def update(songimformation:dict, status:str):

    # swap "omni_epd.mock" for "waveshare_epd.epd2in13_V2" when Pi arrives
    epd = displayfactory.load_display_driver("omni_epd.mock")

    epd.prepare()

    image = Image.new("1", (250, 122), 255)
    draw = ImageDraw.Draw(image)

    draw = drawTopBar(draw, status)

    if mode == "music":
        draw = displaySong(draw, songimformation)
    elif mode == "list":
        draw = displayList(draw)

    epd.display(image)
    epd.close()
    

if __name__ == "__main__":
    # swap "omni_epd.mock" for "waveshare_epd.epd2in13_V2" when Pi arrives
    epd = displayfactory.load_display_driver("omni_epd.mock")

    epd.prepare()

    image = Image.new("1", (250, 122), 255)
    draw = ImageDraw.Draw(image)

    draw = drawTopBar(draw, True)

    epd.display(image)
    epd.close()
