import pandas as pd
import json
import mysql.connector
from pathlib import Path
from sqlalchemy import create_engine

#STATE WISE OF INDIA

# STATE WISE  AGG TRANSACTIONS
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

def st_agg_users(route_path):
    path = Path(route_path)
    col2_names = ['State', 'Year', 'Quarter','Reg_Users','App_Opens', 'Brands', 'Count', 'Percentage']
    col2_values = []

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
                                    for agg_user in data['data']['usersByDevice']:
                                        brand = agg_user['brand']
                                        count = agg_user['count']
                                        percentage = agg_user['percentage']
                                        registered_users = data['data']['aggregated']['registeredUsers']
                                        app_opens = data['data']['aggregated']['appOpens']
                                        col2_values.append([state, year, quarter,registered_users,app_opens, brand, count, percentage])
                                except Exception as e :
                                    print(e)

    df_st_agg_users = pd.DataFrame(col2_values, columns=col2_names)
    df_st_agg_users.head()

    df_st_agg_users.isnull().sum()

    #df_st_agg_users.to_csv('StateWise_Aggregated_Users.csv')
    
    return df_st_agg_users


def st_map_transactions(route_path):
    path = Path(route_path)
    col3_names = ['State', 'Year', 'Quarter', 'District', 'Transaction_count', 'Transaction_amount','Transaction_type']
    col3_values = []

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
                                    for map_trans in data['data']['hoverDataList']:
                                        district = map_trans['name']
                                        count = map_trans['metric'][0]['count']
                                        amount = map_trans['metric'][0]['amount']
                                        type_of_transac =  map_trans['metric'][0]['type']
                                        col3_values.append([state, year, quarter,district, count, amount,type_of_transac])
                                except Exception as e :
                                    print(e)

                            
    df_st_map_transactions= pd.DataFrame(col3_values, columns=col3_names)

    df_st_map_transactions.head()

    df_st_map_transactions.isnull().sum()

    #df_st_map_transactions.to_csv('StateWise_Map_Transactions.csv')
    
    return df_st_map_transactions


def st_map_users(route_path):
    path = Path(route_path)
    col4_names = ['State', 'Year', 'Quarter', 'District', 'Reg_Users','App_Opens']
    col4_values = []

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
                                    for map_user,map_userdata in data['data']['hoverData'].items():
                                        district = map_user
                                        registeredUser = map_userdata['registeredUsers']
                                        app_Opens = map_userdata['appOpens']
                                        col4_values.append([state, year, quarter,district, registeredUser,app_Opens])
                                
                                except Exception as e :
                                    print(e)

                            
    df_st_map_users= pd.DataFrame(col4_values, columns=col4_names)


    df_st_map_users.head()

    df_st_map_users.isnull().sum()

    #df_st_map_users.to_csv('StateWise_Map_Users.csv')
    
    return df_st_map_users


def st_dt_top_transaction(route_path):
    path = Path(route_path)
    col5_names = ['State', 'Year', 'Quarter','District','Transaction_count','Transaction_amount','Transaction_Type']
    col5_values = []
    
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
                                    for top_transac in data['data']['districts']:
                                        district = top_transac['entityName']
                                        type_district = top_transac['metric']['type']
                                        dist_transac_count = top_transac['metric']['count']
                                        dist_transac_amount = top_transac['metric']['amount']
                                        col5_values.append([state, year, quarter,district,dist_transac_count,dist_transac_amount,type_district])
                                        
                                except Exception as e :
                                    print(e)
                                
                                                            
    df_st_dt_top_transaction = pd.DataFrame(col5_values, columns=col5_names)
    
    df_st_dt_top_transaction.head()

    df_st_dt_top_transaction.isnull().sum()

    #df_st_dt_top_transaction.to_csv('State_DistrictWise_Top_Transactions.csv')
    
    return df_st_dt_top_transaction


def st_pin_top_transaction(route_path):
    
    path = Path(route_path)
    
    col6_names = ['State', 'Year', 'Quarter','Pincode','Transaction_count','Transaction_amount','Transaction_type']
    col6_values = []
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
                                    for top_transac1 in data['data']['pincodes']:
                                        pincode = top_transac1['entityName']
                                        pincode_type = top_transac1['metric']['type']
                                        pincode_transac_count = top_transac1['metric']['count']
                                        pincode_transac_amount = top_transac1['metric']['amount']
                                        col6_values.append([state, year, quarter,pincode,pincode_transac_count,pincode_transac_amount,pincode_type])
                                except Exception as e :
                                    print(e)

                            
    
    df_st_pin_top_transaction = pd.DataFrame(col6_values, columns=col6_names)


    
    df_st_pin_top_transaction.head()

    df_st_pin_top_transaction.isnull().sum()

    #df_st_pin_top_transaction.to_csv('State_PincodeWise_Top_Transactions.csv')
    
    return df_st_pin_top_transaction



def st_dt_top_user(route_path):
    path = Path(route_path)
    col7_names = ['State', 'Year', 'Quarter','District','Reg_Users']
    col7_values = []
    
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
                                    for user_transac in data['data']['districts']:
                                        district = user_transac['name']
                                        dist_regusers = user_transac['registeredUsers']
                                        col7_values.append([state, year, quarter,district,dist_regusers])
                                except Exception as e :
                                    print(e)
                                
                                
    df_st_dt_top_user = pd.DataFrame(col7_values, columns=col7_names)
    

    

    df_st_dt_top_user.head()

    df_st_dt_top_user.isnull().sum()

    #df_st_top_user.to_csv('State_DistrictWise_Top_Users.csv')

    return df_st_dt_top_user


def st_pin_top_user(route_path):
    path = Path(route_path)
    
    col8_names = ['State', 'Year', 'Quarter','Pincode','Reg_Users']
    col8_values = []
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
                                    for user_transac1 in data['data']['pincodes']:
                                        pincode = user_transac1['name']
                                        pincode_regusers = user_transac1['registeredUsers']
                                        col8_values.append([state, year, quarter,pincode,pincode_regusers])
                                except Exception as e :
                                    print(e)
                                
    
    df_st_pin_top_user = pd.DataFrame(col8_values, columns=col8_names)

    
    df_st_pin_top_user.head()

    df_st_pin_top_user.isnull().sum()

    #df_st_pin_top_user.to_csv('State_PincodeWise_Top_Users.csv')

    return df_st_pin_top_user


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



def main():
    #Get the data from json file
    df_st_aggregated_transactions = st_agg_transactions("PhonePe_Pulse/data/aggregated/transaction/country/india/state")
    
    df_st_aggregated_users = st_agg_users("PhonePe_Pulse/data/aggregated/user/country/india/state")
    
    df_st_map_transaction= st_map_transactions("PhonePe_Pulse/data/map/transaction/hover/country/india/state")
    
    df_st_map_user= st_map_users("PhonePe_Pulse/data/map/user/hover/country/india/state")
    
    df_st_dt_top_transactions = st_dt_top_transaction('PhonePe_Pulse/data/top/transaction/country/india/state')
    
    df_st_pin_top_transactions = st_pin_top_transaction('PhonePe_Pulse/data/top/transaction/country/india/state')
    
    df_st_dt_top_users = st_dt_top_user('PhonePe_Pulse/data/top/user/country/india/state')
    
    df_st_pin_top_users = st_pin_top_user('PhonePe_Pulse/data/top/user/country/india/state')
    
    
    
    #to clean the state names
    df_st_aggregated_transactions = clean_state_names(df_st_aggregated_transactions)
    
    df_st_aggregated_users = clean_state_names(df_st_aggregated_users)
    
    df_st_map_transaction=clean_state_names(df_st_map_transaction)
    
    df_st_map_user=clean_state_names(df_st_map_user)
    
    df_st_dt_top_transactions=clean_state_names(df_st_dt_top_transactions)
    
    df_st_pin_top_transactions=clean_state_names(df_st_pin_top_transactions)
    
    df_st_dt_top_users=clean_state_names(df_st_dt_top_users)
    
    df_st_pin_top_users=clean_state_names(df_st_pin_top_users)
    
    #CSV FILES
    
    df_st_aggregated_transactions.to_csv('StateWise_Aggregated_Transactions.csv')
    
    df_st_aggregated_users.to_csv('StateWise_Aggregated_Users.csv')
    
    df_st_map_transaction.to_csv('StateWise_Map_Transactions.csv')
    
    df_st_map_user.to_csv('StateWise_Map_Users.csv')
    
    df_st_dt_top_transactions.to_csv('State_DistrictWise_Top_Transactions.csv')
    
    df_st_pin_top_transactions.to_csv('State_PincodeWise_Top_Transactions.csv')
    
    df_st_dt_top_users.to_csv('State_DistrictWise_Top_Users.csv')
    
    df_st_pin_top_users.to_csv('State_PincodeWise_Top_Users.csv')
    
    
# create_database_tables 
    #************ SQL CONNECTION ********************************************************************
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

if __name__ == "__main__":
    main()