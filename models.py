from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Create User"""
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    
    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register user, hash password"""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.add(user)
        db.session.commit()
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Validate user and password.

        Return user if valid
        """
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, first_name={self.first_name}, last_name{self.last_name})"
    

class Feedback(db.Model):

    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    user = db.relationship('User', backref="feedbacks", cascade="all, delete")