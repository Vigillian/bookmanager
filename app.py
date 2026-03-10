from flask import Flask, render_template, request, redirect
from database.db import get_db, init_db
from models.book import BookRead, BookUnread

app = Flask(__name__)

init_db()


@app.route("/")
def index():

    conn = get_db()

    books = conn.execute(
        "SELECT * FROM books ORDER BY tahun DESC"
    ).fetchall()

    conn.close()

    return render_template("index.html", books=books)


@app.route("/tambah", methods=["POST"])
def tambah():

    judul = request.form["judul"]
    penulis = request.form["penulis"]
    tahun = request.form["tahun"]
    status = request.form["status"]

    if status == "Sudah Dibaca":
        book = BookRead(judul, penulis, tahun, status)
    else:
        book = BookUnread(judul, penulis, tahun, status)

    conn = get_db()

    conn.execute(
        "INSERT INTO books (judul,penulis,tahun,status) VALUES (?,?,?,?)",
        (book.judul, book.penulis, book.tahun, book.get_status())
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db()

    conn.execute("DELETE FROM books WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):

    conn = get_db()

    book = conn.execute(
        "SELECT * FROM books WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template("edit.html", b=book)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    judul = request.form["judul"]
    penulis = request.form["penulis"]
    tahun = request.form["tahun"]
    status = request.form["status"]

    conn = get_db()

    conn.execute(
        """UPDATE books
        SET judul=?, penulis=?, tahun=?, status=?
        WHERE id=?""",
        (judul, penulis, tahun, status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
