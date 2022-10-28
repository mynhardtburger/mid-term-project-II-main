# Intro
This is our mid-term project as part of Lighthouse Labs' datascience bootcamp as part of the September 2022 class.  
The task was to use unsupervised clustering techniques to find interesting neighborhood clusters. Clustering on economic or demographic data was to be avoided.

# Approach
The common yelp/foursquare/google restaurant and business review APIs were avoided to keep the project fresh. Various datasets on the NYC open data portal were considered including: 2018 parks squirel census, rodent inspections, tree registry and crime statistics.

We ended up using two datasets:
1. New York City Housing and Vacancy survey (NYCHVS) of 2017
2. Street tree census of 2015

## NYCHVS
This is a survey which is done every 3 years covering a sample of occupied buildings, their residents and vacant buildings throughout NYC.

Various features were considered. Opinion responses from the residents on their neihborhood, the affordability of their housing and factual building age data provided the most interpretable clustering signals while avoiding economic and demographic data.

## Street tree census
This is a census done every 5 years which covers street trees. Trees on private propery and in park are not included.

# Output
Species level tree density clusters and four distinct resident opinion group clusters were identified. These were mapped and visualized using Tableau. The Tableau dashboard provides a convenient tool with which to interrogate the data. 

While no explicit conclusions can be drawn from the results some regions show correlations between resident opinion clusters and tree density clusters. This is a proof concept ontop of which further datasets can be incorporated to help drive decision making and analysis.


# Data sources
* https://www.census.gov/data/datasets/2017/demo/nychvs/microdata.html -> 2017 New York Housing & Vacancy survey (NYCHVS)
* https://www.census.gov/geographies/reference-maps/2017/demo/nychvs/sub-bourough-maps.html -> NYCHVS borough sub-borough ID descriptions
* https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh -> 2015 Street tree census
* https://github.com/nycehs/NYC_geography -> NYC sub-borough GeoJSON files
* https://cityofnewyork.github.io/opendatatsm/citystandards.html -> Geospatial coordinate system used for NYC open data

# Files
* README.md

## Notebooks
* Street trees.ipynb
* NYCHVS: New York City Housing & Vacancy Survey 2017 clustering notebook

## Data
* Data readme.md
* cluster names.csv: Names of the resulting NYCHVS clusters
* old_PUMA_or_Subborough.geo.json: GeoJSON of the NYC boroughs.
* vacant-units-17: Field definitions of vacant buildings survey. Not used in final clustering.
* person-records-17: Field definitions of respondents of each occipied building.
* occupied-units-17: Field definitions of occupied buildings survey.
* Boroughs.xlsx: Mapping of borough and sub-borough id's from the NYCHVS surveys to the GEOCODE field in the GeoJSON.

## Visualizations
* NYC.twb: Tableau dashboard
* NYC tableau data.hyper: Tableau 

## Cluster result sets
* Tree species clusters
* Housing survey response clusters

# Authors
* Mynhardt Burger <https://github.com/mynhardtburger>
* Jeremy Rilkoff <https://github.com/jrilkoff>


