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


### JSON Structure / Syntax
### 1. Aggregated
1.1 data/aggregated/transaction/country/india/2018/1.json
Transaction data broken down by type of payment at country level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/transaction/country/india/state/delhi/2018/1.json

            {
                "success": true, //Ignore. For internal use only
                "code": "SUCCESS", //Ignore. For internal use only
                "data": {
                    "from": 1514745000000, //Data duration
                    "to": 1522175400000,
                    "transactionData": [
                        {
                            "name": "Recharge & bill payments", //Type of payment category
                            "paymentInstruments": [
                                {
                                    "type": "TOTAL",
                                    "count": 72550406, //Total number of transactions for the above payment category
                                    "amount": 1.4472713558652578E10 //Total value
                                }
                            ]
                        },

                        ...,

                        ...,

                        {
                            "name": "Others",
                            "paymentInstruments": [
                                {
                                    "type": "TOTAL",
                                    "count": 5761576,
                                    "amount": 4.643217301269438E9
                                }
                            ]
                        }
                    ]
                },
                "responseTimestamp": 1630346628866 //Ignore. For internal use only.
            }



1.2 data/aggregated/user/country/india/2021/1.json
Users data broken down by devices at country level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/user/country/india/state/delhi/2021/1.json

            {
                "success": true, //Ignore. For internal use only.
                "code": "SUCCESS", //Ignore. For internal use only.
                "data": {
                    "aggregated": {
                        "registeredUsers": 284985430, //Total number of registered users for the selected quarter.
                        "appOpens": 8635508502 //Number of app opens by users for the selected quarter
                    },
                    "usersByDevice": [ //Users by individual device
                        {
                            "brand": "Xiaomi", //Brand name of the device
                            "count": 71553154, //Number of registered users by this brand.
                            "percentage": 0.2510765339828075 //Percentage of share of current device type compared to all devices.
                        },

                        ...,

                        ...,

                        {
                            "brand": "Others", //All unrecognized device types grouped here. 
                            "count": 23564639, //Number of registered users by all unrecognized device types.
                            "percentage": 0.08268717105993804 //Percentage of share of all unrecognized device types compared to overall devices that users are registered with.
                        }
                    ]
                },
                "responseTimestamp": 1630346630074 //Ignore. For internal use only.
            }
            
            
### 2. Map
2.1 data/map/transaction/hover/country/india/2021/1.json
Total number of transactions and total value of all transactions at the state level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for district level too. Ex: data/map/transaction/hover/country/india/state/delhi/2021/1.json      

            {
                "success": true, //Ignore. For internal use only.
                "code": "SUCCESS", //Ignore. For internal use only.
                "data": {
                    "hoverDataList": [ //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
                        {
                            "name": "puducherry", //State / district name
                            "metric": [
                                {
                                    "type": "TOTAL", 
                                    "count": 3309432, //Total number of transactions done within the selected year-quarter for the current state/district.
                                    "amount": 5.899309571743641E9 //Total transaction value within the selected year-quarter for the current state/district.
                                }
                            ]
                        },

                        ...,

                        ...,

                        {
                            "name": "tamil nadu",
                            "metric": [
                                {
                                    "type": "TOTAL",
                                    "count": 136556674,
                                    "amount": 2.4866814387365314E11
                                }
                            ]
                        }            
                    ]
                },
                "responseTimestamp": 1630346628834 //Ignore. For internal use only.
            }

2.2 data/map/user/hover/country/india/2021/1.json
Total number of registered users and number of app opens by these registered users at the state level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for district level too. Ex: data/map/user/hover/country/india/state/delhi/2021/1.json

            {
                "success": true, //Ignore. For internal use only.
                "code": "SUCCESS", //Ignore. For internal use only.
                "data": {
                    "hoverData": { //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
                        "puducherry": {
                            "registeredUsers": 346279, //Total number of registered users for the selected state/district
                            "appOpens": 7914507 //Total number of app opens by the registered users for the selected state/district
                        },

                        ...,

                        ...,

                        "tamil nadu": {
                            "registeredUsers": 16632608,
                            "appOpens": 348801714
                        }
                    }
                },
                "responseTimestamp": 1630346628866 //Ignore. For internal use only.
            }


### 3. Top
3.1 data/top/transaction/country/india/2021/1.json
Top 10 states / districts / pin codes where the most number of the transactions happened for a selected year-quarter combination.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. The only exception is, it won't have data for states. Ex: data/top/transaction/country/india/state/delhi/2021/1.json

            {
                "success": true, //Ignore. For internal use only.
                "code": "SUCCESS", //Ignore. For internal use only.
                "data": {
                    "states": [ //List of states where most number of transactions happened along with total value for a selected year-quarter combination.
                        {
                            "entityName": "karnataka", // State name
                            "metric": {
                                "type": "TOTAL",
                                "count": 523797492, //Total number of transactions
                                "amount": 7.549953574123948E11 //Total value of all transactions
                            }
                        },

                        ...,
                    ],
                    "districts": [ //List of districts where most number of transactions happened along with total value for a selected year-quarter combination.
                        {
                            "entityName": "bengaluru urban", //District name
                            "metric": {
                                "type": "TOTAL",
                                "count": 348712787, //Total number of transactions
                                "amount": 4.324013412317671E11 //Total value of all transactions
                            }
                        },

                        ...,
                    ],
                    "pincodes": [ //List of pin codes where most number of transactions happened along with total value for a selected year-quarter combination.
                        {
                            "entityName": "560001", //Pin code
                            "metric": {
                                "type": "TOTAL",
                                "count": 111898471, //Total number of transactions
                                "amount": 1.5427512629157785E11 //Total value of all transactions
                            }
                        },

                        ...,
                    ]
                },
                "responseTimestamp": 1630346629360 //Ignore. For internal use only.
            }
            
            
 3.2 data/top/user/country/india/2021/1.json
Top 10 states / districts / pin codes where most number of users registered from, for a selected year-quarter combination.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. The only exception is, it won't have data for states. Ex: data/top/user/country/india/state/delhi/2021/1.json

            {
                "success": true, //Ignore. For internal use only.
                "code": "SUCCESS", //Ignore. For internal use only.
                "data": {
                    "states": [ //List of states where the most number of users registered from, for a selected year-quarter combination.
                        {
                            "name": "maharashtra", //State name
                            "registeredUsers": 37077537 //Number of registered users
                        },

                        ...,
                    ],
                    "districts": [ //List of districts where the most number of users registered from, for a selected year-quarter combination.
                        {
                            "name": "bengaluru urban", //State name
                            "registeredUsers": 9955387 //Number of registered users
                        },

                        ...,
                    ],
                    "pincodes": [ //List of pin codes where most number of users registered from, for a selected year-quarter combination.
                        {
                            "name": "201301", //Pin code
                            "registeredUsers": 541127 //Number of registered users
                        },

                        ...,
                    ]
                },
                "responseTimestamp": 1630346630074 //Ignore. For internal use only.
            }
            
 ## Github Cloning

'''
import git

def git_clone():
    return  git.Repo.clone_from("https://github.com/PhonePe/pulse.git", "PhonePe_Pulse")

if __name__ == "__main__":
    
    git_clone()
'''
    




## Inspired From:

Data set link: https://github.com/PhonePe/pulse#readme

Inspired from: https://www.phonepe.com/pulse/explore/transaction/2022/4/

