"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import InputRequired, Length, ValidationError


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name",
                       validators=[InputRequired(message="Playlist name cannot be empty!"), Length(min=1, message="Playlist name cannot be empty!")])
    description = TextAreaField ("Description",
                                 validators=[InputRequired(), Length(min=5, max=500)])
    
    def validate_name(self, field):
        if not field.data.strip():
            raise ValidationError("Playlist name cannot be just spaces!")

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title",
                        validators=[InputRequired(message="Playlist name cannot be empty!"), Length(min=1, max=100)])
    artist = StringField("Artist Title",
                        validators=[InputRequired(), Length(min=1, message="Playlist name cannot be empty!")])
    
    def validate_artist(self, field):
        if not field.data.strip():
            raise ValidationError("Playlist name cannot be just spaces!")

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', validators= [InputRequired()], coerce=int)
