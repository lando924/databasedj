"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name",
                       validators=[InputRequired(), Length(min=1, max=100)])
    description = TextAreaField ("Description",
                                 validators=[InputRequired(), Length(min=5, max=500)])

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title",
                        validators=[InputRequired(), Length(min=1, max=100)])
    artist = StringField("Artist Title",
                        validators=[InputRequired(), Length(min=1, max=100)])
    

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', validators= [InputRequired()], coerce=int)
