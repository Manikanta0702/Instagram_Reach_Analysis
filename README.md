Instagram Engagement Analysis and Prediction Tool

Project Overview
The Instagram Engagement Analysis and Prediction Tool is an advanced Python-based project designed to collect, analyze, and predict Instagram engagement metrics using state-of-the-art techniques. This project automates the collection of Instagram data via Selenium, explores insights using Exploratory Data Analysis (EDA), and leverages both Machine Learning (ML) and Deep Learning (DL) models for predicting likes on posts based on hashtags and other features.

With a comprehensive dataset of 200 Instagram posts, this project provides a robust platform for social media managers, influencers, and analysts to understand trends, optimize content strategies, and predict user engagement.

Key Features

1. Data Collection
Automated Web Scraping:
Utilizes Selenium WebDriver to log into Instagram and scrape profile details, posts, likes, comments, and hashtags.

Robust Navigation:
Handles dynamic Instagram DOM elements using XPath and CSS Selectors.

Data Storage:
Saves data in structured formats such as JSON and CSV for further analysis.

Collected Metrics:
Profile-level: Follower count, following count, number of posts.
Post-level: Post URL, likes, comments, hashtags, timestamp, and location.

2. Exploratory Data Analysis (EDA)

Visualizing Engagement:
Distribution of likes and comments across posts.
Temporal patterns in engagement (daily, monthly trends).

Hashtag Analysis:
Identifies top hashtags and their contribution to post engagement.

Location Insights:
Analyzes location-wise average likes to understand audience preferences.

3. Machine Learning
Implements various regression algorithms to predict likes based on features:
Linear Regression.
Ridge and Lasso Regression.
Random Forest Regressor.
XGBoost Regressor.
Evaluation Metrics:
Mean Squared Error (MSE).
Mean Absolute Error (MAE).
R-squared Score.
Results indicate the predictive performance of different models for engagement metrics.

4. Deep Learning
Bidirectional LSTM for Hashtag-Based Predictions:
Tokenizes hashtags and creates embeddings for training.
Leverages sequential information in hashtags for predicting likes.

Model Architecture:
Embedding Layer: Converts hashtags into dense vector representations.
Bi-LSTM Layer: Captures contextual and sequential dependencies.
Fully Connected Layers: Outputs predicted likes as a regression problem.
Training and Optimization:
Early stopping to prevent overfitting.
Dynamic learning rate scheduling.

5. Visualizations
Bar Plot: Top 10 videos by views.
Box Plot: Likes distribution based on hashtags.
Line Chart: Monthly engagement trends.
Pie Chart: Top hashtags by frequency.

6. Dynamic Hashtag Prediction
Accepts user-defined hashtags to predict likes using the trained deep learning model.
Enables real-time predictions for new hashtag strategies.

Project 			Files
File				Description
Web_Scraper.py			Script for scraping Instagram data using Selenium.
instagram_profile_beebomco.json	JSON file containing the scraped Instagram data for analysis.
Tech_Instagram_Analysis.ipynb	Jupyter Notebook for EDA, ML/DL training, and visualizations.
requirements.txt		List of dependencies required for the project.
README.md			This comprehensive project documentation.

Installation
1. Clone the Repository
git clone https://github.com/yourusername/instagram-engagement-tool.git
cd instagram-engagement-tool

2. Install Dependencies
Install required libraries via pip:
pip install -r requirements.txt

3. Set Up WebDriver
Ensure the Google Chrome browser is installed, and WebDriverManager is configured.

Usage
Step 1: Data Collection
Run the Web_Scraper.py to scrape Instagram data:
python Web_Scraper.py
Logs into Instagram using credentials.
Scrapes the latest 200 posts from the specified profile.
Saves data in JSON format for further analysis.

Step 2: Data Analysis
Open the Jupyter Notebook (Tech_Instagram_Analysis.ipynb) to perform:

Visualization of likes, comments, and hashtags.
Analysis of engagement patterns across time and locations.

Step 3: Model Training
Machine Learning:
Train models to predict likes based on post features.

from sklearn.linear_model import Ridge
model = Ridge().fit(X_train, y_train)

Deep Learning:
Train Bi-LSTM for hashtag-based predictions.
from keras.models import Sequential
model.fit(X_train, y_train, epochs=50, validation_split=0.1)

Step 4: Predictions
Dynamic Hashtag Input:
predict_likes("#technology")  # Predict likes for the hashtag
Results and Visualizations

1. Key Insights
Temporal Trends:
Engagement is highest on weekends and during specific times of the day.

Hashtag Analysis:
Certain hashtags consistently outperform others in driving likes.

Location Analysis:
Posts tagged with "Beebom" locations had the highest average likes.

2. Visual Outputs
Bar Plot: Top 10 videos by views.
Pie Chart: Most frequently used hashtags.
Line Plot: Monthly engagement trends.
Scatter Plot: Actual vs. Predicted Likes.

3. Model Performance
Machine Learning Models:
Model			MAE		R²
Ridge Regression	76464914.23	6786.53	0.37
Random Forest		88460152.91	6909.44	0.27

Deep Learning:
Metric		Value
Test Loss (MSE)	623569.32
Test MAE	550.29

Known Limitations
Web Scraping Challenges:
Instagram's DOM structure changes frequently, requiring script updates.
Automated scraping may trigger Instagram's rate-limiting mechanisms.

Limited Feature Set:
Additional features like user demographics and caption sentiment could improve predictions.

Future Enhancements
Web App Deployment:
Convert the tool into an interactive web application for broader usability.

Expanded Analysis:
Incorporate more features like post format (image, video) and caption analysis.

Advanced Visualizations:
Interactive dashboards for real-time engagement monitoring.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
We welcome contributions to improve this project. Open issues or submit pull requests on GitHub.