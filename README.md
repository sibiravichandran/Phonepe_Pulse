# Phonepe_Pulse
Phonepe Pulse Data Visualization
![PhonePe](https://user-images.githubusercontent.com/102207260/229822254-d6c2fa88-6ba8-4980-979b-dfcd66009354.jpg)


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


                import git

                def git_clone():
                    return  git.Repo.clone_from("https://github.com/PhonePe/pulse.git", "PhonePe_Pulse")

                if __name__ == "__main__":

                    git_clone()


The code above is a Python script that uses the "git" module to clone a Git repository from the specified URL (https://github.com/PhonePe/pulse.git) into a local directory named "PhonePe_Pulse". Here's a breakdown of what each part of the code does:

The line "import git" imports the "git" module, which provides a Python interface for working with Git repositories.

The "git_clone()" function is defined, which uses the "Repo.clone_from()" method provided by the "git" module to clone the Git repository from the specified URL into the local directory specified as the second argument ("PhonePe_Pulse").

The "if name == "main":" block is a conditional statement that ensures that the "git_clone()" function is only called if the script is being run directly as the main program (i.e., not being imported as a module by another script). When the script is run, the "git_clone()" function is called, which clones the specified Git repository into the local directory.

In summary, this script uses the "git" module to clone a Git repository from a specified URL into a local directory, which can be used for further development or analysis.
    


## Data Process

The code defines a function that aggregates data from multiple JSON files and returns the data as a Pandas DataFrame. 


### Example:

                def st_agg_transactions(route_path):

                        path = Path(route_path)
                        col1_names = ['State', 'Year', 'Quarter', 'Payments','Transaction_type', 'Transaction_count', 'Transaction_amount']
                        col1_values = []

                        for state_path in path.iterdir():
                            if state_path.is_dir():
                                state = state_path.name
                                for year_path in state_path.iterdir():
                                    if year_path.is_dir():
                                        year = year_path.name
                                        for quarter_path in year_path.iterdir():
                                            if quarter_path.is_file() and quarter_path.suffix == '.json':
                                                quarter = int(quarter_path.stem)
                                                with open(quarter_path, 'r') as f:
                                                    data = json.load(f)
                                                    try:
                                                        for transaction in data['data']['transactionData']:
                                                            name = transaction['name']
                                                            type_of_transac =  transaction['paymentInstruments'][0]['type']
                                                            count = transaction['paymentInstruments'][0]['count']
                                                            amount = transaction['paymentInstruments'][0]['amount']
                                                            col1_values.append([state, year, quarter, name,type_of_transac, count, amount])
                                                    except Exception as e :
                                                        print(e)

                        df_st_agg_transactions = pd.DataFrame(col1_values, columns=col1_names)

                        df_st_agg_transactions.head()

                        df_st_agg_transactions.isnull().sum()

                        #df_st_agg_transactions.to_csv('StateWise_Aggregated_Transactions.csv')

                        return df_st_agg_transactions



The code above defines a function named st_agg_transactions that aggregates transaction data from multiple JSON files and returns the aggregated data as a Pandas DataFrame. 
Here's what each part of the code does:

The function takes one argument, route_path, which specifies the path to the directory containing the transaction data files.

The Path() function from the pathlib module is used to create a Path object representing the specified directory.

A list of column names (col1_names) is defined for the DataFrame that will hold the aggregated transaction data.

An empty list (col1_values) is defined to hold the transaction data itself.

The function iterates over the directories and files in the specified directory using a series of nested for loops. For each directory and file, the function extracts the state, year, and quarter information from the directory and file names, and uses the json module to load the transaction data from the JSON file.

The function then iterates over the transaction data and extracts the name, type, count, and amount information for each transaction.

The extracted transaction data is appended to the col1_values list.

Once all the transaction data has been extracted and appended, the col1_values list is used to create a new Pandas DataFrame (df_st_agg_transactions) with the specified column names (col1_names).

The function returns the df_st_agg_transactions DataFrame.

Finally, the function also contains some commented-out code (#df_st_agg_transactions.to_csv('StateWise_Aggregated_Transactions.csv')) that would save the aggregated transaction data to a CSV file if uncommented.

In summary, the st_agg_transactions function aggregates transaction data from multiple JSON files into a Pandas DataFrame, making it easier to analyze and manipulate the data.

## Cleaning Data
The below code defines a function called clean_state_names that takes a Pandas DataFrame df as input. The function replaces the abbreviated state names or misspelled state names in the State column of the input DataFrame df with their correct and full names using a predefined dictionary. The corrected DataFrame is then returned.

            def clean_state_names(df):

                states={'andaman-&-nicobar-islands':'Andaman & Nicobar',
                        'andaman & nicobar islands':'Andaman & Nicobar',
                         'andhra-pradesh': 'Andhra Pradesh',
                         'andhra pradesh': 'Andhra Pradesh',
                         'arunachal-p':'Arunanchal Pradesh',
                         'arunachal-pradesh':'Arunanchal Pradesh',
                         'arunachal pradesh':'Arunanchal Pradesh',
                         'assam': 'Assam',
                         'bihar': 'Bihar',
                         'chandigarh': 'Chandigarh',
                         'chhattisgarh': 'Chhattisgarh',
                         'dadra-&-nagar-haveli-&-dama':'Dadara & Nagar Havelli & Daman & Diu',
                         'dadra-&-nagar-haveli-&-daman-&-diu':'Dadara & Nagar Havelli & Daman & Diu',
                         'dadra & nagar haveli & daman & diu' : 'Dadara & Nagar Havelli & Daman & Diu',
                         'delhi': 'NCT of Delhi',
                         'goa': 'Goa',
                         'gujarat': 'Gujarat',
                         'haryana': 'Haryana',
                         'himachal-pradesh': 'Himachal Pradesh',
                         'himachal pradesh': 'Himachal Pradesh',
                         'jammu-&-kashmir': 'Jammu & Kashmir',
                         'jammu & kashmir': 'Jammu & Kashmir',
                         'jharkhand': 'Jharkhand',
                         'karnataka': 'Karnataka',
                         'kerala': 'Kerala',
                         'ladakh': 'Ladakh',
                         'lakshadweep':'Lakshadweep',
                         'madhya-pradesh': 'Madhya Pradesh',
                         'madhya pradesh':'Madhya Pradesh',
                         'maharashtra': 'Maharashtra',
                         'manipur': 'Manipur',
                         'meghalaya': 'Meghalaya',
                         'mizoram':'Mizoram',
                         'nagaland': 'Nagaland',
                         'puducherry': 'Puducherry',
                         'punjab': 'Punjab',
                         'rajasthan': 'Rajasthan',
                         'sikkim': 'Sikkim',
                         'tamil-nadu': 'Tamil Nadu',
                         'tamil nadu':'Tamil Nadu',
                         'telangana': 'Telangana',
                         'tripura': 'Tripura',
                         'uttar-pradesh': 'Uttar Pradesh',
                         'uttar pradesh':'Uttar Pradesh',
                         'uttarakhand': 'Uttarakhand',
                         'west-bengal': 'WestBengal',
                         'west bengal': 'WestBengal',
                         'odisha':'Odisha',
                         }

                df['State'] = df['State'].replace(states)
                return df
                
                
## Table Creation

### create_database_tables 
    
                connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password = "12345678",
                database = "Phonepe_Database"
                )

                #cursor = connection.cursor()

                #my_cursor.execute("CREATE DATABASE Phonepe_Database")

                print('Conn is established')

                engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/Phonepe_Database', echo=False)

                # Write DataFrames to MySQL tables using SQLAlchemy engine
                tables_to_create = {

                    'Statewise_Agg_Transactions': df_st_aggregated_transactions,
                    'Statewise_Agg_Users': df_st_aggregated_users,
                    'Statewise_Map_Transactions': df_st_map_transaction,
                    'Statewise_Map_Users': df_st_map_user,
                    'State_DistrictWise_Top_Transactions': df_st_dt_top_transactions,
                    'State_PincodeWise_Top_Transactions': df_st_pin_top_transactions,
                    'State_DistrictWise_Top_Users': df_st_dt_top_users,
                    'State_PincodeWise_Top_Users': df_st_pin_top_users

                }

                for table_name, df in tables_to_create.items():
                    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

                    print('Tables created successfully.')

                connection.commit()

                connection.close()

The code establishes a connection to a MySQL database on a local machine, and then creates several tables in that database based on DataFrames. The connection details are specified in the connection object, which includes the host name, user name, password, and database name.

The code uses the create_engine method from the SQLAlchemy library to create an engine object that can connect to the database using the same connection details. It then iterates through a dictionary of table names and DataFrames, and uses the to_sql method of each DataFrame to write the data to the corresponding table in the database. The if_exists parameter is set to 'replace', which means that if the table already exists, it will be dropped and recreated with the new data.

Finally, the code commits the changes to the database and closes the connection.

## Data Visualization

To make the data visualize according to the manipulation over the data libraries like matplotlib, plotly,seaborn are used.

Choropleth maps are used for geo visualization of data
Example:
![newplot](https://user-images.githubusercontent.com/102207260/229823634-754f846c-2689-4fc9-9694-b178bd850171.png)

Some of the Visualizations used for this project:

![newplot (2)](https://user-images.githubusercontent.com/102207260/229824952-59d21224-b77d-4d45-849b-dc3cbbd9a3a7.png)
![newplot (1)](https://user-images.githubusercontent.com/102207260/229824964-b278a804-b7b2-4459-ba27-7ce47fe2a15b.png)
![newplot (7)](https://user-images.githubusercontent.com/102207260/229824969-b74592d7-9642-4870-a713-2d7dc4d2d6c7.png)
![newplot (6)](https://user-images.githubusercontent.com/102207260/229824972-381581de-f7dc-4c3b-9eba-7eb1271d2e8f.png)
![newplot (5)](https://user-images.githubusercontent.com/102207260/229824975-3aee4d42-cf73-4bbe-888f-975ece454c32.png)
![newplot (4)](https://user-images.githubusercontent.com/102207260/229824979-16b576a6-6dbb-48e0-a34b-7e143b76fb0b.png)



## Inspired From:

Data set link: https://github.com/PhonePe/pulse#readme

Inspired from: https://www.phonepe.com/pulse/explore/transaction/2022/4/
