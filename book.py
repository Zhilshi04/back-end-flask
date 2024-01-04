from flask import Flask,jsonify

app = Flask(__name__)

books = [ 
    {
        "id":1,
        "title":"Book 1",
        "author":"Author 1"
    },
    {
        "id":2,
        "title":"Book 2",
        "author":"Author 2"
    },
    {
        "id":3,
        "title":"Book 2",
        "author":"Author 2"
    }
]

@app.route("/")
def Greet():
    return "<p> Welcom to Book Management System </p>"

@app.route("/books/" ,  methods = ["GET"])
def GetAllBook():
    return jsonify(books)

@app.route("/books/<int:book_id>" , methods = ["GET"])
def GetBooks(book_id):
    book = next( (b for b in books if b["id"] == book_id),None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error : Book not found"}),404
    

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000 , debug=True)