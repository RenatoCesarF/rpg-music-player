# RPG Music Player

<img width="593" height="344" alt="Screenshot 2026-03-05 at 15 07 51" src="https://github.com/user-attachments/assets/a7cde1c1-5dd5-4ad1-a616-c171e1e9e3fd" />

## Description

This is a simple RPG music player made with Python and pygame.

> The musics folder should be put in `./musics` besides the main.py file, each folder is a playlist.

## Features

- Play random music from a folder (playlist)
- Display cover art if available
- Skip music
- Skip music time (15s, -15s)

## Installation

1. Clone the repository
2. Create a virtual environment with `python -m venv venv`
3. Activate the virtual environment with `source venv/bin/activate`
4. Install the required packages with `pip install -r requirements.txt`
5. Run the main script with `python main.py`

## Usage
1. Create a `./musics` folder
2. Create any folder there, to use as a mood playlist
3. Put the musics in the folders
4. Run the Program

## Controllers

| Key   | Action          |
| ----- | --------------- |
| Space | Play/Pause      |
| n     | Skip music      |
| h     | Skip -15s       |
| l     | Skip 15s        |
| 0...9 | Select Playlist |



