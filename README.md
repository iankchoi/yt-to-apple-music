# YouTube to Apple Music

A personal tool that takes a YouTube link plus song metadata and adds the song directly into your Apple Music library, in one step.

Fill in a form with a YouTube link, song name, artist, album, and cover art. Submitting it:

1. Downloads the audio from the link and converts it to mp3 (`yt-dlp` + `ffmpeg`)
2. Writes the song name, artist, album, and cover art into the mp3's ID3 tags (`mutagen`)
3. Adds the file to your Apple Music library (AppleScript via `osascript`)

## Scope

This only runs locally on macOS. AppleScript can only control apps running on the same machine, so this cannot be hosted remotely. It's built for personal use — no batch/playlist imports, no automatic metadata lookup.

## Requirements

- macOS, with the Music app
- [Homebrew](https://brew.sh)
- Python 3

## Setup

```bash
brew install yt-dlp ffmpeg

python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Running it

```bash
./venv/bin/python3 app.py
```

Then open `http://127.0.0.1:5000` in your browser, fill in the form, and submit.

## Project layout

- `download.py` — downloads and converts YouTube audio to mp3 (`yt-dlp`)
- `tag.py` — writes song name/artist/album/cover art into the mp3's ID3 tags (`mutagen`)
- `music.py` — adds a file to the Apple Music library (AppleScript via `osascript`)
- `pipeline.py` — chains the three steps above into one `add_song(...)` call
- `app.py` — the Flask form that drives `pipeline.add_song`

Downloaded mp3s are saved to a local `downloads/` folder (not tracked in git).
