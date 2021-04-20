from flask import Flask,request,render_template
from flask_socketio import SocketIO
import subprocess
import socket
from threading import Thread

app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello_world():
    cname = subprocess.getoutput("date /t")
    return render_template("HomePage1.html", cname=cname)

@app.route('/tech.html',methods=["GET"])
def tech():
    data=request.args.get("command")
    if("chat" in data):
        return render_template("chat.html")
    elif(("Hadoop" in data) or ("hadoop" in data)):
        AccessKey = request.args.get("commands")
        SecretKey = request.args.get("commandss")
        return render_template("Hadoop_Main.html")
    elif("AWS" in data):
        return render_template("AWS_Main.html")
    else:
        return render_template("tech.html", mydata = subprocess.getoutput(data))

@app.route('/HadoopOutput', methods=["GET"])
def hadoop():
    command = request.args.get("command1")
    return render_template("Hadoop_output.html", command1=command)


@app.route('/User_loged_IN.html', methods=["GET"])
def user_logged():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("msg")

    cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "192.168.118.143"
    port = 2222

    cs.connect((ip,port))
    while True:
        def send_data():
                cs.sendall(name.encode())
    while True:
        def recv_data():
            while True:
                data = cs.recv(1000)
                print(data.decode())
    t=Thread(target=recv_data)
    t.start()
    send_data()
    cs.close()
    return render_template("User_loged_IN.html", myname=name, myemail=email)

@app.route("/AWS-Main1.html", methods=["GET"])
def aws():
    Accesskey = request.args.get("commands")
    SecretKey = request.args.get("commandss")
    return render_template("AWS_Main1.html", Acesskeys=Accesskey, SecretKeys=SecretKey, cname=cname)

