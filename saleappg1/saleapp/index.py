from flask import Flask, render_template, request

from saleapp import dao

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q")

    cates= dao.load_categories()
    prods=dao.load_products(q=q)
    return render_template("index.html",cates=cates,prods=prods)


if __name__ == "__main__":
    app.run(debug=True)
