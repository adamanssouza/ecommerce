from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommecer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Boa prática adicionar isso

db = SQLAlchemy(app)

# produto(id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True) # Corrigido para db.Text

    def __repr__(self):
        return f'<Product {self.name}>'

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description",""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message":"Produto cadastrado com sucesso"})
    return jsonify({"message": "Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message":"Produto deletado com sucesso"})
    return jsonify({"message": "Product not found"}),404

    
@app.route('/')
def hello_word():
    return 'Hello Word'

if __name__ == "__main__": # Corrigido para "__main__"
    app.run(debug=True)