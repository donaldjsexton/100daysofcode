import os
import time
import wave

def play():
     audio = wave.open('audio.wav', 'rb')
    
while True:
        print("PyAmp")
        print("\nPress 1 to Play")
        print("Press 2 to Stop")
        print("\nPress anything else to see the menu again")

        playButton = input("Please make a choice: ")
        if playButton == "1":
            print("Playing audio...")
            time.sleep(211)
            
        elif playButton == "2":
            print("Stopping audio...")
            break
        
        else:
            os.system("clear")

play()