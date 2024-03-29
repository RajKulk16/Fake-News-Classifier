# Fake-News-Classifier

This project contains 2 components. The opening page consists of fake news statistics (interactive pie chart) and much information about the same. 

First component is to check whether the news is fake or not. "train.csv" is used for checking if the news is fake or not. The model has been trained with respect to the 'title'. Therefore, to check fake news, copy paste the title from csv to the site. Two Jupyter Notebooks are used for this project. One is for EDA and the other is for flask. The default port for flask is set to 2000 but can be changed. 

Second component is of interactive graphs which are related to Covid-19 which also predicts the number of cases in India and Brazil in the next 5 days (including today - current date). Graphs include tracking of Covid-19 vaccinations, recorded cases, next 5 days' prediction and more. 

NOTE:

1)Due to limited space on Heroku (for a non-premium user), the deployed application on Heroku consists of the 'fake news checker' component and only 2 graphs. Click on the link to view the deployed project on heroku- https://rvfakenews.herokuapp.com/

2)For better view experience, set the Zoom of browser window to 90% either after running app.py in your flask terminal or after clicking on the link above.


Paper Published -  https://ijtre.com/wp-content/uploads/2022/03/2022090702.pdf

## Website snaps:

#### Main page: 
<img src="https://github.com/Novid-Patsham/covid-project-MIT/blob/main/website%20snaps/Main%20page%201.png" width="900" height="1000">
<img src="https://github.com/Novid-Patsham/covid-project-MIT/blob/main/website%20snaps/Main%20page%202.png" width="900" height="1000">

#### Fake news classifier:
<img src="https://github.com/Novid-Patsham/covid-project-MIT/blob/main/website%20snaps/fake_news_page.png" width="1000" height="400">

#### Visualization: 
<img src="https://github.com/Novid-Patsham/covid-project-MIT/blob/main/website%20snaps/graph_page%201.png" width="900" height="1000">
<img src="https://github.com/Novid-Patsham/covid-project-MIT/blob/main/website%20snaps/graph_page%202.png" width="900" height="1000">
