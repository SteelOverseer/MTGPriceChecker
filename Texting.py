from flask import Flask, request, redirect, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
import CardSearch

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    cardParams = request.form['Body'].split(",")
    cardName =  cardParams[0]
    setName = cardParams[1]
    priceType =  cardParams[2]
    
    priceObj = CardSearch.getCardPrice(setName, cardName, priceType)
    # CardSearch.createGraph(priceObj)

    resp = MessagingResponse()
    
    resp.message('{} {}'.format(cardName, priceObj))
    # resp.message('https://30c8bde8.ngrok.io/priceGraph.png')

    # with resp.message() as message
    # resp.message.body({}.format(cardName))
    # message.media('http://6b20acef.ngrok.io/priceGraph.png')

    return str(resp)

# Graph image URL
@app.route('/priceGraph.png', methods=['GET', 'POST'])
def uploaded_file():
    return send_from_directory('./','priceGraph.png')

if __name__ == '__main__':
    app.run(debug=True)