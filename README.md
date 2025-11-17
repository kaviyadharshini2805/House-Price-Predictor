# 🏠 House Price Predictor

A Streamlit web app that predicts house prices using a trained machine learning model. Users input numeric and categorical features of a house, and the app predicts the estimated price instantly.

## Dataset

The dataset contains historical house data with the following features:

Feature	Type	Description
bedrooms	Numeric	Number of bedrooms
bathrooms	Numeric	Number of bathrooms
sqft	Numeric	Square footage of the house
lot_size	Numeric	Size of the lot in sq.ft
age	Numeric	Age of the house
year_built	Numeric	Year the house was built
garage	Numeric	Number of garage spaces
location	Categorical	House location (e.g., Downtown, Rural, Hills)
house_type	Categorical	Type of house (Condo, Townhouse, Apartment, House)
condition	Numeric	House condition rating (1–5)
has_pool	Binary	1 if the house has a pool, 0 otherwise
has_fireplace	Binary	1 if there’s a fireplace, 0 otherwise
has_basement	Binary	1 if there’s a basement, 0 otherwise
school_rating	Numeric	Nearby school rating (1–10)
price	Numeric	House sale price (target variable)

## Example data:

bedrooms	bathrooms	sqft	lot_size	age	year_built	garage	location	house_type	condition	has_pool	has_fireplace	has_basement	school_rating	price
3	5	2229	12569	38	1986	1	Rural	Condo	4	0	1	0	10	199148
3	2	1897	8942	27	1997	3	Rural	Townhouse	3	0	0	1	3	152932

## Installation

### Clone the repository:

git clone github.com/kaviyadharshini2805/House-Price-Predictor.git
cd house-price-predictor


### Install dependencies:

pip install -r requirements.txt


Ensure your trained pipeline pipeline.pkl is in the project directory.

### Usage

Run the Streamlit app:

streamlit run app.py


Input house details into the form.

Click Predict Price to get the estimated price.

## Features

The app uses the following input features:

Numeric Features:
bedrooms, bathrooms, sqft, lot_size, age, year_built, garage, school_rating, has_pool, has_fireplace, has_basement

Categorical Features:
location, house_type, condition
