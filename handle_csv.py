from datetime import date
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import os



class Datasheet:
    def __init__(self, file):
        self.file = file
  
    def order_cluster(self, cluster_field_name, target_field_name,df,ascending):
        df_new = df.groupby(cluster_field_name)[target_field_name].mean().reset_index()
        df_new = df_new.sort_values(by=target_field_name,ascending=ascending).reset_index(drop=True)
        df_new['index'] = df_new.index
        df_final = pd.merge(df,df_new[[cluster_field_name,'index']], on=cluster_field_name)
        df_final = df_final.drop([cluster_field_name],axis=1)
        df_final = df_final.rename(columns={"index":cluster_field_name})
        return df_final



    def compute(self):
        tx_data = self.file        
        tx_data['InvoiceDate'] = pd.to_datetime(tx_data['InvoiceDate'], format="%d-%m-%Y %H:%M").dt.date
        tx_uk = tx_data.query("Country=='United Kingdom'").reset_index(drop=True)
        tx_3m = tx_uk[(tx_uk.InvoiceDate < date(2011,6,1)) & (tx_uk.InvoiceDate >= date(2011,3,1))].reset_index(drop=True)
        tx_user = pd.DataFrame(tx_3m['CustomerID'].unique())
        tx_user.columns = ['CustomerID']


        tx_max_purchase = tx_3m.groupby('CustomerID').InvoiceDate.max().reset_index()
        tx_max_purchase.columns = ['CustomerID','MaxPurchaseDate']
        tx_max_purchase['Recency'] = (tx_max_purchase['MaxPurchaseDate'].max() - tx_max_purchase['MaxPurchaseDate']).dt.days
        tx_user = pd.merge(tx_user, tx_max_purchase[['CustomerID','Recency']], on='CustomerID')
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(tx_user[['Recency']])
        tx_user['RecencyCluster'] = kmeans.predict(tx_user[['Recency']])
        tx_user = self.order_cluster('RecencyCluster', 'Recency',tx_user,False)

        tx_frequency = tx_3m.groupby('CustomerID').InvoiceDate.count().reset_index()
        tx_frequency.columns = ['CustomerID','Frequency']
        tx_user = pd.merge(tx_user, tx_frequency, on='CustomerID')
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(tx_user[['Frequency']])
        tx_user['FrequencyCluster'] = kmeans.predict(tx_user[['Frequency']])
        tx_user = self.order_cluster('FrequencyCluster', 'Frequency',tx_user,True)

        tx_3m['Revenue'] = tx_3m['UnitPrice'] * tx_3m['Quantity']
        tx_revenue = tx_3m.groupby('CustomerID').Revenue.sum().reset_index()
        tx_user = pd.merge(tx_user, tx_revenue, on='CustomerID')
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(tx_user[['Revenue']])
        tx_user['RevenueCluster'] = kmeans.predict(tx_user[['Revenue']])
        tx_user = self.order_cluster('RevenueCluster', 'Revenue',tx_user,True)

        tx_user['OverallScore'] = tx_user['RecencyCluster'] + tx_user['FrequencyCluster'] + tx_user['RevenueCluster']
        tx_user['Segment'] = 'Low-Value'
        tx_user.loc[tx_user['OverallScore']>2,'Segment'] = 'Mid-Value' 
        tx_user.loc[tx_user['OverallScore']>4,'Segment'] = 'High-Value'

        tx_user = tx_user.sort_values(by=['OverallScore'], ascending=False)

        directory = os.getcwd()

        #print(directory + '\\customer_lifetime_value.csv')
        tx_user.to_csv(directory + '\\customer_lifetime_value.csv', index=False)