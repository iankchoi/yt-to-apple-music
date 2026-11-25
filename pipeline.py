import os
import re

from download import download_audio
from tag import tag_mp3
from music import add_to_music

DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")


def _safe_filename(name: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9 _-]", "", name).strip()
    return cleaned or "untitled"


def add_song(url: str, song_name: str, artist: str, album: str, cover_art_path: str) -> str:
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    mp3_path = os.path.join(DOWNLOAD_DIR, f"{_safe_filename(song_name)}.mp3")

    download_audio(url, mp3_path)
    tag_mp3(mp3_path, song_name, artist, album, cover_art_path)
    add_to_music(mp3_path)

    return mp3_path
