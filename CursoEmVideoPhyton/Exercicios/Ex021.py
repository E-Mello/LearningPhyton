# Crie um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pydub import AudioSegment
from pydub.playback import play
import pygame


def play_audio(filename):
    pygame.mixer.init(frequency=44100, size=-16, channels=2)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the playback speed


# Main program
if __name__ == "__main__":
    # Replace with the path to your MP3 file
    mp3_file = "your_song.mp3"
    play_audio(mp3_file)


# pygame.init()
# pygame.mixer.music.load('your_song.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()
