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

sql.init()
threading.Thread(target=web.app.run, kwargs={"host": SETTINGS["WEB UI"]["host"], "port": SETTINGS["WEB UI"]["port"]}, daemon=True).start()

testing=False

if testing:
    print("Testing, will not listen only display wepage!")
    displayManager.update(sql.get(6), "Testing")


if not testing:
    while True:
<<<<<<< HEAD
        try:
            if funcs.hasInternet():
                
                if len(os.listdir("offline")) > 0:
                    print("Syncing offline songs...")
=======
        if funcs.hasInternet():
            
            if len(os.listdir("offline")) > 0:
                print("Syncing offline songs...")
>>>>>>> be05049a09e4ac40f91b0633756e573363878234

                    displayManager.update(sql.get(6), "Syncing")

                    for file in os.listdir("offline"):
                        if file.endswith(".wav"):
                            sql.write(identifier.sync(path=f"offline/{file}"))
                        time.sleep(random.randint(
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"],
                            SETTINGS["IDENTIFIACTION"]["sync inbetween time"]+2)
                        )
                    print("Finished syncing!")

                sql.write(identifier.record())

                if identifier.songPlaying and len(identifier.lastSong) > 0:
                    if displayManager.displayedSong != identifier.lastSong["title"]:
                        if deezer.getAlbumCover(identifier.lastSong["artist"], identifier.lastSong["title"]):

<<<<<<< HEAD
                            displayManager.mode = "music"
                            displayManager.update(sql.get(6), "Idle")
=======
                        displayManager.mode = "music"
                        displayManager.update(sql.get(6), "Idle")
>>>>>>> be05049a09e4ac40f91b0633756e573363878234

                elif not identifier.songPlaying:

<<<<<<< HEAD
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
            
=======
                displayManager.mode = "list"
                displayManager.update(sql.get(6), "Idle")
                
        else:

            print("Using offline mode as user hasn't got internet!")
            sql.write(identifier.record(internet=False))
>>>>>>> be05049a09e4ac40f91b0633756e573363878234
            displayManager.mode = "list"
            displayManager.update(sql.get(6), "Idle")

        sleepTime = random.randint(SETTINGS["IDENTIFIACTION"]["inbetween time"]-10,SETTINGS["IDENTIFIACTION"]["inbetween time"]+10)

        print(f"Done cycle, waiting {sleepTime} seconds for next cycle!")
        time.sleep(sleepTime)