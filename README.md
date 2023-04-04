# Phonepe_Pulse
Phonepe Pulse Data Visualization


The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.


The solution includes the following steps:
1. Extracting the data from the Phonepe pulse Github repository through scripting and clone it..
2. Transforming the data into a suitable format and perform any necessary cleaning and pre-processing steps.
3. Inserting the transformed data into a MySQL database for efficient storage and retrieval.
4. Created a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually      appealing manner.
5. Fetched the data from the MySQL database to display in the dashboard.
6. Provided at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.

## Approach

1. Data extraction
2. Data transformation
3. Database insertion
4. Dashboard creation
5. Data retrieval
6. Deployment


## Guide
This data has been structured to provide details of following two sections with data cuts on Transactions and Users of PhonePe Pulse Folder that has been cloned using the PhonepePulse git repository's data folder

### Aggregated 
    Aggregated values of various payment categories as shown under Categories section
### Map 
    Total values at the State and District levels.
### Top 
    Totals of top States / Districts /Pin Codes
All the data provided in these folders is of JSON format.

## Documentation

### Folder Structure
Head to the data folder to the find below shown structure. Overall, above mentioned sections data can be found at top level folder structure.

Under each of these sections there are folders for Transactions and Users respectively.

Data for Transactions and Users is grouped under country level within India folder which further grouped the data into each year(for country level data) and there is one folder with name state which groups data for all the available states of India respectively.

Similar to country level data, state level data too grouped into each year. All of these year folders(both at country and state level) have a maximum of four files with names starting from 1 to 4. These numbers represent each quarter in the selected year.

Example: 2021 > 1.json represents data for quarter 1 (Jan, Feb and Mar 2021)

            data
            |___ aggregated
                |___ transactions
                    |___ country
                        |___ india
                            |___ 2018
                            |    1.json
                            |    2.json
                            |    3.json
                            |    4.json

                            |___ 2019
                            |    ...
                            |___ 2019
                            |___ state 
                                |___ andaman-&-nicobar-islands
                                    |___2018
                                    |   1.json
                                    |   2.json
                                    |   3.json
                                    |   4.json

                                |___ andhra-pradesh
                                |    ...
                                |    ...

## Inspired From:

Data set link: https://github.com/PhonePe/pulse#readme

Inspired from: https://www.phonepe.com/pulse/explore/transaction/2022/4/

