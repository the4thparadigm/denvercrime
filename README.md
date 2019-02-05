# Denver Crime Data Science
the 4th Paradigm data science student organization

Colorado State University | Fort Collins, Colorado

## Data
This project analyzes data from the city of Denver, and can be found [here](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime). The data are also hosted on [kaggle](https://www.kaggle.com/paultimothymooney/denver-crime-data). From denvergov.org:

>This dataset includes criminal offenses in the City and County of Denver for the previous five calendar years plus the current year to date. The data is based on the National Incident Based Reporting System (NIBRS) which includes all victims of person crimes and all crimes within an incident. The data is dynamic, which allows for additions, deletions and/or modifications at any time, resulting in more accurate information in the database. Due to continuous data entry, the number of records in subsequent extractions are subject to change. Crime data is updated Monday through Friday.

Because the data are updated regularly, we must choose a snapshot to ensure that everyone has the same data. We will be using version 25, which can be accessed at https://www.kaggle.com/paultimothymooney/denver-crime-data/version/25. Make sure you download this version, NOT the latest version.

## Getting started
Please consult the [*Project setup*](https://github.com/the4thparadigm/hitchhikers_guide/tree/master/ds_projects/project_set_up) section of the hitchhiker's guide before proceeding. 
* Clone this repo 
* Create your own branch to work on
* Install packages from requirements.txt
* System environment
  * Append the repo src folder to PYTHONPATH to allow module imports
  * Create environment variable that points to config file so python can find it
* Create directories for the data.
  * In a terminal, navigate to the project directory
  * `mkdir data`
  * `mkdir data/raw
* Download the data from kaggle
  * Get a kaggle API token from your profile page (kaggle.com/username/account --> Create new API token)
  * In a terminal, navigate to your home directory
  * `mkdir .kaggle`
  * `mv Downloads/kaggle.json .kaggle/kaggle.json`
  * Navigate to the project directory
  * `mv denver-crime-data.zip data/raw`
  * `unzip denver-crime-data.zip`
  * `kaggle datasets download -d paultimothymooney/denver-crime-data/version/25`

  
