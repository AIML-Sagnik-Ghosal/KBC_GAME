from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests as r
import json as j
import random as ra
from threading import Timer
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
CORS(app)
remaining_time = 30
e_no=0
def countdown():
    global remaining_time, timer
    if remaining_time > 0:
        remaining_time -= 1
        timer = Timer(1, countdown)
        timer.start()
timer = Timer(1, countdown)

@app.route("/done/<data>/<no>", methods=['GET', 'POST'])
def done(data, no):
			global timer
			global e_no
			timer.cancel()
			if correct(no, data):
				if order[1] == 1:
					order[1] = 0
					e_no+=2
					return redirect(url_for('index', no=int(no)+2))
				else:
					e_no+=1
					return redirect(url_for('index',no=int(no)+1))
			else:
				kbc_data[int(no)]['correctAnswer']=''
				take_kbc_data()
				e_no=0
				return redirect(url_for('index',no=0))
	
@app.route("/<no>",methods=['GET','POST'])
def index(no):
    global e_no
    no=eval(no)
    if no==e_no:
        ques=question(no)
        p=price(no)
        global timer
        timer.cancel()
        global remaining_time
        remaining_time = 30
        timer = Timer(1, countdown)
        timer.start()
        return render_template("index.html",q=ques,os=options(no),price=p,no=no)
    else:
        return redirect(url_for('index',no=0))
@app.route('/time')
def get_time():
    global remaining_time
    return str(remaining_time)
@app.route("/h1/<no>",methods=['GET','POST'])
def help1(no):
	if help[0]:
		no=eval(no)
		ques=question(no)
		p=price(no)
		help[0]=0
		return render_template("index.html",q=ques,os=shuffle(order[0],kbc_data[int(no)]['correctAnswer']),price=p,no=no)
	else:
		no=eval(no)
		ques=question(no)
		p=price(no)
		return render_template("index.html",q=ques,os=order[0],price=p,no=no)
@app.route("/h2/<no>",methods=['GET','POST'])
def help2(no):
	if help[1]:
		no=eval(no)
		ques=question(no)
		p=price(no)
		help[1]=0
		if not ra.randint(0,9):
				o=shuffle(order[0],kbc_data[int(no)]['correctAnswer'])
				print(o,'1')
				o=[o[i] if o[i]!=kbc_data[int(no)]['correctAnswer'] else '' for i in range(4)]
		else:
				o=shuffle(order[0],kbc_data[int(no)]['correctAnswer'])
				print(o,'2')
				o=[o[i] if o[i]==kbc_data[int(no)]['correctAnswer'] else '' for i in range(4)]
		print(o,kbc_data[int(no)]['correctAnswer'])
		return render_template("index.html",q=ques,os=o,price=p,no=no)
	else:
		no=eval(no)
		ques=question(no)
		p=price(no)
		return render_template("index.html",q=ques,os=order[0],price=p,no=no)
@app.route("/h3/<no>",methods=['GET','POST'])
def help3(no):
	if help[2]:
		order[1]=1
		no=eval(no)
		ques=question(no)
		p=price(no)
		help[2]=0
		return render_template("index.html",q=ques,os=order[0],price=p,no=no)
	else:
		no=eval(no)
		ques=question(no)
		p=price(no)
		return render_template("index.html",q=ques,os=order[0],price=p,no=no)
@app.route("/h4/<no>",methods=['GET','POST'])
def help4(no):
	if help[3]:
		no=eval(no)
		kbc_data[no]=kbc_data[19]
		help[3]=0
		return redirect(url_for('index',no=no))
	else:
		no=eval(no)
		ques=question(no)
		p=price(no)
		return render_template("index.html",q=ques,os=order[0],price=p,no=no)
@app.route("/",methods=['GET','POST'])
def home():
	global remaining_time
	remaining_time = 30
	global e_no
	e_no=0
	take_kbc_data()
	return redirect(url_for('index',no=0))
def price(no):
	return p[::-1][no]
def question(no):
	return kbc_data[no]['question']
def options(no):
	option=kbc_data[no]['incorrectAnswers']+[kbc_data[no]['correctAnswer']]
	ra.shuffle(option)
	order[0]=option
	return option
def correct(no,n):
	if n==kbc_data[int(no)]['correctAnswer']:
		return True
	return False
def shuffle(a,c):
	i=[j for j in range(len(a))]
	i.remove(a.index(c))
	for j in range(len(a)//2):
		x=ra.choice(i)
		a[x]=''
		i.remove(x)
	order[0]=a
	return a
def take_kbc_data():
	t=r.get("https://the-trivia-api.com/api/questions?categories=film_and_tv,arts_and_literature,general_knowledge,science,sport_and_leisure&limit=20&difficulty=easy")
	global kbc_data
	kbc_data=j.loads(t.text)
	global order
	order=[0,0]
	global help
	help=[1,1,1,1]
	global p
	p=['7 Crore','₹2.5 Crore','₹1 Crore','₹50,00,000/-','₹25,00,000/-','₹12,50,000/-','₹6,40,000/-','₹3,20,000/-','₹1,60,000','₹80,000/-','₹40,000/-','₹20,000/-',
	'₹10,000/-','₹5,000/-','₹2,500/-','₹1,000/-']
def take_kbc_data1():
	global kbc_data
	kbc_data=pd.read_excel("kbc.xlsx")
	global order
	order=[0,0]
	global help
	help=[1,1,1,1]
	global p
	p=['7 Crore','₹2.5 Crore','₹1 Crore','₹50,00,000/-','₹25,00,000/-','₹12,50,000/-','₹6,40,000/-','₹3,20,000/-','₹1,60,000','₹80,000/-','₹40,000/-','₹20,000/-',
	'₹10,000/-','₹5,000/-','₹2,500/-','₹1,000/-']
if __name__ == "__main__":
	countdown()
	app.run(debug=False)