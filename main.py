from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

data = []


@app.route("/")
def index():
    return render_template("index.html", todo_list = data, count = len(data))

@app.route("/change_status/<id>")
def change_status(id):
    for item in data:
        if item["id"] == id:
            item["status"] = not item["status"]

    return redirect(url_for("index"))



@app.route("/del/<id>")
def del_item(id):
    for item in data:
        if item["id"] == id:
            data.remove(item)

    return redirect(url_for("index"))



@app.route("/search", methods=["POST"])
def search_item():
    searching_word = request.form.get("search_item")
    search_list = []

    for item in data:
        if searching_word in item["text"]:
            search_list.append(item)

    return render_template("index.html", todo_list = search_list, count = len(data))



@app.route("/add_item", methods=["POST"])
def add_item():
    text = request.form.get("item").strip()

    if not text:
        return redirect(url_for("index"))

    item = {
        "id": str(uuid.uuid4()),
        "text": text,
        "status": False
    }

    data.append(item)

    print(data)
    return redirect(url_for("index"))





if __name__ == '__main__':
    app.run(port=8000)