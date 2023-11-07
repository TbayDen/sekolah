from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Siswa(db.Model):
    __tablename__ = 'siswa'
    id = db.Column(db.Integer, primary_key=True)
    nis = db.Column(db.Integer)
    nisn = db.Column(db.Integer)
    nama = db.Column(db.String(250))
    bidang_keahlian = db.Column(db.String(250))
    kompetensi_keahlian = db.Column(db.String(250))
    kelas = db.Column(db.String(50))
    #semester =   
    #Tahun ajaran = 

    def __repr__(self):
        return f"Siswa(id={self.id}, nis={self.nis}, nisn={self.nisn}, nama={self.nama}, bidang_keahlian={self.bidang_keahlian}), kompetensi_keahlian={self.kompetensi_keahlian}, kelas={self.kelas})"