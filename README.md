# Mid-Term Project
This repository cointains all the information you need to work on the Mid-Term project.

## Hello and Welcome!!!

The idea of this project is to segment the neighborhoods of New York City into separate clusters and examine the information about them. A desirable intention is to create the neighborhood cluster’s based on the various information we are able to find, for example:

- location
- restaurants and different venue types
    - [Foursquare](https://developer.foursquare.com/places)
    - [Yelp](https://www.yelp.com/developers/documentation/v3/get_started)
    - [Google Places API](https://developers.google.com/places/web-service/intro)
- [Uber rides](https://data.world/data-society/uber-pickups-in-nyc) 
- [meetups](https://www.meetup.com/meetup_api/)
- There could be something interesting in [NYC Open Data](https://data.cityofnewyork.us/browse?sortBy=most_accessed&utf8=%E2%9C%93)
- You can use different data that come to your mind as well

**Do not include** any economic or demographic indicators in our input data. However, further examination might reveal if data above has any relationship with the diversity of a neighborhood and its economics.


### Files

- **data_preparation.ipynb** - contains further information about how to proceed with data preparation
- **modeling.ipynb** - contains important information about the modeling part of the project

### Data

- The NYC neighborhoods can be found [here](https://drive.google.com/file/d/16hGHxuPHDVVwlHhiZ5pFoNMfmGjh_JYb/view?usp=sharing).
- [Average housing prices for Manhattan and Brooklyn](https://drive.google.com/file/d/17kDaedI8cBoZz8rKY7yZ0N-QNSLChQWR/view?usp=sharing) from July 2020 by [City Realty](https://www.cityrealty.com/nyc/market-insight/rental-building-offers/battery-park-city/map-average-nyc-rent-prices-july-2020-21-buildings-offering-free-rent/45084).
- [Median housing prices for Manhattan and Brooklyn](https://drive.google.com/file/d/1EyXSpnV--2iYmYzlGZmMgonbW9jzJdcv/view?usp=sharing) from Feb 2021 by[Zumber](https://www.zumper.com/rent-research/new-york-ny).


### Presentation Guidelines

The main goal of this presentation is to prepare you for your **Demo Day** at the end of the bootcamp where your time will be capped. Therefore, it's important to keep the duration of the presentation to **max 5 minutes** (number of slides doesn't necessarily determine the duration of the presentation). Focus on explaining what you did, how you approached the problem, what you achieved, and, if appropriate, suggest what else could be done. Don't speak to every single task and step there is, focus more on the highlights and interesting findings instead. If you struggled with something, feel free to mention it, but do not undermine your work by highlighting that part.

1. Spend **1 min** on project flow structure.
    Which steps does your project have?
2. Spend **1 min** on showing different APIs and data sources you took the information and data from.
    - were there any interesting findings you came up with during EDA?
3. Results (**1 min**):
    - what clustering techniques did you use?
    - evaluation metrics
    - how did you come up with the number of clusters?
4. **1 min** on profiling of clusters
    - what are the features that show the biggest difference across the clusters?
    - what features are showing the biggest correlation with economic indicators?
5. Explain the biggest challenges in **1 min**.
    - what would you do if you have a bit more time?


### Submission Guidelines

1. Share the link to your project repository through Compass
2. The file `submission.csv` that contains two columns, name of the neighborhood and cluster_id, should be included in the repository.


### How to Start

As the first step, we need to parse the original JSON file with the neighborhoods into the Pandas. Afterward, we can start to gather different data from various sources. Spend some time on research of different APIs that could be used. Information from all data sources need to be joined with the neighborhoods before we can proceed with feature engineering and clustering itself. Do not forget about visualizations of clusters and neighborhoods as well becaue there is a lot of things that can be done in this area.
