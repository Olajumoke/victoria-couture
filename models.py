from app import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    firstname = db.Column(db.String(64), index=False, unique=False, nullable=False)
    lastname = db.Column(db.String(64), index=False, unique=False, nullable=False)

    def __init__(self, username, email, created, admin, firstname, lastname):
        self.username = username
        self.email = email
        self.created = created
        self.admin = admin
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return '<User {}>'.format(self.username)