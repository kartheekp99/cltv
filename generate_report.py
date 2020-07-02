import pandas as pd

class Report:
    def __init__(self,file):
        self.file=file

    def generate(self):
        report_data={}
        data_count  = pd.read_csv("customer_lifetime_value.csv")
        data_country = self.file
        countries = data_country['Country'].value_counts().iloc[:10]
        count = data_count['Segment'].value_counts()

        clv={}
        for i in count.index:
            clv[i[:i.index('-')]+" "+"Clv"] = int(count[i])
        report_data['clv']=clv


        countries_data = {'countries':[], 'customers':[]}
        for i in countries.index:
            countries_data['countries'].append(i)
            countries_data['customers'].append(int(countries[i]))
        report_data['countries']=countries_data

        
        monthly_revenue = {'Date':[],'Revenue':[]}
        data_country['InvoiceDate'] = pd.to_datetime(data_country['InvoiceDate'])
        data_country['InvoiceYearMonth'] = data_country['InvoiceDate'].map(lambda date: str(date.year) + "-" + str(date.month).zfill(2))
        data_country['Revenue'] = data_country['UnitPrice'] * data_country['Quantity']
        revenue = data_country.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()
        for i in revenue['InvoiceYearMonth']:
            monthly_revenue['Date'].append(i)
        for i in revenue['Revenue']:    
            monthly_revenue['Revenue'].append(int(i))
        report_data['monthly_revenue'] = monthly_revenue


        monthly_active = {'Date':[] ,'Active':[]}
        uk_data = data_country.query("Country=='United Kingdom'").reset_index(drop=True)
        active = uk_data.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
        for i in active['InvoiceYearMonth']:
            monthly_active['Date'].append(i)
        for i in active['CustomerID']:
            monthly_active['Active'].append(int(i))
        report_data['monthly_active'] = monthly_active


        new_exist = {'Date':[],'New':[],'Exist':[]}
        min_purchase = uk_data.groupby('CustomerID').InvoiceDate.min().reset_index()
        min_purchase.columns = ['CustomerID','MinPurchaseDate']
        min_purchase['MinPurchaseYearMonth'] = min_purchase['MinPurchaseDate'].map(lambda date: str(date.year) + "-" + str(date.month).zfill(2))
        uk_data = pd.merge(uk_data, min_purchase, on='CustomerID')
        uk_data['UserType'] = 'New'
        uk_data.loc[uk_data['InvoiceYearMonth']>uk_data['MinPurchaseYearMonth'],'UserType'] = 'Existing'
        user_type_revenue = uk_data.groupby(['InvoiceYearMonth','UserType'])['Revenue'].sum().reset_index()
        user_type_revenue = user_type_revenue.query("InvoiceYearMonth != 2010-12 and InvoiceYearMonth != 2011-12")
        new = user_type_revenue.query("UserType=='New'").reset_index(drop=True)
        exist = user_type_revenue.query("UserType=='Existing'").reset_index(drop=True)
        for i in new['InvoiceYearMonth']:
            new_exist['Date'].append(i)
        for i in new['Revenue']:
            new_exist['New'].append(int(i))
        for i in exist['Revenue']:
            new_exist['Exist'].append(int(i))
        report_data['New_Exist']=new_exist
        

        return report_data
