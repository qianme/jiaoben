from flask import Flask,make_response
import json


app = Flask(__name__)#当前文件位置

@app.route("/",methods=["get"])
def main():
    return "要努力啊，不要再摆烂了\n再摆烂你宝就要走了，真走了怎么办"

#1debug 模式




if __name__=="__main__":
    app.run(debug=True)