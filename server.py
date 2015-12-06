from flask import Flask
import twilio.twiml

MAIN_STRING = ("Hello. We are working on the ninth avenue side of " +
    "the fourth floor and the lights have turned off. Could you please " +
    "turn them on? Thank you. Hello. We are working on the ninth avenue " +
    "side of the fourth floor and the lights have turned off. Could you " +
    "please turn them on? Thank you.")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say(" ".join([MAIN_STRING]*5))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
