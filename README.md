

# 📰 News Sentiment Analysis (Fake vs Real News Detection)

## 🔍 Overview

In today’s digital era, the rapid spread of misinformation and fake news has become a serious concern. This project aims to detect fake news articles using machine learning techniques and sentiment analysis of news headlines. By analyzing emotional tones and linguistic patterns, we built and evaluated models to classify news as FAKE or REAL effectively.

## 🎯 Objectives

- Classify news articles as FAKE or REAL.
- Analyze sentiment polarity in news headlines.
- Compare model performance based on evaluation metrics.
- Draw meaningful insights to assist in misinformation detection.

## 🧾 Dataset

- **Source**: [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/)
- **Features Used**:
  - `title`: News headline
  - `text`: Full article text
  - `label`: Ground truth (FAKE/REAL)

## ⚙️ Technologies Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn
- NLTK (for VADER sentiment analysis)
- Jupyter Notebook

## 🧠 Models Applied

- **Logistic Regression**
- **Random Forest Classifier**

## 📊 Model Performance

| Metric        | Logistic Regression | Random Forest |
|---------------|---------------------|----------------|
| Accuracy      | 0.9879              | 0.9973         |
| Precision     | 0.9849              | 0.9965         |
| Recall        | 0.9899              | 0.9978         |
| F1-Score      | 0.9874              | 0.9972         |
| AUC-ROC       | 0.9987              | 0.9999         |

Random Forest outperformed other models and was selected for final deployment.

## 😊 Sentiment Analysis

- Used **VADER** Sentiment Analyzer.
- Labels: `Positive`, `Negative`, `Neutral`
- Observations:
  - Fake news headlines tend to exhibit more emotional polarity.
  - Real news titles maintain a more neutral tone.

## 📈 Insights

- Certain keywords (e.g., “BREAKING”, “SHOCKING”) appear more in fake news.
- Sentiment distribution helped uncover tone-based patterns.
- Feature importance highlighted which terms are more predictive of fake vs real.

## 📌 Project Highlights

- Complete preprocessing, EDA, and modeling pipeline.
- Sentiment-label and truth-label comparison.
- Visual insights using matplotlib and seaborn.
- Clean and modular code in `news_sent_analysis.py`.

## 📁 Project Structure

```
📂 News-Sentiment-Analysis
│
├── 📘 News_Sent_Analysis.ipynb       # Main Jupyter notebook
├── 🐍 news_sent_analysis.py          # Python script version
├── 📊 Visualizations                 # Sentiment charts, label plots, etc.
└── README.md                         # This file
```

## ✅ Status

**Project Completed** ✅  
Ready for deployment or integration into a fact-checking pipeline.

## 🙋‍♂️ Author

**R Manisha Achary**
*Data Science Intern*  
📧 manisha.achary13@gmail.com  
🔗 https://www.linkedin.com/in/r-manisha-achary-470798204<br>
🔗 https://github.com/manishaachary13
