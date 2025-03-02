Customer Behavioral Segmentation in a Shopping Mall

📌 Project Overview

This project uses Machine Learning to segment customers based on their shopping behavior in a mall. The goal is to help businesses understand different customer groups and personalize marketing strategies.

Using clustering techniques like K-Means, Hierarchical Clustering, and DBSCAN, we analyze Annual Income, Spending Score, and Shopping Frequency to classify customers into different segments.

📊 Key Features:
✔ Customer segmentation using ML algorithms
✔ Data preprocessing & visualization
✔ Elbow Method & Silhouette Score for cluster evaluation
✔ Business insights for marketing strategies
✔ (Optional) Interactive Web App using Streamlit/Flask
📂 Project Structure

customer-segmentation-mall  
│── data/               # Raw & processed datasets  
│── notebooks/          # Jupyter notebooks for each step  
│── src/               # Python scripts (data processing, clustering)  
│── reports/           # Findings & insights (PDF, images)  
│── app/               # (Optional: Flask/Streamlit web app)  
│── README.md          # Project overview & guide  
│── requirements.txt   # Required dependencies  
│── LICENSE            # (Optional: Open-source license)  
│── .gitignore         # Ignore unnecessary files

📊 Dataset

Source: Mall Customer Segmentation Dataset

Features:

CustomerID: Unique identifier

Gender: Male/Female

Age: Customer age

Annual Income (k$): Customer income

Spending Score (1-100): Shopping pattern score

Shopping Frequency: Visits per month


🚀 How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/yourusername/customer-segmentation-mall.git
cd customer-segmentation-mall

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Jupyter Notebook (For Analysis)

jupyter notebook

4️⃣ Run Streamlit App (Optional, If Web UI is Included)

streamlit run app/app.py

🔬 Machine Learning Models Used

✅ K-Means Clustering (Finds groups using centroids)
✅ Hierarchical Clustering (Uses dendrograms for grouping)
✅ DBSCAN (Detects high-density customer clusters)

📊 Results & Insights

✔ Identified high-value customers for targeted offers
✔ Segmented budget-conscious vs. frequent shoppers
✔ Helped businesses optimize marketing campaigns

📌 Example Visualization:

📜 Technologies Used

🔹 Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
🔹 Jupyter Notebook for data analysis
🔹 Flask/Streamlit (optional for UI)
🔹 Google Colab (for online execution)

🔗 Run on Google Colab

📜 License

This project is open-source under the MIT License.


