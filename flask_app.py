from flask import Flask, render_template
#from flask_ask import Ask, statement, question, session
#import requests
#import urllib
#import re
#from pyvirtualdisplay import Display
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def anim():
    anim_var = 10
    return render_template("anim.html", value = anim_var)

'''

def move_fn(move):
    print (move);
    x = 1
    resp = "OK"
    if x == 1:
        return move
    else:
        return resp



if __name__ == '__main__':
    app.run(debug=True)
'''
'''
ask = Ask(app, "/alexa")

@ask.launch
def new_ask():
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome) \
        .reprompt(reprompt)

@ask.intent('GameMove')
def launchMove(move):
    if (move is None):
        reprompt_move = render_template("reprompt_move")
        return question(reprompt_move)
    else:
        latest_resp = move_fn(move)
        return statement(latest_resp)
'''