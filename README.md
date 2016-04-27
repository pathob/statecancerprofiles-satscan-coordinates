# Statecancerprofiles Satscan Coordinates

The website http://statecancerprofiles.cancer.gov provides statistical cancer
data as csv files. To evaluate them with the http://www.satscan.org/ software, a
file with geographic data is needed.

This program takes csv files and assumes that the first row contains the
location name that should be looked up. Then it searches for this name together
with the keyword "USA" to avoid naming collisions in other countries like
Australia.

Then it generates a geo.csv file containing the location name and its latitude
and longitude.

## Usage

Install Python 3, PIP 3 and install Geopy with PIP.

Then run the following:

```bash
python3 geo.py YOURFILE.csv
```
