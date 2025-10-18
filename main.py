from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/", methods=[ "POST"])
def hola_mundo():
    import pusher
    data = request.get_json()
   
    pusher_client = pusher.Pusher(
        app_id = "2065485",
        key = "e20b94984455774539fe",
        secret = "bdb758bec6eb6142c9d7",
        cluster = "mt1",
        ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', {'message':data["message"]})
    return ".."

if __name__ == "__main__":
    app.run(debug=True)