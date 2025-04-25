
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_size():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    product_type = data.get('product_type')

    # Basic rule-based size prediction logic (for testing/demo)
    size = "M"
    confidence = "80%"
    if product_type == "top":
        if height < 160 and weight < 50:
            size = "XS"
        elif 160 <= height <= 170 and 50 <= weight <= 60:
            size = "S"
        elif 170 <= height <= 180 and 60 <= weight <= 70:
            size = "M"
        elif 180 <= height <= 190 and 70 <= weight <= 85:
            size = "L"
        else:
            size = "XL"
    elif product_type == "bottom":
        size = "M"  # Placeholder logic
    elif product_type == "footwear":
        size = "42"  # Placeholder logic

    return jsonify({
        "size": size,
        "confidence": confidence
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
