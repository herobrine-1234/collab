from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC46ac61224e60d3a2414e7c9830ece8a3'
    TWILIO_SYNC_SERVICE_SID = 'IS5293b6fff6a1a30ee07914e4861d971f'
    TWILIO_API_KEY = 'SK4d595437a799575ee415ed617382f00f'
    TWILIO_API_SECRET = 'EVloGd3Pu3Y0hWpWAxoDX8S4UWtyqw9Z'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

