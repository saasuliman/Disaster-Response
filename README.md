# UDACITY Disaster Response Pipeline Project

## Prerequisites

### Libraries

To run this project, you have to install the required libraries in the `requirements.txt`. Run the command below.
```
pip install -r requirements.txt
```

### Model

The model was built with KNNeigbours Classifier. The script to the model can be found in the `train_classifier.py` file.
Due to the large file size of the model, it cannot be uploaded here. But when the train_classifier.py file is run, it will generate a pcikle file of the model.

---

## Introduction

This project deals with classifying text, the processes involved:

### 1. ETL Process

We merged the dataset in the `data` folder, `disaster_messages.csv` and `disaster_categories.csv`, then did some cleaning on the dataset and stored the clean data in sqlite database `DisasterResponse.db`.

### 2. Training Model

Using scikit-learn, then we train the classifier to be able to get a model which can classify a message, save the model in the `models` folder with the name `classifier.pkl`.

### 3. Run the Web App

Flask was use to run and deploy the model into a w eb app.

---

### Files

#### `data/disaster_categories.csv` , `data/disaster_messages.csv`

These are the dataset used in the project, `disaster_messages.csv` contains the message  and genre of the message while `disaster_categories.csv` contains the categories of each message.

#### `data/process_data.py`

This file is used for the ETL process, where we merged the `disaster_messages.csv` and `disaster_categories.csv` then store it in sqlite database.

#### `data/DisasterResponse.db`

This is the database that stores the cleaned and preprocessed data.

#### `models/train_classifier.py`

Loading the data from the database and training of the model was done here.

### `app/templates/go.html`

This contains the code to the web page that displays the classification result

### `app/templates/master.html`

This contains the code to the web page for to main page of the web app

#### `app/run.py`

This contains the code to the web app that the model runs on.

---

## Instructions

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        ```
        python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
        ```
    - To run ML pipeline that trains classifier and saves
        ```
        python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
        ```

2. Run the following command in the app's directory to run your web app. 
```
python run.py
```

3. Go to http://0.0.0.0:3001/
