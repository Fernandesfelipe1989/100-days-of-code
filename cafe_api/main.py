from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random():
    from random import choice
    cafes = Cafe.query.all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/cafes", methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.all()
    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(results=all_cafes)


@app.route("/search", methods=['GET'])
def search_cafe():
    location = request.args.get('loc')
    cafes = Cafe.query.filter_by(location=location).all()
    if cafes:
        match_cafes = [cafe.to_dict() for cafe in cafes]
        return jsonify(results=match_cafes)
    return jsonify(error={'Not Found': "Sorry, we don' have a cafe at that location"})


## HTTP POST - Create Record

@app.route("/cafes/", methods=["POST"])
def add_cafe():
    data = request.form
    if data:
        cafe = Cafe(
            name=data.get('name'),
            can_take_calls=data.get('can_take_calls', "").title() == "True",
            has_sockets=data.get('has_sockets', "").title() == "True",
            has_toilet=data.get('has_toilet', "").title() == "True",
            has_wifi=data.get('has_wifi', "").title() == "True",
            coffee_price=data.get('coffee_price'),
            img_url=data.get('img_url'),
            location=data.get('location'),
            map_url=data.get('map_url'),
        )
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={'success': "Successfully added the new cafe"})
    return jsonify(error={"Bad Request": "It's necessary a body with data"})

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
