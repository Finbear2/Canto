from CONFIG import SETTINGS
import displayManager
import identifier
import threading
import deezer
import random
import funcs
import time
import sql
import web
import os

funcs.logo()

sql.init()
threading.Thread(target=web.app.run, kwargs={"host": SETTINGS["WEB UI"]["host"], "port": SETTINGS["WEB UI"]["port"]}, daemon=True).start()

baseDir = os.path.dirname(os.path.abspath(__file__))
offlinePath = os.path.join(baseDir, "offline")

displayManager.initScreen()

time.sleep(20)

if SETTINGS["GENERAL"]["testing"]:

    print("Testing, will not listen only display wepage!")
    displayManager.update(sql.get(6), "Testing")
    while True:
        pass

else:

    while True:
        try:
            if funcs.hasInternet():
                
                if len(os.listdir(offlinePath)) > 0:
                    print("Syncing offline songs...")

                    displayManager.update(sql.get(6), "Syncing")

                    for file in os.listdir(offlinePath):
                        if file.endswith(".wav"):
                            sql.write(identifier.sync(path=f"{offlinePath}/{file}"))
                        time.sleep(random.randint(
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"],
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"]+2)
                        )
                    print("Finished syncing!")

                sql.write(identifier.record())

                if identifier.songPlaying and len(identifier.lastSong) > 0:
                    if displayManager.displayedSong != identifier.lastSong["title"]:
                        if deezer.getAlbumCover(identifier.lastSong["artist"], identifier.lastSong["title"]):

                            displayManager.mode = "music"
                            displayManager.update(sql.get(6), "Idle")

                elif not identifier.songPlaying:

                    displayManager.mode = "list"
                    displayManager.update(sql.get(6), "Idle")

                else:
                    displayManager.update(sql.get(6), "Idle")
                    
            else:

                print("Using offline mode as user hasn't got internet!")
                sql.write(identifier.record(internet=False))
                displayManager.mode = "list"
                displayManager.update(sql.get(6), "Idle")

        except Exception as e:
            print(e)
            
            displayManager.mode = "list"
            displayManager.update(sql.get(6), "Idle")

        sleepTime = random.randint(SETTINGS["IDENTIFIACTION"]["inbetween time"]-10,SETTINGS["IDENTIFIACTION"]["inbetween time"]+10)

        print(f"Done cycle, waiting {sleepTime} seconds for next cycle!")
        time.sleep(sleepTime)