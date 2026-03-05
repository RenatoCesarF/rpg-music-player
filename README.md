# RPG Music Player
<img width="596" height="348" alt="Screenshot 2026-03-05 at 15 18 31" src="https://github.com/user-attachments/assets/cef3d07f-b074-478a-b650-1f4c727cde3e" />

## Description
This is a simple RPG music player made with Python and pygame. The idea is to separate music into mood folders that can be played easily

> The musics folder should be put in `./musics` besides the main.py file, each folder is a playlist.

## Features

- Play random music from a folder (playlist)
- Play next music from playlist when current music finishes
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



