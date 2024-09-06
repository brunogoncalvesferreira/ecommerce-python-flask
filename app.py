# Importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Banco de dados SQL usando o SQLAlchemy ORM

app = Flask(__name__) # Cria uma instância da aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Configura o SQLAlchemy para usar o SQLite como banco de dados

db = SQLAlchemy(app) # Conexão com o SQLite

# Modelagem do banco de dados
# Produto (id, name, price, description)
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.Text, nullable=True)

# Definir uma rota raiz ( página inicial ) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
  return 'Hello, World!'

# Executar a aplicação
if __name__ == '__main__':
 app.run(debug=True)
  

