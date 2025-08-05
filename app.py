from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import numpy as np
import pickle
import os

# Load the trained model and scaler
with open("kmeans_model.pkl", "rb") as model_file:
    kmeans = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

app = Flask(__name__)

@app.route('/')
def home():
    # Load clustered segmentation data
    df = pd.read_csv('segmentation_results.csv')

    # Display first 20 rows in a basic HTML table
    html_table = df.head(20).to_html(classes='table table-striped', index=False)

    # Simple HTML template to display the table
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
        # Get JSON input
        input_data = request.get_json()

        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data])

        # Scale input data
        input_scaled = scaler.transform(input_df)

        # Predict cluster
        prediction = kmeans.predict(input_scaled)

        return jsonify({
            "input": input_data,
            "predicted_cluster": int(prediction[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
