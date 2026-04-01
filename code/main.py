from CONFIG import SETTINGS
import displayManager
import identifier
import asyncio
import deezer
import random
import funcs
import time
import sql
import os

funcs.logo()

baseDir = os.path.dirname(os.path.abspath(__file__))
offlinePath = os.path.join(baseDir, "offline")

displayManager.initScreen()

if funcs.hasInternet():
    asyncio.run(sql.init())
else:
    print("No internet, database initialization failed!")

if SETTINGS["GENERAL"]["testing"]:

    print("Testing, will not listen only display webage!")
    songs = asyncio.run(sql.get(6))
    displayManager.update(songs, "Testing")
    while True:
        time.sleep(60)
        songs = asyncio.run(sql.get(6))
        displayManager.update(songs, "Testing")

else:

    while True:
        try:
            if funcs.hasInternet():

                displayManager.mode = "list"
                
                if len(os.listdir(offlinePath)) > 0:
                    print("Syncing offline songs...")

                    songs = asyncio.run(sql.get(6))
                    displayManager.update(songs, "Syncing")

                    for file in os.listdir(offlinePath):
                        if file.endswith(".wav"):
                            asyncio.run(sql.write(identifier.sync(path=f"{offlinePath}/{file}")))
                        time.sleep(random.randint(
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"],
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"]+2)
                        )
                    print("Finished syncing!")

                asyncio.run(sql.write(identifier.record()))

                if identifier.songPlaying and len(identifier.lastSong) > 0:
                    if displayManager.displayedSong != identifier.lastSong["title"]:
                        if deezer.getAlbumCover(identifier.lastSong["artist"], identifier.lastSong["title"]):

                            displayManager.mode = "music"
                            songs = asyncio.run(sql.get(6))
                            displayManager.update(songs, "Idle")

                elif not identifier.songPlaying:

                    displayManager.mode = "list"
                    songs = asyncio.run(sql.get(6))
                    displayManager.update(songs, "Idle")

                else:
                    songs = asyncio.run(sql.get(6))
                    displayManager.update(songs, "Idle")
                    
            else:
                print("Using offline mode as user hasn't got internet!")

                identifier.record(internet=False)
                if displayManager.mode == "list":
                    songs = asyncio.run(sql.get(6))
                    displayManager.update(songs, "Idle")
                else:
                    displayManager.mode == "Error"
                    displayManager.update({}, "Error")

        except Exception as e:
            print(e)
            
            if funcs.hasInternet():
                displayManager.mode = "list"
                songs = asyncio.run(sql.get(6))
                displayManager.update(songs, "Error")
            else:
                if displayManager.mode == "list":
                    displayManager.update(displayManager.lastList, "Error")
                else:
                    displayManager.mode == "Error"
                    displayManager.update({}, "Error")

        sleepTime = random.randint(SETTINGS["IDENTIFIACTION"]["inbetween time"]-10,SETTINGS["IDENTIFIACTION"]["inbetween time"]+10)

        print(f"Done cycle, waiting {sleepTime} seconds for next cycle!")
        time.sleep(sleepTime)