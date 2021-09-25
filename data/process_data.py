# This script preprocesses the data and saves the result into an sql database

# import needed libraries to run the script

import pandas as pd
import sys
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """Combines messages and categories into a single dataframe"""

    # Loads messages into pandas dataframe
    messages = pd.read_csv(messages_filepath)
    # Loads categories into pandas dataframe
    categories = pd.read_csv(categories_filepath)

    # Merge the two dataframes
    data = messages.merge(categories, on='id')
    
    return data


def clean_data(data):
    """Preprocesses and cleans merged dataframe"""
    
    # Creates new columnn according to category
    categories = data['categories'].str.split(pat=';', expand=True)

    # Rename columns accordingly
    row = categories.loc[0]
    category_colnames = list(row.apply(lambda x: x.split('-')[0]))
    categories.columns = category_colnames

    # Tidies up values in categories
    for col in categories:

        # set each value to be the last character of the string
        categories[col] = categories[col].apply(lambda x: x.split('-')[1])
        
        # Convert each column into numeric data type
        categories[col] = categories[col].astype(int)

    categories['related'] = categories['related'].replace(2, 1)

    # Drops categories column
    data.drop(columns=['categories'], inplace=True)
    # Binds full data with new categories
    data = pd.concat([data, categories], axis=1)
    # Drops duplicate from the data
    data.drop_duplicates(inplace=True)

    return data

def save_data(data, database_filename):
    """Saves input dataframe into sqlite database"""
    
    # Create sqlite engine
    engine = create_engine('sqlite:///{}'.format(database_filename))
    # Saves messages into data base 
    data.to_sql('messages', engine, if_exists='replace', index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        data = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        data = clean_data(data)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(data, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()