from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form




@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0


    message = ""
    if 'messages' in session:
        session['messages'].append(message)
    else:
        session['messages'] = []

    if 'moves' in session:
        pass
    else:
        session['moves'] = 0

    return render_template("index.html", message=message)


@app.route('/process_money', methods=["POST"])
def process_money():
    session['location'] = request.form['location']
    print('process money', 'location: ' , session['location'])

    if 'moves' in session:
        session['moves'] += 1
    else:
        session['moves'] = 0

    if session['location'] == 'farm':
        randGold = random.randint(10,20)
        message = "<li class='text-success'>You went to the farm and earned " + str(randGold) + " gold at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
        session['messages'].append(message)

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)

    elif session['location'] == 'cave':
        randGold = random.randint(5,10)
        message = "<li class='text-success'>You went to the cave and found " + str(randGold) + " gold at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
        session['messages'].append(message)

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)


    elif session['location'] == 'house':
        randGold = random.randint(2,5)
        message = "<li class='text-success'>You went to the house and stole " + str(randGold) + " gold at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
        session['messages'].append(message)

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)


    elif session['location'] == 'casino':
        randGold = random.randint(-50,50)
        if randGold > 0:
            message = "<li class='text-success'>You went to the casino and won " + str(randGold) + " gold at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
            session['messages'].append(message)
        elif randGold == 0:
            message = "<li class='text-info'>You went to the casino and broke even at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
            session['messages'].append(message)
        else:
            message = "<li class='text-danger'>You went to the casino and lost " + str(randGold) + " gold at " + datetime.strftime(datetime.now(), '%I:%M%p %m %d %Y  ') + "</li>"
            session['messages'].append(message)

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)
    
    
    return redirect("/")

@app.route('/destroy_session')
def destroy():

    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)