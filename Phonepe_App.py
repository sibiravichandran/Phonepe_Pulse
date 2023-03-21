import streamlit as st 
import pandas as pd 
import plotly.express as px 
import mysql.connector
import json
from urllib.request import urlopen
import streamlit_option_menu as streamlit_option
import plotly.graph_objs as go
import plotly.subplots as sp
from PIL import Image
import webbrowser
import uuid




#   Connecting to MYSQL

my_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password = "12345678",
    database = "Phonepe_Database"
    )

cursor = my_connection.cursor()
 
 
#   Reading Data from SQL   
def read_data_from_mysql(table_name):
    my_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password = "12345678",
    database = "Phonepe_Database"
    )
    #engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/Phonepe_Database', echo=False)
    
    df = pd.read_sql(f"SELECT * FROM {table_name}", con=my_connection)
    
    return df



df_aggregated_transaction = read_data_from_mysql('Statewise_Agg_Transactions')
df_aggregated_user = read_data_from_mysql('Statewise_Agg_Users')
df_map_transaction = read_data_from_mysql('Statewise_Map_Transactions')
df_map_user = read_data_from_mysql('Statewise_Map_Users')
df_st_dt_top_transactions = read_data_from_mysql('State_DistrictWise_Top_Transactions')
df_st_pin_top_transactions = read_data_from_mysql('State_PincodeWise_Top_Transactions')
df_st_dt_top_users = read_data_from_mysql('State_DistrictWise_Top_Users')
df_st_pin_top_users = read_data_from_mysql('State_PincodeWise_Top_Users')




#**************************************************************************************************************************

phn = Image.open('Phonepe.png')
st.set_page_config(page_title='PhonePe Pulse', page_icon=phn, layout='wide')
st.title(' PhonePe Pulse Data Visualization ')
phn1 = Image.open('Phonepe_logo.png')
my_pic = Image.open('24A.jpg')

def set_background_color(color):
    st.markdown(f'<style>body {{ margin: 0; padding: 0; background-color: {color}; }}</style>', unsafe_allow_html=True)

# Set page configuration
def set_page_config(im, bgcolor):
    st.set_page_config(
        page_title="Phonepe Pulse Insights",
        page_icon='₹',
        layout="wide",
    )
    set_background_color(bgcolor)
    
    


def display_navigation():
    
    # Generate a unique key for the widget
    #key1 = str(uuid.uuid4())


    selected1 = streamlit_option.option_menu(
    menu_title = "Welcome to PhonePe Pulse India ",  
    options = ["About","Overview of Insights","Home","Analyze Insights","Discoveries","Contact"],
    icons =["bar-chart","toggles","house","search","list-task", 'at'],
    orientation="horizontal",
    default_index=0    )
    

    return selected1



def Home():
    st.header("*Introduction*")
    st.subheader("""The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and State-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem.""")
    st.header("*GUIDE*")
    st.subheader(""" This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.""")
    st.header("*Aggregated*")
    st.subheader("Aggregated values of various types of payments, brands and so on")
        #st.write(df_aggregated_transaction.groupby(['Transaction_type'])['count'].sum())
    st.header("*Map*")
    st.subheader("Total values at the State and District levels")
    st.header("*Top*")
    st.subheader("Totals of top States / Districts / Pin Codes")
    st.header("*Github*")
    st.subheader("A home for the data that powers the PhonePe Pulse website.")
    if st.button('Open'):
        webbrowser.open_new_tab("https://github.com/PhonePe/pulse#readme")
 
 
        
def About():
    st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    col1, col2 = st.columns(2)
    with col1:
        st.image(phn1)
        if st.button("DOWNLOAD THE APP NOW"):
            webbrowser.open_new_tab('https://www.phonepe.com/app-download/')

    with col2:
        video_url = f'https://www.youtube.com/watch?v=c_1H6vivsiA'
        st.video(video_url)
        
        st.subheader("*Phonepe Now Everywhere..!*")



def Contact():
    name = " *SIBI RAVICHANDRAN* "
    mail = (f'{"Mail :"}  {"ravisibi16@gmail.com"}')
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(my_pic)
        if st.button('Github'):
            webbrowser.open_new_tab("https://github.com/sibiravichandran")
    with col2:
        st.title(name)
        st.subheader("Aspiring Data Scientist with a passion for turning data into insights and using those insights to drive business decisions.I bring a wealth of knowledge and expertise to any organization looking to streamline their operations and drive growth through effective use of technology. With a passion for continuous learning and professional as well as personal development, I am dedicated to staying on the cutting edge of industry trends and best practices, and am always seeking out new challenges and opportunities to expand my skillset. Whether it's through formal education, online courses, or simply exploring new ideas and perspectives, I am passionate about staying curious and engaged with the world around me. With a commitment to continuous growth and development, I am constantly pushing myself to reach new heights and take on new challenges and I am committed to sharing my knowledge and insights with others, and am always eager to collaborate and exchange ideas with fellow professionals in the field.. If you share my love of learning and are looking for a dynamic and enthusiastic team member to help drive innovation and success in your organization, I would love to hear from you!")
        st.write("---")
        st.subheader(mail)
    # st.write("#")
    
    
        if st.button('LinkedIn'):
            webbrowser.open_new_tab("https://www.linkedin.com/in/sibi-ravichandran-817ab021b/")



def Dashboard():
    
    padding = 0
    # is a method from the Streamlit library that allows the user to set various page-level options for the app
    #st.set_page_config(page_title="PhonePe Pulse", layout="wide", page_icon="₹")
    # setting page title
    
    with st.sidebar:
    
        selected2 = streamlit_option.option_menu(
        menu_title = "Welcome to PhonePe Pulse India Dashboard",  
        options = ['Overall Data','State-wise Data'],
        default_index=0
        )


# Overall Data Analysis
     
    if selected2 == 'Overall Data':

        
            st.subheader("Select Transactions/User Data")
            menu=st.selectbox("",('Transactions',"User"))
        
            if menu=="Transactions":
                option1 = ['Aggregated', 'Map', 'Top']
                selected_option1 = st.selectbox('Select Option', option1)
                
                col_1, col_2 = st.columns(2)
                
                with col_1:
                    st.subheader("Select Year")
                    year= st.selectbox("",("2018", "2019", "2020", "2021", "2022"))
                
                with col_2:
                    st.subheader("Select Quarter")
                    Quarter=st.selectbox('',('1','2','3','4'))
        
                
                
                if selected_option1 == 'Aggregated':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_agg_transactions WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map = df_agg[['State', 'Transaction_amount','Transaction_count']].groupby(['State']).sum().reset_index()
                
                    fig = px.choropleth(india_map,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Transaction_count',
                                    hover_data=['State', 'Transaction_amount','Transaction_count'],
                                    projection="robinson",
                                    color_continuous_scale='rainbow'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR OVERALL AGGREGATED TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                
                
                        
            
                if selected_option1 == 'Map':
                            
                            df_map = pd.read_sql(f"SELECT * FROM statewise_map_transactions WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                            #st.dataframe(df_agg)
                            
                            india_map = df_map[['State','District', 'Transaction_amount','Transaction_count']].groupby(['State']).sum().reset_index()
                        
                            fig = px.choropleth(india_map,
                                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                            featureidkey='properties.ST_NM',
                                            locations='State',
                                            color='Transaction_count',
                                            hover_data=['State', 'Transaction_amount','Transaction_count'],
                                            projection="robinson",
                                            color_continuous_scale='blackbody'
                                            )
                            
                            
                            fig.update_geos(fitbounds = 'locations',visible = False )
                            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                            
                            
                            st.subheader("MAP ANALYSIS FOR OVERALL MAP TRANSACTIONS")
                        
                            # Display the map in the Streamlit app
                            st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    
                    
                if selected_option1 == 'Top':
                            
                            df_top = pd.read_sql(f"SELECT * FROM state_districtwise_top_transactions WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                            #st.dataframe(df_agg)
                            
                            india_map = df_top[['State','District', 'Transaction_amount','Transaction_count']].groupby(['State']).sum().reset_index()
                        
                            fig = px.choropleth(india_map,
                                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                            featureidkey='properties.ST_NM',
                                            locations='State',
                                            color='Transaction_count',
                                            hover_data=['State', 'Transaction_amount','Transaction_count'],
                                            projection="robinson",
                                            color_continuous_scale='hot'
                                            )
                            
                            
                            fig.update_geos(fitbounds = 'locations',visible = False )
                            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                            
                            
                            st.subheader("MAP ANALYSIS FOR OVERALL TOP TRANSACTIONS")
                        
                            # Display the map in the Streamlit app
                            st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                            
            
            if menu=="User":
                user_options = ['Aggregated', 'Map', 'Top']
                select_option = st.selectbox('Select Option', user_options)
                
                col_1, col_2 = st.columns(2)
                
                with col_1:
                    st.subheader("Select Year")
                    year= st.selectbox("",("2018", "2019", "2020", "2021", "2022"))
                
                with col_2:
                    st.subheader("Select Quarter")
                    Quarter=st.selectbox('',('1','2','3','4'))
            
            
                if select_option == 'Aggregated':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_agg_users WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State', 'Reg_Users','App_Opens','Count','Percentage']].groupby(['State']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Count',
                                    hover_data=['State', 'Reg_Users','App_Opens','Count','Percentage'],
                                    projection="robinson",
                                    color_continuous_scale='rainbow'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR OVERALL USER AGGREGATED TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    

                
                if select_option == 'Map':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_map_users WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State', 'Reg_Users','App_Opens']].groupby(['State']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Reg_Users',
                                    hover_data=['State', 'Reg_Users','App_Opens'],
                                    projection="robinson",
                                    color_continuous_scale='piyg'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR OVERALL USER MAP TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    
                if select_option == 'Top':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM state_districtwise_top_users WHERE Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State', 'Reg_Users']].groupby(['State']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Reg_Users',
                                    hover_data=['State', 'Reg_Users'],
                                    projection="robinson",
                                    color_continuous_scale='hsv'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR OVERALL USER TOP TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
            
            
# Statewise India Analysis           
                   
    if selected2 == 'State-wise Data':
        
            STATE = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
            
            st.subheader("Select Transactions/User Data")
            menu=st.selectbox("",('Transactions',"User"))
        
            if menu=="Transactions":
                options2 = ['Aggregated', 'Map', 'Top']
                selected_option2 = st.selectbox('Select Option', options2)
                
                st.subheader("Select State")
                states =st.selectbox('',STATE)
                
                col_1, col_2 = st.columns(2)
                
                with col_1:
                    st.subheader("Select Year")
                    year= st.selectbox("",("2018", "2019", "2020", "2021", "2022"))
                
                with col_2:
                    st.subheader("Select Quarter")
                    Quarter=st.selectbox('',('1','2','3','4'))
        
                
                
                
                if selected_option2 == 'Aggregated':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_agg_transactions WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map = df_agg[['State','Payments','Transaction_amount','Transaction_count']].groupby(['State','Payments']).sum().reset_index()
                
                    fig = px.choropleth(india_map,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Transaction_count',
                                    hover_data=['State','Payments', 'Transaction_amount','Transaction_count'],
                                    projection="robinson",
                                    color_continuous_scale='puor'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR STATEWISE AGGREGATED TRANSACTIONS")
                    
                                        # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                
                    data = india_map.sort_values(by='Transaction_amount',ascending=False).reset_index(drop=True)

                    fig = px.bar(data, x='Payments', y='Transaction_count',
                            hover_data=['Transaction_count'], color='Transaction_amount',
                            labels={'Transaction_amount':'Transaction_amount'}, height=400)
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    
                    
                if selected_option2 == 'Map':
                        
                        df_map1 = pd.read_sql(f"SELECT * FROM statewise_map_transactions WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                        #st.dataframe(df_agg)
                        
                        india_map = df_map1[['State','District', 'Transaction_amount','Transaction_count']].groupby(['State','District']).sum().reset_index()
                    
                        fig = px.choropleth(india_map,
                                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                        featureidkey='properties.ST_NM',
                                        locations='State',
                                        color='Transaction_count',
                                        hover_data=['State', 'District','Transaction_amount','Transaction_count'],
                                        projection="robinson",
                                        color_continuous_scale='earth'
                                        )
                        fig.update_geos(fitbounds = 'locations',visible = False )
                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                        
                        st.subheader("MAP ANALYSIS FOR STATEWISE MAP TRANSACTIONS")
                        
                                            # Display the map in the Streamlit app
                        st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    
                        data = india_map.sort_values(by='Transaction_amount',ascending=False).reset_index(drop=True)

                        fig1 = px.bar(data, x='District', y='Transaction_count',
                                hover_data=['Transaction_count'], color='Transaction_amount',
                                labels={'Transaction_amount':'Transaction_amount'}, height=400)
                        st.plotly_chart(fig1,theme="streamlit",use_container_width=True)
                    
                    
                if selected_option2 == 'Top':
                    
                        #st.subheader("Select District")
                        #District = ['Andaman Islands', 'Nicobar Islands', 'Adilabad', 'Anantapur', 'Chittoor', 'Cuddapah', 'East Godavari', 'Guntur', 'Hyderabad', 'Karimnagar', 'Khammam', 'Krishna', 'Kurnool', 'Mahbubnagar', 'Medak', 'Nalgonda', 'Nellore', 'Nizamabad', 'Prakasam', 'Rangareddi', 'Srikakulam', 'Vishakhapatnam', 'Vizianagaram', 'Warangal', 'West Godavari', 'Changlang', 'East Kameng', 'East Siang', 'Kurung Kumey', 'Lohit', 'Lower Dibang Valley', 'Lower Subansiri', 'Papum Pare', 'Tawang', 'Tirap', 'Upper Dibang Valley', 'Upper Siang', 'Upper Subansiri', 'West Kameng', 'West Siang', 'Barpeta', 'Bongaigaon', 'Cachar', 'Darrang', 'Dhemaji', 'Dhuburi', 'Dibrugarh', 'Goalpara', 'Golaghat', 'Hailakandi', 'Jorhat', 'Kamrup', 'Karbi Anglong', 'Karimganj', 'Kokrajhar', 'Lakhimpur', 'Marigaon', 'Nagaon', 'Nalbari', 'North Cachar Hills', 'Sibsagar', 'Sonitpur', 'Tinsukia', 'Araria', 'Aurangabad', 'Banka', 'Begusarai', 'Bhabua', 'Bhagalpur', 'Bhojpur', 'Buxar', 'Darbhanga', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Katihar', 'Khagaria', 'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger', 'Muzaffarpur', 'Nalanda', 'Nawada', 'Pashchim Champaran', 'Patna', 'Purba Champaran', 'Purnia', 'Rohtas', 'Saharsa', 'Samastipur', 'Saran', 'Sheikhpura', 'Sheohar', 'Sitamarhi', 'Siwan', 'Supaul', 'Vaishali', 'Chandigarh', 'Bastar', 'Bilaspur', 'Dantewada', 'Dhamtari', 'Durg', 'Janjgir-Champa', 'Jashpur', 'Kanker', 'Kawardha', 'Korba', 'Koriya', 'Mahasamund', 'Raigarh', 'Raipur', 'Raj Nandgaon', 'Surguja', 'Dadra and Nagar Haveli', 'Daman', 'Junagadh', 'Delhi', 'North Goa', 'South Goa', 'Ahmadabad', 'Amreli', 'Anand', 'Banas Kantha', 'Bharuch', 'Bhavnagar', 'Dahod', 'Gandhinagar', 'Jamnagar', 'Junagadh', 'Kachchh', 'Kheda', 'Mahesana', 'Narmada', 'Navsari', 'Panch Mahals', 'Patan', 'Porbandar', 'Rajkot', 'Sabar Kantha', 'Surat', 'Surendranagar', 'The Dangs', 'Vadodara', 'Valsad', 'Ambala', 'Bhiwani', 'Faridabad', 'Fatehabad', 'Gurgaon', 'Hisar', 'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonepat', 'Yamuna Nagar', 'Bilaspur', 'Chamba', 'Hamirpur', 'Kangra', 'Kinnaur', 'Kullu', 'Lahul and Spiti', 'Mandi', 'Shimla', 'Sirmaur', 'Solan', 'Una', 'Anantnag (Kashmir South)', 'Bagdam', 'Baramula (Kashmir North)', 'Doda', 'Jammu', 'Kargil', 'Kathua', 'Kupwara (Muzaffarabad)', 'Ladakh (Leh)', 'Pulwama', 'Punch', 'Rajauri', 'Srinagar', 'Udhampur', 'Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'Garhwa', 'Giridih', 'Godda', 'Gumla', 'Hazaribag', 'Jamtara', 'Koderma', 'Latehar', 'Lohardaga', 'Pakur', 'Palamu', 'Pashchim Singhbhum', 'Purba Singhbhum', 'Ranchi', 'Sahibganj', 'Saraikela Kharsawan', 'Simdega', 'Bagalkot', 'Bangalore Rural', 'Bangalore Urban', 'Belgaum', 'Bellary', 'Bidar', 'Bijapur', 'Chamrajnagar', 'Chikmagalur', 'Chitradurga', 'Dakshin Kannad', 'Davanagere', 'Dharwad', 'Gadag', 'Gulbarga', 'Hassan', 'Haveri', 'Kodagu', 'Kolar', 'Koppal', 'Mandya', 'Mysore', 'Raichur', 'Shimoga', 'Tumkur', 'Udupi', 'Uttar Kannand', 'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod', 'Kollam', 'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad', 'Pattanamtitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad', 'Kavaratti', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'East Nimar', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha', 'West Nimar', 'Ahmednagar', 'Akola', 'Amravati', 'Aurangabad', 'Bhandara', 'Bid', 'Buldana', 'Chandrapur', 'Dhule', 'Garhchiroli', 'Gondiya', 'Greater Bombay', 'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Nagpur', 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Parbhani', 'Pune', 'Raigarh', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg', 'Solapur', 'Thane', 'Wardha', 'Washim', 'Yavatmal', 'Bishnupur', 'Chandel', 'Churachandpur', 'East Imphal', 'Senapati', 'Tamenglong', 'Thoubal', 'Ukhrul', 'West Imphal', 'East Garo Hills', 'East Khasi Hills', 'Jaintia Hills', 'Ri-Bhoi', 'South Garo Hills', 'West Garo Hills', 'West Khasi Hills', 'Aizawl', 'Champhai', 'Kolasib', 'Lawngtlai', 'Lunglei', 'Mamit', 'Saiha', 'Serchhip', 'Dimapur', 'Kohima', 'Mokokchung', 'Mon', 'Phek', 'Tuensang', 'Wokha', 'Zunheboto', 'Angul', 'Baleshwar', 'Baragarh', 'Bhadrak', 'Bolangir', 'Boudh', 'Cuttack', 'Deogarh', 'Dhenkanal', 'Gajapati', 'Ganjam', 'Jagatsinghpur', 'Jajpur', 'Jharsuguda', 'Kalahandi', 'Kandhamal', 'Kendrapara', 'Keonjhar', 'Khordha', 'Koraput', 'Malkangiri', 'Mayurbhanj', 'Nabarangpur', 'Nayagarh', 'Nuapada', 'Puri', 'Rayagada', 'Sambalpur', 'Sonepur', 'Sundargarh', 'Karaikal', 'Mahe', 'Puducherry', 'Yanam', 'Amritsar', 'Bathinda', 'Faridkot', 'Fatehgarh Sahib', 'Firozpur', 'Gurdaspur', 'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana', 'Mansa', 'Moga', 'Muktsar', 'Nawan Shehar', 'Patiala', 'Rupnagar', 'Sangrur', 'Ajmer', 'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Bundi', 'Chittaurgarh', 'Churu', 'Dausa', 'Dhaulpur', 'Dungarpur', 'Ganganagar', 'Hanumangarh', 'Jaipur', 'Jaisalmer', 'Jalor', 'Jhalawar', 'Jhunjhunun', 'Jodhpur', 'Karauli', 'Kota', 'Nagaur', 'Pali', 'Rajsamand', 'Sawai Madhopur', 'Sikar', 'Sirohi', 'Tonk', 'Udaipur', 'East', 'North Sikkim', 'South Sikkim', 'West Sikkim', 'Ariyalur', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kancheepuram', 'Kanniyakumari', 'Karur', 'Madurai', 'Nagapattinam', 'Namakkal', 'Nilgiris', 'Perambalur', 'Pudukkottai', 'Ramanathapuram', 'Salem', 'Sivaganga', 'Thanjavur', 'Theni', 'Thiruvallur', 'Thiruvarur', 'Thoothukudi', 'Tiruchchirappalli', 'Tirunelveli Kattabo', 'Tiruvannamalai', 'Vellore', 'Villupuram', 'Virudhunagar', 'Dhalai', 'North Tripura', 'South Tripura', 'West Tripura', 'Agra', 'Aligarh', 'Allahabad', 'Ambedkar Nagar', 'Auraiya', 'Azamgarh', 'Badaun', 'Baghpat', 'Bahraich', 'Ballia', 'Balrampur', 'Banda', 'Bara Banki', 'Bareilly', 'Basti', 'Bijnor', 'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah', 'Faizabad', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Jyotiba Phule Nagar', 'Kannauj', 'Kanpur Dehat', 'Kanpur', 'Kaushambi', 'Kushinagar', 'Lakhimpur Kheri', 'Lalitpur', 'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'Rae Bareli', 'Rampur', 'Saharanpur', 'Sant Kabir Nagar', 'Sant Ravi Das Nagar', 'Shahjahanpur', 'Shravasti', 'Siddharth Nagar', 'Sitapur', 'Sonbhadra', 'Sultanpur', 'Unnao', 'Varanasi', 'Almora', 'Bageshwar', 'Chamoli', 'Champawat', 'Dehra Dun', 'Haridwar', 'Naini Tal', 'Pauri Garhwal', 'Pithoragarh', 'Rudra Prayag', 'Tehri Garhwal', 'Udham Singh Nagar', 'Uttarkashi', 'Bankura', 'Barddhaman', 'Birbhum', 'Dakshin Dinajpur', 'Darjiling', 'East Midnapore', 'Haora', 'Hugli', 'Jalpaiguri', 'Kochbihar', 'Kolkata', 'Maldah', 'Murshidabad', 'Nadia', 'North 24 Parganas', 'Puruliya', 'South 24 Parganas', 'Uttar Dinajpur', 'West Midnapore']
                        
                        #menu=st.selectbox("",District)
                        
                        df_agg = pd.read_sql(f"SELECT * FROM state_districtwise_top_transactions WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                        #st.dataframe(df_agg)
                        
                        india_map = df_agg[['State','District', 'Transaction_amount','Transaction_count']].groupby(['State','District']).sum().reset_index()
                    
                        fig = px.choropleth(india_map,
                                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                        featureidkey='properties.ST_NM',
                                        locations='State',
                                        color='Transaction_count',
                                        hover_data=['State','Transaction_amount','Transaction_count'],
                                        projection="robinson",
                                        color_continuous_scale='amp'
                                        )
                        fig.update_geos(fitbounds = 'locations',visible = False )
                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                        
                        st.subheader("MAP ANALYSIS FOR STATEWISE TOP TRANSACTIONS")
                        
                                            # Display the map in the Streamlit app
                        st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                        
                        data = india_map.sort_values(by='Transaction_amount',ascending=False).reset_index(drop=True)

                        fig2 = px.bar(data, x='District', y='Transaction_count',
                                hover_data=['Transaction_count'], color='Transaction_amount',
                                labels={'Transaction_amount':'Transaction_amount'}, height=400)
                        st.plotly_chart(fig2,theme="streamlit",use_container_width=True)
                   
         
            
            if menu=="User":
                user_options = ['Aggregated', 'Map', 'Top']
                select_option = st.selectbox('Select Option', user_options)
                
                st.subheader("Select State")
                states =st.selectbox('',STATE)
                
                col_1, col_2 = st.columns(2)
                
                with col_1:
                    st.subheader("Select Year")
                    year= st.selectbox("",("2018", "2019", "2020", "2021", "2022"))
                
                with col_2:
                    st.subheader("Select Quarter")
                    Quarter=st.selectbox('',('1','2','3','4'))
            
            
                if select_option == 'Aggregated':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_agg_users WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State','Brands','Reg_Users','App_Opens','Count','Percentage']].groupby(['State','Brands']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Count',
                                    hover_data=['State', 'Reg_Users','App_Opens','Count','Percentage'],
                                    projection="robinson",
                                    color_continuous_scale='oxy'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR STATEWISE USER AGGREGATED TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    

                    data = india_map_user.sort_values(by='Reg_Users',ascending=False).reset_index(drop=True)

                    fig2 = px.bar(data, x='Brands', y='Count',
                            hover_data=['Reg_Users','App_Opens','Count'], color='Reg_Users',
                             height=400)
                    st.plotly_chart(fig2,theme="streamlit",use_container_width=True)
                    
                    
                    
                
                if select_option == 'Map':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM statewise_map_users WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State','District','Reg_Users','App_Opens']].groupby(['State','District']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Reg_Users',
                                    hover_data=['State', 'Reg_Users','App_Opens'],
                                    projection="robinson",
                                    color_continuous_scale='piyg'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR STATEWISE USER MAP TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    
                    data = india_map_user.sort_values(by='Reg_Users',ascending=False).reset_index(drop=True)

                    fig2 = px.bar(data, x='District', y='Reg_Users',
                            hover_data=['Reg_Users','App_Opens'], color='App_Opens',
                            height=400)
                    st.plotly_chart(fig2,theme="streamlit",use_container_width=True)
                    
                    
                    
                if select_option == 'Top':
                    
                    df_agg = pd.read_sql(f"SELECT * FROM state_districtwise_top_users WHERE State = '{states}' AND Year = {year} AND Quarter = {Quarter}", con=my_connection)

                    #st.dataframe(df_agg)
                    
                    india_map_user = df_agg[['State','District','Reg_Users']].groupby(['State','District']).sum().reset_index()
                
                    fig = px.choropleth(india_map_user,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations='State',
                                    color='Reg_Users',
                                    hover_data=['State', 'Reg_Users'],
                                    projection="robinson",
                                    color_continuous_scale='delta'
                                    )
                    fig.update_geos(fitbounds = 'locations',visible = False )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    
                    st.subheader("MAP ANALYSIS FOR STATEWISE USER TOP TRANSACTIONS")
                
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)              
            

                    data = india_map_user.sort_values(by='Reg_Users',ascending=False).reset_index(drop=True)

                    fig2 = px.bar(data, x='District', y='Reg_Users',
                            hover_data=['Reg_Users'], color='Reg_Users',
                            labels={'Reg_Users':'Reg_Users'}, height=400)
                    st.plotly_chart(fig2,theme="streamlit",use_container_width=True)

                
    

def Insights():
    
    padding = 0
    # is a method from the Streamlit library that allows the user to set various page-level options for the app
    #st.set_page_config(page_title="PhonePe Pulse", layout="wide", page_icon="₹")
    # setting page title
    
    with st.sidebar:
    
        selected3 = streamlit_option.option_menu(
        menu_title = "Welcome to PhonePe Pulse India Insights",  
        options = ['Transaction Data Insights','User Data Insights'],
        default_index=0
        )

    
    if selected3 == 'Transaction Data Insights':
        
        
        options3 = ["Aggregated", "User", "Top"]
        st.subheader("Select the type of transaction data required")
        select = st.selectbox("",options3)
        
        if select == 'Aggregated':
            
            st.subheader("Payments")
            payment = st.selectbox("",[
                                'Recharge & bill payments',
                                'Peer-to-peer payments', 
                                'Merchant payments',
                                'Financial Services', 
                                'Others'])
            
            
            st.subheader("Select Quarter")
            quarter = st.selectbox('',('1','2','3','4'))
            
            st.subheader("Metric")
            metric = st.selectbox("",('Transaction_count','Transaction_amount'))
            
            df_agg = pd.read_sql(f"Select Distinct State,Payments, sum({metric}) as Total_Metric, Year from statewise_agg_transactions where Payments = '{payment}' AND Quarter = {quarter} AND Year BETWEEN 2018 AND 2022 group by State, Year ORDER BY State ASC", con=my_connection)

              
            insight_data = df_agg[['State','Payments','Total_Metric','Year']].groupby(['State','Year','Payments']).sum().reset_index()
            
            insight_fig = px.line(insight_data, x="Year", y="Total_Metric",color='State' ,title='Analysis Based on the type of Payment and Metric between 2018 - 2022 for each Quarter', markers=True,
                                  width=800, height=600)
            st.plotly_chart(insight_fig)
            
            insight_fig2 = px.sunburst(insight_data, path=['Year','State'] ,values='Total_Metric',color='State',
                                       width=800, height=600)
            
            st.plotly_chart(insight_fig2)
   

        
        
        if select == 'User':
            
            st.subheader("State")
            user_state = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
            selected_state = st.selectbox('',user_state)
            
            st.subheader("Select Quarter")
            quarter_user = st.selectbox('',('1','2','3','4'))
            
            st.subheader("Metric")
            metric_user = st.selectbox("",('Transaction_count','Transaction_amount'))
            
            df_map = pd.read_sql(f"Select Distinct State,District, sum({metric_user}) as Total_Metric, Year from statewise_map_transactions where State = '{selected_state}' AND Quarter = {quarter_user} AND Year BETWEEN 2018 AND 2022 group by State, Year,District ORDER BY State ASC", con=my_connection)
            
            insight_map = df_map[['State','District','Total_Metric','Year']].groupby(['State','Year','District','Total_Metric']).sum().reset_index()
            
            insight_map_fig = px.line(insight_map, x="Year", y="Total_Metric",color='District' ,title='Analysis Based on the State and Metric between 2018 - 2022 for each Quarter', 
                                      markers=True,
                                  width=800, height=600)
            st.plotly_chart(insight_map_fig)

            insight_map_fig2 = px.histogram(insight_map,x="District",y='Total_Metric' ,nbins=40,
                             color="Year",
                             title="Histogram of Total Metric by District",
                             opacity=0.7,
                             marginal="rug",
                             width=800, height=600)
            
            st.plotly_chart(insight_map_fig2)
            
          
          
          
            
        if select == 'Top':
            
        
            option1 = ["District", "Pincode"]
            st.subheader("Data based on District or Pincode")
            select1 = st.selectbox("",option1)
            
            if select1 == 'District':
            
                st.subheader("State")
                top_state = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
                select_state = st.selectbox('',top_state)
                
                st.subheader("Select Quarter")
                quarter_top = st.selectbox('',('1','2','3','4'))
                
                st.subheader("Metric")
                metric_top = st.selectbox("",('Transaction_count','Transaction_amount'))
                
                df_top = pd.read_sql(f"Select Distinct State,District, sum({metric_top}) as Total_Metric, Year from state_districtwise_top_transactions where State = '{select_state}' AND Quarter = {quarter_top} AND Year BETWEEN 2018 AND 2022 group by State, Year,District ORDER BY State ASC", con=my_connection)

                insight_top = df_top[['State','District','Total_Metric','Year']].groupby(['State','Year','District','Total_Metric']).sum().reset_index()
                
                insight_top_fig = px.line(insight_top, x="Year", y="Total_Metric",color='District' ,title='Analysis Based on the State and Metric between 2018 - 2022 for each Quarter', 
                                        markers=True,
                                    width=800, height=600)
                st.plotly_chart(insight_top_fig)
                
                insight_top_dt = px.scatter(insight_top, x="Year", y="Total_Metric",
	         size="Total_Metric", color="District",
                 hover_name='District',  size_max=60)
                #insight_top3.update_layout(xaxis=dict(tickmode='linear'))
                
                st.plotly_chart(insight_top_dt)
                
                insight_top_dt_1 = px.histogram(insight_top, x="Year", y="Total_Metric", color="District", marginal="rug",
                   hover_data=insight_top.columns)
                
                st.plotly_chart(insight_top_dt_1)
            
            if select1 == 'Pincode':
                
                st.subheader("State")
                top_state = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
                select_state = st.selectbox('',top_state)
                
                st.subheader("Select Quarter")
                quarter_top = st.selectbox('',('1','2','3','4'))
                
                st.subheader("Metric")
                metric_top = st.selectbox("",('Transaction_count','Transaction_amount'))
                
                df_top = pd.read_sql(f"Select Distinct State,Pincode, sum({metric_top}) as Total_Metric, Year from state_pincodewise_top_transactions where State = '{select_state}' AND Quarter = {quarter_top} AND Year BETWEEN 2018 AND 2022 group by State, Year,Pincode ORDER BY State ASC", con=my_connection)

                insight_top2 = df_top[['State','Pincode','Total_Metric','Year']].groupby(['State','Year','Pincode','Total_Metric']).sum().reset_index()
                
                insight_top_fig2 = px.line(insight_top2, x='Year', y='Total_Metric', color='Pincode', line_group='State',
              title='Total Metric by Year, State, and Pincode', markers=True)
                
                st.plotly_chart(insight_top_fig2)
                
                insight_top3 = px.scatter(insight_top2, x="Year", y="Total_Metric",
	         size="Total_Metric", color="Pincode",
                 hover_name='Pincode',  size_max=60)
                #insight_top3.update_layout(xaxis=dict(tickmode='linear'))
                
                st.plotly_chart(insight_top3)
                
                insight_top4 = px.histogram(insight_top2, x="Year", y="Total_Metric", color="Pincode", marginal="rug",
                   hover_data=insight_top2.columns)
                
                st.plotly_chart(insight_top4)
                
                
    if selected3 == 'User Data Insights': 
        opt = ["Aggregated", "User", "Top"]
        st.subheader("Select the type of transaction data required")
        select = st.selectbox("",opt)
        
        if select == 'Aggregated':
            
            brands = ['Xiaomi'
                    ,'Samsung'
                    ,'Vivo'
                    ,'Oppo'
                    ,'OnePlus'
                    ,'Realme'
                    ,'Apple'
                    ,'Motorola'
                    ,'Lenovo'
                    ,'Huawei'
                    ,'Others'
                    ,'Tecno'
                    ,'Gionee'
                    ,'Infinix'
                    ,'Asus'
                    ,'Micromax'
                    ,'HMD Global'
                    ,'Lava'
                    ,'COOLPAD'
                    ,'Lyf']
            st.subheader("Select Brand")
            selected_brand = st.selectbox('',brands)
            
            st.subheader("Select Quarter")
            quarter = st.selectbox('',('1','2','3','4'))
            
            st.subheader("Metric")
            metric = st.selectbox("",('Count','Percentage','Reg_Users','App_Opens'))
            
            user_insight = pd.read_sql(f"Select Distinct State,Brands, sum({metric}) as Total_Metric, Year from statewise_agg_users where Brands = '{selected_brand}' AND Quarter = {quarter} AND Year BETWEEN 2018 AND 2022 group by State,Brands,Year ORDER BY State ASC", con=my_connection)
            
            user_insight_data = user_insight[['State','Brands','Total_Metric','Year']].groupby(['State','Year','Brands']).sum().reset_index()
            
            user_insight_fig = px.line(user_insight_data, x="Year", y="Total_Metric",color='State' ,title='Analysis Based on the type of Brands and Metric between 2018 - 2022 for each Quarter', markers=True,
                                  width=700, height=500)
            st.plotly_chart(user_insight_fig)
            
            user_insight_fig2 = px.scatter(user_insight_data, x="Year", y="Total_Metric", color="State",
                 size='Total_Metric', hover_data=['State'])
            
            st.plotly_chart(user_insight_fig2)
     
     
 
 
 
        if select == 'User':
            
            st.subheader("State")
            users_state = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
            select_state = st.selectbox('',users_state)
            
            st.subheader("Select Quarter")
            quarter_user = st.selectbox('',('1','2','3','4'))
            
            st.subheader("Metric")
            metric_user = st.selectbox("",('Reg_Users','App_Opens'))
            
            map_user_insight = pd.read_sql(f"Select Distinct State,District, sum({metric_user}) as Total_Metric, Year from statewise_map_users where State = '{select_state}' AND Quarter = {quarter_user} AND Year BETWEEN 2018 AND 2022 group by State, Year,District ORDER BY State ASC", con=my_connection)
            
            insight_map_user = map_user_insight[['State','District','Total_Metric','Year']].groupby(['State','Year','District','Total_Metric']).sum().reset_index()
            
            insight_map_user_fig = px.line(insight_map_user, x="Year", y="Total_Metric",color='District' ,title='Analysis Based on the State and Metric between 2018 - 2022 for each Quarter', 
                                      markers=True,
                                  width=800, height=600)
            st.plotly_chart(insight_map_user_fig)

            insight_map_user_fig2 = px.histogram(insight_map_user,x="District",y='Total_Metric' ,nbins=40,
                             color="Year",
                             title="Histogram of Total Metric by District",
                             opacity=0.7,
                             marginal="rug",
                             width=800, height=600)
            
            st.plotly_chart(insight_map_user_fig2)
            
 
 
 
 
 
        if select == 'Top':
            opt1 = ["District", "Pincode"]
            st.subheader("Data based on District or Pincode")
            select2 = st.selectbox("",opt1)
 

            if select2 == 'District':
            
                st.subheader("State")
                top_state_user = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
                select_top_state = st.selectbox('',top_state_user)
                
                st.subheader("Select Quarter")
                quarter_top_user = st.selectbox('',('1','2','3','4'))
                
                df_top_user = pd.read_sql(f"Select Distinct State,District, sum(Reg_Users) as Total_Reg_Users , Year from state_districtwise_top_users where State = '{select_top_state}' AND Quarter = {quarter_top_user} AND Year BETWEEN 2018 AND 2022 group by State, Year,District ORDER BY State ASC", con=my_connection)

                insight_top_user = df_top_user[['State','District','Total_Reg_Users','Year']].groupby(['State','Year','District','Total_Reg_Users']).sum().reset_index()
                
                insight_top_fig = px.line(insight_top_user, x="Year", y="Total_Reg_Users",color='District' ,title='Analysis Based on the State and Metric between 2018 - 2022 for each Quarter', 
                                        markers=True,
                                    width=800, height=600)
                st.plotly_chart(insight_top_fig)
                
                insight_top_user_dt = px.scatter(insight_top_user, x="Year", y="Total_Reg_Users",
	         size="Total_Reg_Users", color="District",
                 hover_name='District',  size_max=60)
                #insight_top3.update_layout(xaxis=dict(tickmode='linear'))
                
                st.plotly_chart(insight_top_user_dt)
                
                insight_top_user_dt1 = px.histogram(insight_top_user, x="Year", y="Total_Reg_Users", color="District", marginal="rug",
                   hover_data=insight_top_user.columns)
                
                st.plotly_chart(insight_top_user_dt1)
 

            if select2 == 'Pincode':
                st.subheader("State")
                top_state = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli & Daman & Diu','NCT of Delhi','Goa','Gujarat','Haryana','Jammu & Kashmir','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','WestBengal','Odisha']
                select_state = st.selectbox('',top_state)
                
                st.subheader("Select Quarter")
                quarter_top = st.selectbox('',('1','2','3','4'))
                
                              
                df_top_pin = pd.read_sql(f"Select Distinct State,Pincode, sum(Reg_Users) as Total_Reg_Users, Year from state_pincodewise_top_users where State = '{select_state}' AND Quarter = {quarter_top} AND Year BETWEEN 2018 AND 2022 group by State, Year,Pincode ORDER BY State ASC", con=my_connection)

                insight_top_pin = df_top_pin[['State','Pincode','Total_Reg_Users','Year']].groupby(['State','Year','Pincode','Total_Reg_Users']).sum().reset_index()
                
                insight_top_pin_fig = px.line(insight_top_pin, x='Year', y='Total_Reg_Users', color='Pincode', line_group='State',
              title='Analysis Based on the State and Metric between 2018 - 2022 for each Quarter', markers=True)
                
                st.plotly_chart(insight_top_pin_fig)
                
                insight_top_pin_fig2 = px.scatter(insight_top_pin, x="Year", y="Total_Reg_Users",
	         size="Total_Reg_Users", color="Pincode",
                 hover_name='Pincode',  size_max=60)
                #insight_top3.update_layout(xaxis=dict(tickmode='linear'))
                
                st.plotly_chart(insight_top_pin_fig2)
                
                insight_top_pin_fig3 = px.histogram(insight_top_pin, x="Year", y="Total_Reg_Users", color="Pincode", marginal="rug",
                   hover_data=insight_top_pin.columns)
                
                st.plotly_chart(insight_top_pin_fig3)
 
 

def Fun_Facts():


    with st.sidebar:
        selected_fact = streamlit_option.option_menu(
        menu_title = "Welcome to PhonePe Pulse India Fun Facts",  
        options = [
                    "Top 10 states based on amount of transaction",   
                "Least 10 states based on amount of transaction",
                "Top 10 mobile brands based on percentage of transaction",
                "Least 10 mobile brands based on percentage of transaction",
                "Top 10 mobile brands based on count of transactions",
                "Least 10 mobile brands based on count of transactions",
                "Top 10 States based on Registered-users",
                "Least 10 States based on Registered-users",
                "Top 10 Districts based on Registered-users",
                "Least 10 Districts based on Registered-users",
                "Top 10 Pincodes based on Registered-users",
                "Least 10 Pincodes based on Registered-users",
                "Top 10 States based on App_Opens",
                "Least 10 States based on App_Opens",
                "Top 10 Districts based on App_Opens",
                "Least 10 Districts based on App_Opens",
                "Top 10 Districts based on amount of transaction",
                "Least 10 Districts based on amount of transaction",
                "Top Transaction Amounts based on the payments",
                "Highest Transaction Amount based on Payments",
                "Lowest Transaction Amount based on Payments"],
        default_index=0
        )
                
    if selected_fact == "Top 10 states based on amount of transaction":
        cursor.execute(
            "SELECT distinct State, sum(Transaction_amount) AS Total_Transaction_amount FROM state_districtwise_top_transactions where Year between 2018 AND 2022 AND Quarter BETWEEN 1 AND 4 group by State ORDER BY Total_Transaction_amount DESC LIMIT 10")  
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Top 10 states based amount of transaction")
        fig = px.bar(df, x="State", y="Transaction_amount", color="State")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["State"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['State'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Transaction Amounts by State'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="State", y="Transaction_amount", color="State",
                 size='Transaction_amount', hover_data=['State'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Least 10 states based on amount of transaction":
        cursor.execute(
            "SELECT distinct State, sum(Transaction_amount) AS Total_Transaction_amount FROM state_districtwise_top_transactions where Year between 2018 AND 2022 AND Quarter BETWEEN 1 AND 4 group by State ORDER BY Total_Transaction_amount ASC LIMIT 10")  
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Least 10 states based on amount of transaction")
        fig_1 = px.bar(df1, x="State", y="Transaction_amount", color="State")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df1["State"], y=df1["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df1['State'], values=df1['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Transaction Amounts by State'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df1, x="State", y="Transaction_amount", color="State",
                 size='Transaction_amount', hover_data=['State'])
            
        st.plotly_chart(user_fig)

                    
    elif selected_fact == "Top 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT Brands,sum(Percentage) as Total_Percentage FROM statewise_agg_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Brands ORDER BY Total_Percentage DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Brands', 'Percentage'])
        st.title("Top 10 mobile brands based on percentage of transaction")
        fig_1 = px.bar(df2, x="Brands", y="Percentage", color='Brands')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["Brands"], y=df2["Percentage"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Brands'], values=df2['Percentage'], name='Percentage of Transactions',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Brands based on Percentage of transaction '}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Brands", y="Percentage", color="Brands",
                 size='Percentage', hover_data=['Brands'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Least 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT Brands,sum(Percentage) as Total_Percentage FROM statewise_agg_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Brands ORDER BY Total_Percentage ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Brands', 'Percentage'])
        st.title("Least 10 mobile brands based on percentage of transaction")
        fig_1 = px.bar(df2, x="Brands", y="Percentage", color='Brands')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["Brands"], y=df2["Percentage"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Brands'], values=df2['Percentage'], name='Percentage of Transactions',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Brands based on Percentage of transaction '}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Brands", y="Percentage", color="Brands",
                 size='Percentage', hover_data=['Brands'])
            
        st.plotly_chart(user_fig)
    
    elif selected_fact == "Top 10 mobile brands based on count of transactions":
        cursor.execute("SELECT DISTINCT Brands,sum(Count) as Total_Count FROM statewise_agg_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Brands ORDER BY Total_Count DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Brands', 'Count'])
        st.title("Top 10 mobile brands based on count of transaction")
        fig_1 = px.bar(df2, x="Brands", y="Count", color='Brands')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["Brands"], y=df2["Count"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Brands'], values=df2['Count'], name='Count of Transactions',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Brands based on Count of transactions '}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Brands", y="Count", color="Brands",
                 size=df2['Count'].apply(int), hover_data=['Brands'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Least 10 mobile brands based on count of transactions":
        cursor.execute("SELECT DISTINCT Brands,sum(Count) as Total_Count FROM statewise_agg_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Brands ORDER BY Total_Count ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Brands', 'Count'])
        st.title("Least 10 mobile brands based on count of transaction")
        fig_1 = px.bar(df2, x="Brands", y="Count", color='Brands')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["Brands"], y=df2["Count"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Brands'], values=df2['Count'], name='Count of Transactions',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Brands based on Count of transactions '}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Brands", y="Count", color="Brands",
                 size=df2['Count'].apply(int), hover_data=['Brands'])
            
        st.plotly_chart(user_fig)
    
    
    elif selected_fact =="Top 10 States based on Registered-users":
        cursor.execute("SELECT DISTINCT State,sum(Reg_Users) as Total_Reg_Users FROM state_districtwise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY State ORDER BY Total_Reg_Users DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Reg_Users'])
        st.title("Top 10 States based on Registered-users")
        fig_1 = px.bar(df2, x="State", y="Reg_Users", color='State')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["State"], y=df2["Reg_Users"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['State'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'States based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="State", y="Reg_Users", color="State",
                 size=df2['Reg_Users'].apply(int), hover_data=['State'])
            
        st.plotly_chart(user_fig)
    
    
    elif selected_fact == "Least 10 States based on Registered-users":
        cursor.execute("SELECT DISTINCT State,sum(Reg_Users) as Total_Reg_Users FROM state_districtwise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY State ORDER BY Total_Reg_Users ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Reg_Users'])
        st.title("Least 10 States based on Registered-users")
        fig_1 = px.bar(df2, x="State", y="Reg_Users", color='State')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["State"], y=df2["Reg_Users"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['State'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'States based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="State", y="Reg_Users", color="State",
                 size=df2['Reg_Users'].apply(int), hover_data=['State'])
            
        st.plotly_chart(user_fig)
    
    
    elif selected_fact == "Top 10 Districts based on Registered-users":
        cursor.execute("SELECT DISTINCT District,sum(Reg_Users) as Total_Reg_Users FROM state_districtwise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY District ORDER BY Total_Reg_Users DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['District', 'Reg_Users'])
        st.title("Top 10 Districts based on Registered-users")
        fig_1 = px.bar(df2, x="District", y="Reg_Users", color='District')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["District"], y=df2["Reg_Users"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['District'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Districts based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="District", y="Reg_Users", color="District",
                 size=df2['Reg_Users'].apply(int), hover_data=['District'])
            
        st.plotly_chart(user_fig)
    
    
    elif selected_fact == "Least 10 Districts based on Registered-users":
        
        cursor.execute("SELECT DISTINCT District,sum(Reg_Users) as Total_Reg_Users FROM state_districtwise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY District ORDER BY Total_Reg_Users ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['District', 'Reg_Users'])
        st.title("Least 10 Districts based on Registered-users")
        fig_1 = px.bar(df2, x="District", y="Reg_Users", color='District')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["District"], y=df2["Reg_Users"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['District'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Districts based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="District", y="Reg_Users", color="District",
                 size=df2['Reg_Users'].apply(int), hover_data=['District'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Top 10 Pincodes based on Registered-users":
        cursor.execute("SELECT DISTINCT Pincode,sum(Reg_Users) as Total_Reg_Users FROM state_pincodewise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Pincode ORDER BY Total_Reg_Users DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Reg_Users'])
        st.title("Top 10 Pincodes based on Registered-users")
        fig_1 = px.bar(df2, x='Pincode', y='Reg_Users',
             title='Top 10 Pincodes by Total Registered Users',
             labels={'Pincode': 'Pincode', 'Reg_Users': 'Total Registered Users'},color='Pincode')
        
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Pincode'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Pincodes based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Pincode", y="Reg_Users", color="Pincode",
                 size=df2['Reg_Users'].apply(int), hover_data=['Pincode'])
            
        st.plotly_chart(user_fig)
        
        
    elif selected_fact == "Least 10 Pincodes based on Registered-users":
        cursor.execute("SELECT DISTINCT Pincode,sum(Reg_Users) as Total_Reg_Users FROM state_pincodewise_top_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY Pincode ORDER BY Total_Reg_Users ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Reg_Users'])
        st.title("Least 10 Pincodes based on Registered-users")
        fig_1 = px.bar(df2, x='Pincode', y='Reg_Users',
             title='Top 10 Pincodes by Total Registered Users',
             labels={'Pincode': 'Pincode', 'Reg_Users': 'Total Registered Users'},color='Pincode')
        
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['Pincode'], values=df2['Reg_Users'], name='Count of Reg_Users',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Pincodes based on Count of Reg_Users'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="Pincode", y="Reg_Users", color="Pincode",
                 size=df2['Reg_Users'].apply(int), hover_data=['Pincode'])
            
        st.plotly_chart(user_fig)
    
    
    elif selected_fact == "Top 10 States based on App_Opens":
        cursor.execute("SELECT DISTINCT State,sum(App_Opens) as Total_App_Opens FROM statewise_map_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY State ORDER BY Total_App_Opens DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['State', 'App_Opens'])
        st.title("Top 10 States based on App_Opens")
        fig_1 = px.bar(df2, x="State", y="App_Opens", color='State')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["State"], y=df2["App_Opens"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['State'], values=df2['App_Opens'], name='Count of App_Opens',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'States based on Count of App_Opens'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="State", y="App_Opens", color="State",
                 size=df2['App_Opens'].apply(int), hover_data=['State'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Least 10 States based on App_Opens":
        cursor.execute("SELECT DISTINCT State,sum(App_Opens) as Total_App_Opens FROM statewise_map_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY State ORDER BY Total_App_Opens ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['State', 'App_Opens'])
        st.title("Least 10 States based on App_Opens")
        fig_1 = px.bar(df2, x="State", y="App_Opens", color='State')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["State"], y=df2["App_Opens"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['State'], values=df2['App_Opens'], name='Count of App_Opens',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'States based on Count of App_Opens'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="State", y="App_Opens", color="State",
                 size=df2['App_Opens'].apply(int), hover_data=['State'])
            
        st.plotly_chart(user_fig)
        

    elif selected_fact == "Top 10 Districts based on App_Opens":
        cursor.execute("SELECT DISTINCT District,sum(App_Opens) as Total_App_Opens FROM statewise_map_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY District ORDER BY Total_App_Opens DESC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['District', 'App_Opens'])
        st.title("Top 10 Districts based on App_Opens")
        fig_1 = px.bar(df2, x="District", y="App_Opens", color='District')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["District"], y=df2["App_Opens"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['District'], values=df2['App_Opens'], name='Count of App_Opens',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Districts based on Count of App_Opens'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="District", y="App_Opens", color="District",
                 size=df2['App_Opens'].apply(int), hover_data=['District'])
            
        st.plotly_chart(user_fig)
        
    elif selected_fact == "Least 10 Districts based on App_Opens":
        cursor.execute("SELECT DISTINCT District,sum(App_Opens) as Total_App_Opens FROM statewise_map_users where Year in (2018,2019,2020,2021,2022) AND Quarter in (1,2,3,4) GROUP BY District ORDER BY Total_App_Opens ASC LIMIT 10")
        df2 = pd.DataFrame(cursor.fetchall(), columns=['District', 'App_Opens'])
        st.title("Least 10 Districts based on App_Opens")
        fig_1 = px.bar(df2, x="District", y="App_Opens", color='District')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig_1, theme=None, use_container_width=True)
            
        fig_2 = go.Figure(data=go.Scatter(x=df2["District"], y=df2["App_Opens"], mode='lines', fillcolor="darkmagenta"))
        st.plotly_chart(fig_2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart_1 = go.Pie(labels=df2['District'], values=df2['App_Opens'], name='Count of App_Opens',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Districts based on Count of App_Opens'}

        pie_fig_1 = go.Figure(data=[pie_chart_1], layout=layout)

        st.plotly_chart(pie_fig_1, use_container_width=True)
        
        user_fig = px.scatter(df2, x="District", y="App_Opens", color="District",
                 size=df2['App_Opens'].apply(int), hover_data=['District'])
            
        st.plotly_chart(user_fig)
    
    
    
    elif selected_fact == "Top 10 Districts based on amount of transaction":
        cursor.execute(
            "SELECT distinct District, sum(Transaction_amount) AS Total_Transaction_amount FROM state_districtwise_top_transactions where Year between 2018 AND 2022 AND Quarter BETWEEN 1 AND 4 group by District ORDER BY Total_Transaction_amount DESC LIMIT 10")  
        df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Top 10 Districts based amount of transaction")
        fig = px.bar(df, x="District", y="Transaction_amount", color="District")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["District"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['District'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Transaction Amounts by District'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="District", y="Transaction_amount", color="District",
                 size='Transaction_amount', hover_data=['District'])
            
        st.plotly_chart(user_fig)   


    elif selected_fact == "Least 10 Districts based on amount of transaction":
        cursor.execute(
            "SELECT distinct District, sum(Transaction_amount) AS Total_Transaction_amount FROM state_districtwise_top_transactions where Year between 2018 AND 2022 AND Quarter BETWEEN 1 AND 4 group by District ORDER BY Total_Transaction_amount ASC LIMIT 10")  
        df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Least 10 Districts based amount of transaction")
        fig = px.bar(df, x="District", y="Transaction_amount", color="District")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["District"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['District'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Transaction Amounts by District'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="District", y="Transaction_amount", color="District",
                 size='Transaction_amount', hover_data=['District'])
            
        st.plotly_chart(user_fig)   


    elif selected_fact == "Top Transaction Amounts based on the payments":
        cursor.execute(
            "SELECT DISTINCT Payments,sum(Transaction_amount) AS Total_Transaction_amount FROM statewise_agg_transactions where Year BETWEEN 2018 and 2022 AND Quarter BETWEEN 1 AND 4 GROUP BY Payments ORDER BY Total_Transaction_amount DESC")        
        df = pd.DataFrame(cursor.fetchall(), columns=['Payments', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Top Transaction Amounts based on the payments")
        fig = px.bar(df, x="Payments", y="Transaction_amount", color="Payments")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["Payments"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['Payments'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Transaction Amounts by Payments'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="Payments", y="Transaction_amount", color="Payments",
                 size='Transaction_amount', hover_data=['Payments'])
            
        st.plotly_chart(user_fig)   
        

    elif selected_fact == "Highest Transaction Amount based on Payments":
        cursor.execute("SELECT DISTINCT Payments,MAX(Transaction_amount) AS Total_Transaction_amount FROM statewise_agg_transactions where Year BETWEEN 2018 and 2022 AND Quarter BETWEEN 1 AND 4 GROUP BY Payments ORDER BY Total_Transaction_amount")        
        
        df = pd.DataFrame(cursor.fetchall(), columns=['Payments', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Highest Transaction Amounts based on the payments")
        fig = px.bar(df, x="Payments", y="Transaction_amount", color="Payments")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["Payments"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['Payments'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Highest Transaction Amounts by Payments'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="Payments", y="Transaction_amount", color="Payments",
                 size='Transaction_amount', hover_data=['Payments'])
            
        st.plotly_chart(user_fig)
        

    elif selected_fact == "Lowest Transaction Amount based on Payments":
        cursor.execute("SELECT DISTINCT Payments,MIN(Transaction_amount) AS Total_Transaction_amount FROM statewise_agg_transactions where Year BETWEEN 2018 and 2022 AND Quarter BETWEEN 1 AND 4 GROUP BY Payments ORDER BY Total_Transaction_amount")        
        
        df = pd.DataFrame(cursor.fetchall(), columns=['Payments', 'Transaction_amount'])
        
        #st.dataframe(df)
        
        st.title("Lowest Transaction Amounts based on the payments")
        fig = px.bar(df, x="Payments", y="Transaction_amount", color="Payments")
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)
            
        fig2 = go.Figure(data=go.Scatter(x=df["Payments"], y=df["Transaction_amount"], mode='lines'))
        st.plotly_chart(fig2,use_container_width=True)
 
        
        # Create a pie chart of the transaction amounts
        pie_chart = go.Pie(labels=df['Payments'], values=df['Transaction_amount'], name='Transaction Amounts',
                            marker=dict(colors=['#FFA07A', '#98FB98', '#87CEFA', '#F08080', '#D3D3D3']))
        layout = {'title': 'Lowest Transaction Amounts by Payments'}

        pie_fig = go.Figure(data=[pie_chart], layout=layout)

        st.plotly_chart(pie_fig, use_container_width=True)
        
        user_fig = px.scatter(df, x="Payments", y="Transaction_amount", color="Payments",
                 size='Transaction_amount', hover_data=['Payments'])
            
        st.plotly_chart(user_fig)


if __name__ == '__main__':
    #set_page_config(Image.open("Phonepe_logo.png"), '#3498db')
    #display_navigation()
    selected1 = display_navigation()
    if selected1 == "Home":
        Home()
        
    elif selected1 == "About":
        About()
        
    elif selected1 == "Contact":
        Contact()
    
    elif selected1 == "Overview of Insights":
        
        Dashboard()
        
    elif selected1 ==  "Analyze Insights":
        Insights()
    
    
    elif selected1 == "Discoveries":
        Fun_Facts()
        
        
        
    #Dashboard()
    
    #Insights()
    
    #Fun_Facts()