import os
import tempfile

from flask import Flask, request, render_template_string

from pipeline import add_song

app = Flask(__name__)

FORM_HTML = """
<!doctype html>
<title>YouTube to Apple Music</title>
<h1>Add a song to Apple Music</h1>
{% if message %}<p><strong>{{ message }}</strong></p>{% endif %}
<form method="post" enctype="multipart/form-data">
  <label>YouTube link:<br><input type="text" name="url" size="50" required></label><br><br>
  <label>Song name:<br><input type="text" name="song_name" required></label><br><br>
  <label>Artist:<br><input type="text" name="artist" required></label><br><br>
  <label>Album:<br><input type="text" name="album" required></label><br><br>
  <label>Cover art:<br><input type="file" name="cover_art" accept="image/*" required></label><br><br>
  <button type="submit">Add to Apple Music</button>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        url = request.form["url"]
        song_name = request.form["song_name"]
        artist = request.form["artist"]
        album = request.form["album"]
        cover_art_file = request.files["cover_art"]

        suffix = os.path.splitext(cover_art_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            cover_art_path = tmp.name
        cover_art_file.save(cover_art_path)

        try:
            add_song(url, song_name, artist, album, cover_art_path)
            message = f"Added \"{song_name}\" to Apple Music."
        except Exception as e:
            message = f"Something went wrong: {e}"
        finally:
            os.remove(cover_art_path)

    return render_template_string(FORM_HTML, message=message)


if __name__ == "__main__":
    app.run(debug=True)
