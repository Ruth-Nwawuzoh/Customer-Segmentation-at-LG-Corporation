from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    df = pd.read_csv('segmentation_results.csv')
    html_table = df.head(20).to_html(classes='table table-striped', index=False)
    html_template = f'''
    <html>
    <head>
        <title>LG Customer Segmentation</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="p-4">
        <div class="container">
            <h2 class="mb-3">LG Customer Segmentation Results</h2>
            <p>This table shows a sample of the clustered data (first 20 records).</p>
            {html_table}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expect JSON with a list of features (e.g., [34, 1, 700, ...])
        input_data = request.get_json(force=True)
        input_array = np.array(input_data['features']).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        cluster = model.predict(scaled_input)
        return jsonify({'predicted_cluster': int(cluster[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
