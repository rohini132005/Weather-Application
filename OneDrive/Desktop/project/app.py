from flask import Flask, render_template, request
from ir_model import rank_documents

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    message = ""

    if request.method == "POST":
        query = request.form["query"]
        ranked = rank_documents(query)

        # Filter only matching documents
        results = [r for r in ranked if r["score"] > 0]

        if not results:
            message = "No relevant documents found."

    return render_template("index.html", results=results, message=message)
if __name__ == "__main__":
    app.run(debug=True)