## Weather Data Pipeline:
      This project fetches weather data from the open-meteo API,transforms the data into a structured format, and stores it in BigQuery for analysis.

## Project Overview

This project demonstrates a simple data pipeline that fetches weather data from the Open-Meteo API, transforms it into a structured format using Python and Pandas, and stores the processed data as a CSV file.

## Objective

The goal of this pipeline is to automate weather data collection and prepare the data for analytics workflows.

## Technologies Used

- Python
- Pandas
- Requests
- Open-Meteo API

## Pipeline Steps

1. Fetch weather data from the API
2. Convert JSON response into structured tabular format
3. Store the processed data as a CSV file
4. Prepare the data for future warehouse integration such as BigQuery

## Files Included

- fetch_weather.py → Python pipeline script
- weather_data.csv → Generated dataset
- README.md → Project documentation

## API Used

Open-Meteo Weather API:
https://open-meteo.com/

## Future Improvements

- Automate scheduled data collection
- Integrate directly with BigQuery
- Add historical weather tracking
- Build dashboard visualizations
