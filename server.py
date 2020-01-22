from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form




@app.route('/')
def index():
    message = "<ul><li>Hello</li></ul>"
    return render_template("index.html", message=message)


@app.route('/process_money', methods=["POST"])
def process_money():
    session['location'] = request.form['location']
    print('process money', 'location: ' , session['location'])
    

    if session['location'] == 'farm':
        randGold = random.randint(10,20)
        message = "You went to the farm and got " + str(randGold) + " gold"

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)

    elif session['location'] == 'cave':
        randGold = random.randint(5,10)
        message = "You went to the cave and got " + str(randGold) + " gold"

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)


    elif session['location'] == 'house':
        randGold = random.randint(2,5)
        message = "You went to the house and got " + str(randGold) + " gold"

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)


    elif session['location'] == 'casino':
        randGold = random.randint(-50,50)
        if randGold > 0:
            message = "You went to the casino and got " + str(randGold) + " gold"
        elif randGold == 0:
            message = "You went to the casino and broke even!"
        else:
            message = "You went to the casino and lost " + str(randGold) + " gold"

        if 'gold' in session:
            session['gold'] += int(randGold)
        else:
            session['gold'] = int(randGold)
    
    
    return render_template("index.html", message=message)

@app.route('/destroy_session')
def destroy():

    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)