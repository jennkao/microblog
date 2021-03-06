from app import app, db
from flask_login import LoginManager, UserMixin
from hashlib import md5

lm = LoginManager(app)

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(64), nullable=False, unique=True)
  nickname = db.Column(db.String(64), nullable=False)
  email = db.Column(db.String(64), nullable=True)
  posts = db.relationship('Post', backref='author', lazy='dynamic')
  about_me = db.Column(db.String(140))
  last_seen = db.Column(db.DateTime)

  def avatar(self, size):
    return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

  def __repr__(self):
    return '<User %r>' % (self.nickname)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(140))
  timestamp = db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __repr__(self):
    return '<Post %r>' % (self.body)

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))