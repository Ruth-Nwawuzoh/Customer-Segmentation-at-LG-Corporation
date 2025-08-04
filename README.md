# Customer-Segmentation-at-LG-Corporation
LG Customer Segmentation Using K-Means Clustering
# LG Customer Segmentation Using K-Means Clustering

## Project Overview

This project analyzes customer data to identify distinct segments for LG Corporation, a global leader in consumer electronics. LG aims to enhance its marketing and pricing strategies using data-driven insights. By applying unsupervised machine learning, specifically K-Means clustering, the company can better understand customer behavior and tailor strategies to each group.

## Business Objective

- Segment customers based on preferences, behavior, and purchasing patterns.
- Optimize marketing messages and product pricing per segment.
- Increase engagement, satisfaction, and revenue through personalization.

---

## Getting Started

Follow the steps below to run the project on your local machine.

### 

1. Clone the repository: 
[https://github.com/Ruth-Nwawuzoh/Customer-Segmentation-at-LG-Corporation.git]
*or* unzip the file:  
   `Ruth_Nwawuzoh_BAN6800_Final_Project.zip`

2. Open Lg_Segmentation_Analysis.ipynb in Jupyter Notebook, JupyterLab, or VSCode.

3. Run all cells step-by-step 

The notebook includes data loading, cleaning, eda, encoding, scaling, clustering, visualization, and data export.
###
---

##  Requirements & Installation
Before running the notebook, make sure you have Python 3.7+ installed. 

## Tools & Libraries Used

- `pandas` – For data manipulation and analysis
- `numpy` – For numerical operations
- `matplotlib`- For plotting graphs
- `seaborn` – For advanced visualizations
- `joblib` - For saving/loading models or scalers
- `os` - For interacting with the file system
- `sklearn` – Scaling, K-Means, PCA, silhouette score

---

## Why Unsupervised Learning?

This is an **unsupervised learning** problem because:
- There is **no target variable**.
- The goal is to **discover natural groupings** (clusters) of customers based on their attributes.
- We use **K-Means**, a popular clustering technique, to identify these groups.

---

## Workflow Steps

### 1. **Import Libraries**
Import necessary Python packages for data loading, visualization, preprocessing, clustering, and evaluation.

### 2. **Load Dataset**
Read the dataset from `consumer_electronics_sales_data.csv`, which includes customer behavior and purchase data.

### 3. **Data Cleaning**
Remove irrelevant columns such as `ProductID` and check for missing values and duplicates.

### 4. **Exploratory Data Analysis**
- Different distributions of the variables
- Relationship among variables

### 5. **Data Preparation**
- Convert categorical columns to category type.
- One-hot encode categorical variables.
- Standardize features using `StandardScaler`.

### 6. **Determine Optimal Clusters**
Use:
- **Elbow Method** – For inertia drop-off.
- **Silhouette Score** – For clustering quality.
Optimal clusters were selected as `k=4`.

### 7. **K-Means Clustering**
Fit the model using 4 clusters and assign each customer to a group.

### 8. **Cluster Profiling**
Generate statistical summaries of each cluster to understand customer behavior patterns.

### 9. **Visualization**
Apply **PCA** to reduce dimensions and visualize clusters in 2D.

### 10. **Export Clustered Data**
Save the segmented dataset as `segmentation_results.csv` for future business use.

---

## Cluster Interpretation


| Cluster | Summary                                                  |
|---------|----------------------------------------------------------|
|    0    | Tech-savvy laptop buyers with moderate satisfaction      |
|    1    | Smart watch enthusiasts with high satisfaction and intent|
|    2    | Tablet users with balanced behavior and Sony preference  |
|    3    | Smartphone-focused, mobile-first shoppers                | 


---

## Files Included

- `Lg_Segmentation_Analysis.ipynb` – Jupyter Notebook with full analysis.
- `consumer_electronics_sales_data.csv` – Raw dataset from Kaggle.
- `output` – Directory containing saved plots.
- `segmentation_results.csv` – Final customer data with cluster labels.
- `README.md` – This summary file (Project overview and instructions)

---

## Outcome

With this clustering model, LG can:
- Deploy **personalized marketing** campaigns.
- Improve **price optimization** based on behavior.
- Build a **scalable segmentation system** for real-time targeting.

---

## Deployment on Render

To make this project publicly accessible, we deployed it using [Render](https://render.com/).

### Steps to Deploy

1. **Ensure you have these files in your GitHub repo**:
   - `app.py` – Contains the Flask app
   - `requirements.txt` – Lists Python dependencies (e.g., pandas, flask, scikit-learn, etc.)
   - `Lg_Segmentation_Analysis.ipynb` – Optional, for reference
   - `consumer_electronics_sales_data.csv` – The dataset used
   - `segmentation_results.csv` – Processed output 

2. **Login to [Render](https://render.com/)** using your GitHub account.

3. **Create a new Web Service**:
   - Click **“New” > “Web Service”**
   - Connect your **GitHub repository**
   - Choose the correct repo and branch
   - Set the **Build Command** (if needed):  
     ```
     pip install -r requirements.txt
     ```
   - Set the **Start Command**:  
     ```
     python app.py
     ```

4. **Deploy** the app and wait for Render to build and host it.

5. **Copy the live URL** generated by Render. This is your hosted project link.

> Note: If you're using a work laptop with installation restrictions, you can deploy **without running locally** — just make sure your files work together logically and test after deployment.

---

## Hosted App

Once deployed, your app will be available at:

[https://ruth-lg-segmentation.onrender.com/]

