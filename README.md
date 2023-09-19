# JDReviewAnalyzer - Comprehensive Analysis of JD.com Product Reviews

## Introduction:
JDReviewAnalyzer is an in-depth review analysis platform tailored for JD.com, one of China's most prominent e-commerce giants. Using Python-based web scraping, it focuses on capturing 1000 reviews of the most-reviewed notebook on JD.com, the "Lenovo Challenger". By harnessing technologies like SQLite for data storage, Echarts for visualization, WordCloud for word frequency representation, and Flask for web application deployment, this system provides detailed insights into product sentiment, purchase patterns, and user feedback.

## Features
- Web Scraping:
 - Automated scraping of 1000 reviews from JD.com for the Lenovo Challenger, capturing details like user ID, username, ratings, product variant, comment timestamp, and content.
- Data Storage:
 - Immediate parsing of data into an Excel sheet using xlwt for preliminary checks.
 - Persistent storage of review data in an SQLite database.
- Data Visualization:
 - Echarts integration to visualize product variant popularity through bar graphs.
- Word Frequency Analysis: 
 - Utilization of the jieba library for Chinese word segmentation.
 - Application of MapReduce for word frequency computation.
 - Representation of common phrases and words from reviews using WordCloud.
- Web Interface:
 - Deployment of a web platform via Flask, displaying database content, rating statistics, and word frequency analytics.
