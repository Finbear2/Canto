SETTINGS = {
    "GENERAL": {
        "testing": False,
    },
    "WEB UI": {
        "host": "0.0.0.0", 
        "port": 5000,
    },
    "IDENTIFIACTION": {
        "inbetween time": 60, # Time inbetween each recording in seconds
        "sync inbetween time": 5, # Time inbetween each recording during offline syncing in seconds
        "noise threshold": 40, # The volume a noise must be above to be regonised dault is 3000
        "sample rate": 44100, # The sample rate for recordings
        "sample size": 20, # The zise of each recording in settings
    },
    "SQL": {
        "database path": "/home/fin/dev/projects/null/code/database/songs.db",
    },
    "DISPLAY": {
        "connected": False,
        "waveshare drivers": "waveshare_epd.epd2in13_V3",
        "album cover dithering type": "atkinson",
    }
}