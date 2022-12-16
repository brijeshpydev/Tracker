from app import app
from app import db

    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String, nullable=False, unique=True)
    user_isp = db.Column(db.String, nullable=False)
    browser_info = db.Column(db.String)
    timezone = db.Column(db.String)
    
    def __repr__(self):
        return "<user_ip %r >" % self.user_ip 
    
class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False)
    browser_info = db.Column(db.String)
    timezone = db.Column(db.String)
    
    def __repr__(self):
        return "<user_ip %r >" % self.user_ip

class ClientInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False)
    client_info = db.Column(db.String, nullable=False)
    client_ip = db.Column(db.String)
    client_user_agent = db.Column(db.String)
    
    def __repr__(self):
        return "<client_ip %r >" % self.client_ip
    