# Denver Crime Data Science
the 4th Paradigm data science student organization

Colorado State University | Fort Collins, Colorado

## Data
This project analyzes data from the city of Denver, and can be found [here](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime). The data are also hosted on [kaggle](https://www.kaggle.com/paultimothymooney/denver-crime-data). From denvergov.org:

>This dataset includes criminal offenses in the City and County of Denver for the previous five calendar years plus the current year to date. The data is based on the National Incident Based Reporting System (NIBRS) which includes all victims of person crimes and all crimes within an incident. The data is dynamic, which allows for additions, deletions and/or modifications at any time, resulting in more accurate information in the database. Due to continuous data entry, the number of records in subsequent extractions are subject to change. Crime data is updated Monday through Friday.

Because the data are updated regularly, we must choose a snapshot to ensure that everyone has the same data. We will be using version 25, which can be accessed at https://www.kaggle.com/paultimothymooney/denver-crime-data/version/25. Make sure you download this version, NOT the latest version.

## Getting started
Please consult the [*Project setup*](https://github.com/the4thparadigm/hitchhikers_guide/tree/master/ds_projects/project_set_up) section of the hitchhiker's guide before proceeding.
1. Clone this repo
```bash
git clone https://github.com/the4thparadigm/denvercrime.git
```
2. Create a virtual environment called `venv` in the project root directory and activate it
```bash
virtualenv --python=python3 venv  # confirm any messages to create
echo "source venv/bin/activate" >> source_me.sh
source source_me.sh
```
3. Create your own branch to work on
```bash
cd denvercrime
git branch mybranch
```
4. Install packages from requirements.txt using `pip` in the project root directory
```bash
pip3 install -r requirements.txt
```
5. System environment
  * Update PYTHONPATH with the `src` folder/directory so python can import packages from `src`
  * Create environment variable that points to config file so python can find it
```bash
echo "export PYTHONPATH=src:$PYTHONPATH" >> source_me.sh
echo "export CONFIGYAML=config/config.yml.template" >> source_me.sh
source source_me.sh
```
6. Download the data from kaggle
  * Get a kaggle API token from your profile page (kaggle.com/username/account --> Create new API token)
  * Copy the `kaggle.json` file to `$HOME/.kaggle`
  ```bash
  mkdir -f $HOME/.kaggle
  mv $HOME/Downloads/kaggle.json $HOME/.kaggle/kaggle.json
  chmod 600 $HOME/.kaggle/kaggle.json  # only you can read/write to it
  ```
  * Navigate to the project directory and un-zip the data
  ```bash
  kaggle datasets download -d paultimothymooney/denver-crime-data/version/25
  mv denver-crime-data.zip data/raw
  unzip denver-crime-data.zip`
  ```
