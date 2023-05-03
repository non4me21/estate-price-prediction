# Estate Price Prediction App

Hi, it's my application for engineering thesis. The goal was to make a web app which may help people who want to check possible price of flat in Wroclaw/Poland. 

## General info

In repo you can see two directiories: "Backend i Testy"(BE) and "Frontend"(FE). In BE you can find data mining, data processing, plots, training and tuning machine learning model (random forest), API for frontend and simple tests. In FE there is only React application with user-friendly interface.

## Technologies

### Data mining and processsing:
- Selenium
- Beautiful Soup
- Pandas

### Machine Learning:
- SciKit-Learn

### Backend:
- Flask

### Frontend: 
- React

### Tests:
- PyTest
- Selenium

## Dataset
Dataset consist 7000 records of flats and apartments located in Wrocław in mieszkania_wspolrzedne.csv. Data was mined from site otodom, polish online market for houses/flats/apartments. Columns in dataset are: address, latitude, longitude, number of rooms, floor area in squared metres and price in zloty.

## Machine learning algorithm
After consideration of few algoritms random forest algorithm had the best results. Parametres has been tuned in tuning.py using method from scikit-learn. Model is saved in model.sav file.

## Setup

1. Get into "Backend i testy". Install requirements with `pip install –r requirements.txt` and run app with `python3 api.py`.
2. Get into "Frontend". Install with `npm install` and run with `npm start`.
3. Have fun :).

