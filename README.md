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
* Create a virtual environment by running `virtualenv venv` in the project root directory. Activate it with `source venv\bin\activate`
* Install packages from requirements.txt by running `pip3 install -r requirements.txt` in the project root directory
* System environment
  * Append the repo src folder to PYTHONPATH to allow module imports
  * Create environment variable that points to config file so python can find it
* Download the data from kaggle
  * Get a kaggle API token from your profile page (kaggle.com/username/account --> Create new API token)
  * In a terminal, navigate to your home directory
  * `mkdir .kaggle`
  * `mv Downloads/kaggle.json .kaggle/kaggle.json`
  * Navigate to the project directory
  * `kaggle datasets download -d paultimothymooney/denver-crime-data/version/25`
  * `mv denver-crime-data.zip data/raw`
  * `unzip denver-crime-data.zip`
  
## .gitignore
This repository provides a basic .gitignore. If you've never used a .gitignore, it's simply a list of directories and files that we want to Git to ignore when it performs its magic. If you have any files in your project directory that you don't want included in version control, add them to the .gitignore. For example, if you created a notebook for your own personal exploration as notebooks/exp.ipynb, you would add notebooks/exp.ipynb to the .gitignore and Git would ignore this file when you make changes to it. The .gitignore in this repo lists the things that come with the repo that should be ignored (like the .gitignore).
