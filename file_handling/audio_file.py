import vlc
# pip install python-vlc
import os

if os.path.exists(r'C:\DeeYarr.mp3'):
    player = vlc.MediaPlayer(r'C:\DeeYarr.mp3')
    player.play()
    print("Playing mp3 file...")

else:
    print("File does not exist.")
