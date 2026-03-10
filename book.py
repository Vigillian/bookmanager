class Book:

    def __init__(self, judul, penulis, tahun, status):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = status

    def get_status(self):
        return self.status


class BookRead(Book):

    def get_status(self):
        return "Sudah Dibaca"


class BookUnread(Book):

    def get_status(self):
        return "Belum Dibaca"
