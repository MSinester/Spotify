from flask import Flask, render_template, request, flash
from config.db import mydb
from spotify import search_spotify

app = Flask(__name__)
app.secret_key = 'Spotify_search_music'


@app.route('/', methods=['GET', 'POST'])
def spotify_music():
    if request.method == 'POST':
        q = request.form['q'].lower()
        if len(q) == 0:
            flash('Please, complete the fields')
        else:
            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM tracks WHERE song LIKE '{q}';")
            result = cursor.fetchall()
            cursor.close()
            try:
                if len(result) == 0:
                    id_track, name_track, artist, spotify_track, image_track = search_spotify(q)
                    cursor = mydb.cursor()
                    cursor.execute(f"INSERT INTO tracks (id, song, artist, href_spotify, image) VALUES "
                                   f"('{id_track}', '{name_track.lower()}', '{artist}', '{spotify_track}', '{image_track}');")
                    mydb.commit()
                    cursor.close()
                    flash(f'https://open.spotify.com/embed/track/{id_track}')

                else:
                    cursor = mydb.cursor()
                    cursor.execute(f"SELECT * FROM tracks WHERE song LIKE '%{q}%';")
                    result = cursor.fetchall()
                    cursor.close()
                    flash(f'https://open.spotify.com/embed/track/{result[0][0]}')
                    flash('DB')

            except:
                flash('No found')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
