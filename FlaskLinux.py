from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/nao', methods=['POST'])
def nao_endpoint():
    #data = request.json
    data = request.get_json()['image_data']
    # Process the data sent from NAO
    photo_data = base64.b64decode(data)


    with open("nao/testdata.jpg", "wb") as file:
        file.write(photo_data)
    #print(data)
    return 'Received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)

