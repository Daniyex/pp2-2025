import pygame
import os

pygame.init()
pygame.mixer.init()

KEY_PLAY_PAUSE = pygame.K_SPACE
KEY_STOP = pygame.K_s
KEY_NEXT = pygame.K_n
KEY_PREVIOUS = pygame.K_p

MUSIC_FOLDER = r"C:\Users\user\Music"
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_track_index = 0

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Pygame Music Player")

def play_music(track_index):
    track_path = os.path.join(MUSIC_FOLDER, tracks[track_index])
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()
    print(f"Playing: {tracks[track_index]}")

if not tracks:
    print("No music files found in the directory!")
    exit()

play_music(current_track_index)

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == KEY_PLAY_PAUSE:
                if pygame.mixer.music.get_busy() and not paused:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Paused")
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resumed")

            elif event.key == KEY_STOP:
                pygame.mixer.music.stop()
                paused = False
                print("Stopped")

            elif event.key == KEY_NEXT:
                current_track_index = (current_track_index + 1) % len(tracks)
                paused = False
                play_music(current_track_index)

            elif event.key == KEY_PREVIOUS:
                current_track_index = (current_track_index - 1) % len(tracks)
                paused = False
                play_music(current_track_index)

pygame.quit()
