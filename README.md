# README: Final project Sundowner long-term trends analysis

#### Description:
Enables analysis of long-term trends in the Sundowner weather station data.

#### Installation:
Clone repository to VS code (this will change to pip install once the work is done)

#### Quick Start:
See example notebooks temp_plot and humidity_plot for use of different scripts

#### Features / capabilities:
* Given input of a desired start and end date, the script will output a combined dataframe containing all records between the start and end date.
* Generate timeseries plots of specified variables
* (coming soon!) Generate additional plots analyzing different statistical characteristics of the data during the given time period
* (coming soon!) Analyze the "data signature" of particular events (eg. mountain wave pattern)
* (coming soon!) Detect instances where the data signature occurs throughout the timeseries data

#### Requirements / dependencies

#### Usage examples
The original purpose of this project was to develop a software tool that would identify the weather data "signature" of an event that took place on December 30, 2021 in Colorado's front range town of Superior: The Marshall fire, which burned over 1,000 homes. The Marshall fire was characterized by a particular weather pattern: a mountain wave, in which a cold front traveling West over the Rocky Mountains created extreme wind speeds. It was also preceded by an anomalously dry Fall season.  The data signature of the mountain wave pattern is high windspeed from the west, and a drop in air pressure. 

In principle, the code I'm developing here should be designed to identify instances of mountain wave events over a time period of multiple years or decades. It should also be able to tell whether or not the frequency of these events has changed over time.  If the code were even further generalized, perhaps it could be used to determine the data signature of other events, and determine their frequency over time.

#### Contributing guidelines
Anyone contributing to this project is welcome to add additional statistical analysis tools, plots or plot refinements, or work on the "coming soon!" portions.

#### License information
MIT license

#### Author information
Michael Moench
University of Colorado Masters of the Environment Program
almo1024@colorado.edu

### Data source
University of Colorado ATOC Weather Network, CU Boulder Campus. https://sundowner.colorado.edu/weather/atoc1/