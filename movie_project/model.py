from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MovieModel(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    year = Column(Integer)
    description = Column(String(1000), nullable=True)
    rating = Column(Float)
    ranking = Column(Integer)
    review = Column(String(1000), nullable=True)
    img_url = Column(String)

    def __repr__(self):
        return self.title
