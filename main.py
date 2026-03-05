import os
from datetime import datetime
import random
import sys
import pygame
import vlc

from urllib.parse import urlparse, unquote

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 350
RIGHT_MARGIN = 10
TOP_MARGIN = 10
LEFT_MARGIN = 15 

base_folder_dir = "../"
folders_to_ignore = [ "Pythonscript" ]


player = vlc.MediaPlayer()

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RPG Music Player")

    folders = [
        f for f in os.listdir(base_folder_dir)
        if os.path.isdir(os.path.join(base_folder_dir, f)) and f not in folders_to_ignore
    ]

    running = True
    last_selected_playlist = {}
    playing_music = {}

    clock.tick(1)

    while running:
        screen.fill((25, 25, 25))
        write(screen, "Pastas disponíveis:", (LEFT_MARGIN, TOP_MARGIN), (255, 255, 255))
        for i, folder in enumerate(folders):
            y_pos = TOP_MARGIN + 20 + i * 25
            write(screen, f"{str(i)} - {folder}", pos=(LEFT_MARGIN, y_pos), color=(255, 255, 255))
            if last_selected_playlist.get("index") == i:
                rect_surface = pygame.Surface((300, 25), pygame.SRCALPHA)
                rect_surface.fill((255, 255, 255, 80))

                screen.blit(rect_surface, (2, y_pos - 3))

        length = player.get_length()
        current = player.get_time()

        if length > 0 and current >= length:
            playing_music = play_random_music(last_selected_playlist.get("path"))

        if playing_music and playing_music.get("path") is not None:
            draw_current_music_cover(screen, playing_music)

            draw_current_music(screen, playing_music)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                player.pause()

            if event.key == pygame.K_n:
                player.set_time(player.get_length())

            if event.key == pygame.K_h:
                skip_time(-15)
            if event.key == pygame.K_l:
                skip_time(15)

            if pygame.K_0 <= event.key <= pygame.K_9:
                index = event.key - pygame.K_0

                if index >= len(folders):
                    continue

                folder_path = os.path.join(base_folder_dir, folders[index])
                last_selected_playlist = { "path": folder_path, "index": index}

                playing_music = play_random_music(folder_path)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def draw_current_music_cover(screen, playing_music):
    media = playing_music.get('media')
    if not media:
        return
    media.parse()  # carrega metadata

    art_url = media.get_meta(vlc.Meta.ArtworkURL)
    if not art_url:
        return

    path = unquote(urlparse(art_url).path)
    if not path:
        return
    cover = pygame.image.load(path).convert()
    cover = pygame.transform.scale(cover, (220,220))
    screen.blit(cover, (SCREEN_WIDTH - RIGHT_MARGIN - cover.get_width() - 20, TOP_MARGIN + 10 ))

def draw_current_music(screen, playing_music):
    write(screen, f"Tocando: {playing_music["path"].split("/")[-1]}", (LEFT_MARGIN, 280), (255, 255, 255))

    play_time_progress = 0
    if player.get_length() > 0:
        play_time_progress = player.get_time() / player.get_length()

    bar_width = (SCREEN_WIDTH - 20 - RIGHT_MARGIN) * play_time_progress
    pygame.draw.rect(screen, (105, 105, 105), (LEFT_MARGIN, 300, SCREEN_WIDTH - 20 - RIGHT_MARGIN, 10))
    pygame.draw.rect(screen, (255,255,255), (LEFT_MARGIN, 300, bar_width, 10))

    write(screen, f"Playtime: {time_lenght_format(player.get_length())}", (LEFT_MARGIN, 315), (255, 255, 255))


def time_lenght_format(time_length):
    seconds = time_length // 1000

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes}:{seconds:02d}"

def play_random_music(folder_path):
    music = get_random_music(folder_path)
    if not music:
        return None

    return play_music(music)

def skip_time(time):
    time_to_set = player.get_time() + time * 1000
    if time_to_set < 0:
        time_to_set = 0
    if time_to_set > player.get_length():
        time_to_set = player.get_length() - 100

    player.set_time(time_to_set)

def get_random_music(folder_path):
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".mp3", ".wav", ".ogg"))
    ]
    if not files:
        return None
    return os.path.join(folder_path, random.choice(files))


def play_music(path):
    global player
    player.stop()
    media = vlc.Media(path)
    player.set_media(media)
    player.play()
    return {'media': media, 'path': path}

def write(screen, text, pos, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

if __name__ == "__main__":
    main()
