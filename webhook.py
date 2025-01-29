from flask import Flask, request

app = Flask(__name__)

# Token segreto per verificare il webhook
VERIFY_TOKEN = "mio_token123"

@app.route('/webhook', methods=['GET'])
def verify():
    token_sent = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token_sent == VERIFY_TOKEN:
        return challenge
    return "Token non valido", 403

@app.route('/webhook', methods=['POST'])
def receive_message():
    data = request.json
    print("Messaggio ricevuto:", data)  # Qui riceverai i messaggi di Instagram
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
