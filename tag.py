import mimetypes

from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC


def tag_mp3(file_path: str, song_name: str, artist: str, album: str, cover_art_path: str) -> None:
    audio = ID3(file_path)

    audio.add(TIT2(encoding=3, text=song_name))
    audio.add(TPE1(encoding=3, text=artist))
    audio.add(TALB(encoding=3, text=album))

    mime_type = mimetypes.guess_type(cover_art_path)[0]
    with open(cover_art_path, "rb") as f:
        image_bytes = f.read()

    audio.add(APIC(encoding=3, mime=mime_type, type=3, desc="Cover", data=image_bytes))

    audio.save(file_path)
