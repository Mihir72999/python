from flask  import Flask, render_template , request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo 
from waitress import serve
import pprint
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mihir72999:Mihir72999@api.tv0cw9w.mongodb.net/data?retryWrites=true&w=majority"
mongo = PyMongo(app).db


CORS(app)
product_data = [
    {
        "name":"apple",
        "price":150,
        "qty":4
    },
    {
       "name":"samsung",
       "price":140,
       "qty":4 
    }
]  


@app.route("/")
def hello() :
    print("f", float(2 * 3))
    item = mongo.products.find()
    datas = list(item) 
    return render_template('index.html' , datas = datas)


@app.route('/data')
def data() :
  
    return jsonify(product_data)

@app.route('/product')
def product() :
   
   item = mongo.products.find()   
   datas = list(item)
   
   return render_template('card.html', datas=datas)

@app.route('/product/<name>')
def detail(name) :
     
      items = mongo.products.find({'name':name})
      for datas in items :
           datas
      return render_template('detail.html', datas=datas   )

@app.route('/itemData') 
def itemData() :
     datas = product()
     print(datas) 
     return datas

@app.route('/cart', methods=['GET' ,'POST'])
def addToCart() :
  input = request.form.get('input')

  if input and request.method == 'POST' :
    print(input)
  return render_template('cart.html') 

@app.route('/contact') 
def contact() :
      return render_template('contact.html')


if __name__ == '__main__':
             serve(app)
