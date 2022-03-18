from flask import Flask,jsonify, render_template, request


app = Flask(__name__)

title = "Flask tutorial"
subtitle = "Running on port 5000"

@app.route('/')
def hello_world():
  return render_template('index.html', title=title, subtitle=subtitle)


@app.route('/teste')
def json_test():
  a = 5 * 592
  res = {
    "name":"Thiago",
    "age": 20,
    "phones": [
      {
        "name": "Nokia",
        "number": '999998877'
      },
      {
        "name": "Samsung",
        "number": '989598877'
      }
    ]
  }
  return jsonify(res)

  
@app.route('/add', methods=['POST'])
def add_two_nums():
  body = request.get_json()
  if body['x'] and body['y']:
    try:
      res = body['x'] + body['y']
      return jsonify(res), 200
    except request.HTTPError as exception:
      print(exception), 400




if __name__ == '__main__':
  app.run(debug=True)