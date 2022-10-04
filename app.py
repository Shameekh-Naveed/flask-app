from flask import Flask,render_template, request
from cs50 import SQL

app=Flask(__name__)

db = SQL("sqlite:///comments.db")
@app.route('/',methods=["GET","POST"])

def index():
  if request.method=="GET":
    return render_template("index.html")
  else:
    name=request.form.get("name")
    comment=request.form.get("comments")
    names=db.execute("SELECT DISTINCT(name) FROM comments")
    if name in names:
      db.execute("DELETE FROM comments WHERE name=?", name)
      return render_template("index.html")
    db.execute("INSERT INTO comments(name,comments) VALUES(?,?)",name,comment)
    comments=db.execute("SELECT * FROM comments")
    return render_template("index.html", comments=comments)
