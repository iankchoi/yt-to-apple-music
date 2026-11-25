import subprocess


def add_to_music(file_path: str) -> None:
    script = f'tell application "Music" to add POSIX file "{file_path}"'
    subprocess.run(["osascript", "-e", script], check=True)
