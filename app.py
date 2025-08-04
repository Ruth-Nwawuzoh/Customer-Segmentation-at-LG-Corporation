from flask import Flask, render_template_string
import pandas as pd
import os

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
        https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
    </head>
    <body class="p-4">
        <h2>LG Customer Segmentation Results</h2>
        <p>This table shows a sample of the clustered data (first 20 records).</p>
        {html_table}
    </body>
    </html>
    '''

    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
