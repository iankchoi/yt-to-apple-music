import subprocess
from pathlib import Path


def download_audio(url: str, output_path: str) -> None:
    output_template = str(Path(output_path).with_suffix(".%(ext)s"))

    subprocess.run(
        ["yt-dlp", "-x", "--audio-format", "mp3", "-o", output_template, url],
        check=True,
    )


if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=CeA92xqw-QI", "/Users/ianchoi/Desktop/YT to Apple Music/scratch/test2.mp3")
