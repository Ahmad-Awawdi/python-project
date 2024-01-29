# this project is about NYC 311 Customer Service Requests Analysis

# I analysis Tasks like:

#- convert the columns ‘Created Date’ and Closed Date’ to datetime datatype and create a new column
# ‘Request_Closing_Time’ as the time elapsed between request creation and request closing.

#- Provide major insights/patterns that you can offer in a visual format (graphs or tables); 
#  at least 4 major conclusions that you can come up with after generic data mining.



import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
nyc=pd.read_csv('NYC311data.csv')
nyc.head(10)


# In[6]:


missing_values=nyc.isna().sum()
missing_values


# In[ ]:


nyc['Created Date']=pd.to_datetime(nyc['Created Date'])
nyc['Closed Date']=pd.to_datetime(nyc['Closed Date'])
nyc.head(3)


# In[41]:


nyc['Request_Closing_Time']=nyc['Closed Date']-nyc['Created Date']
nyc


# In[58]:


nyc['Complaint Type'].values


# In[103]:


complaint_counts = nyc['Complaint Type'].value_counts()
complaint_counts


# In[77]:


most_frequent_problem = complaint_counts.idxmax()
most_frequent_problem


# In[119]:


print("Problem Counts:")
print(complaint_counts)
print("Most Frequent Problem:", most_frequent_problem)


# In[92]:


import matplotlib as mpl
import matplotlib.pyplot as plt


# In[115]:


specific_items = ['Blocked Driveway', 'Illegal Parking']

# Filter the DataFrame for the specific items
specific_item_data = nyc[nyc['Complaint Type'].isin(specific_items)]

# Count the occurrences of each complaint type
complaint_counts = nyc['Complaint Type'].value_counts()

# Remove the specific items from the counts 
rest_of_complaints = complaint_counts.drop(specific_items)

# Combine 'Rest of Complaints' with the specific items
combined_counts = rest_of_complaints.append(pd.Series({item: len(nyc[nyc['Complaint Type'] == item]) for item in specific_items}))

combined_counts.plot(kind='bar')
plt.ylabel('Number of Complaints')
plt.title(f'Comparison of Specific Items with Rest of Complaints')
plt.show()


# In[114]:


specific_items = ['Blocked Driveway', 'Illegal Parking']

# Filter the DataFrame for the specific items
specific_item_data = nyc[nyc['Complaint Type'].isin(specific_items)]

# Count the occurrences of each complaint type
complaint_counts = nyc['Complaint Type'].value_counts()

# Remove the specific items from the counts
rest_of_complaints = complaint_counts.drop(specific_items)

plt.bar(['Rest of Complaints'] + specific_items, [rest_of_complaints.sum()] + [len(specific_item_data[specific_item_data['Complaint Type'] == item]) for item in specific_items])
plt.ylabel('Number of Complaints')
plt.title('Comparison of Specific Items with Rest of Complaints')
plt.show()


# In[2]:


df1=nyc.groupby(['City','Complaint Type']).size().unstack().fillna(0)



# In[9]:


df = pd.DataFrame(nyc)
selected_columns = ['Complaint Type','City']
result_df = df[selected_columns]
print(result_df)


# In[29]:


com_per=nyc['Complaint Type'].value_counts()
com_per
complaint_city= (selected_columns,com_per)
complaint_city


# In[35]:


Complaint_Type=nyc['Complaint Type']
nyc.City


# In[61]:


test1='this is test'
test2=[1,2,3,4]
print(test1.split())
print(list(test1))
print(tuple(test1))
print(str(test1))
print(test1[0:1])


# In[76]:


df=nyc.groupby(['City','Complaint Type']).size().unstack().fillna(0)
df


# In[77]:


df.plot.bar(figsize=(15,10), stacked=True)
plt.ylabel('Number of Complaints')
plt.title('Number of complaints vs. City')


# In[108]:


DataFrame=nyc.groupby(['City','Status']).size().unstack().fillna(0)

DataFrame.sort_values(by='Closed', ascending=False).head()


# In[115]:


###אילו תלונות בד״כ נסגרות ו נפתרות 

CityStat=nyc.groupby(['Complaint Type','Status']).size().unstack().fillna(0)
CityStat.sort_values(by='Open', ascending=False).head()


# In[19]:


### by type of problem and treating department

complaint_counts = nyc.groupby(['Complaint Type','Agency Name']).size().reset_index(name='Count')

complaint_counts.head(5)


# In[21]:


complaint_counts.plot.bar(figsize=(15,10), stacked=True)
complaint_counts.drop_duplicates()
plt.ylabel('Count')
plt.title('Agency Name')


# In[17]:


###Issue status and quantity
complaint_counts = nyc.groupby(['Complaint Type', 'Status']).size().reset_index(name='Count')

complaint_counts.head(10)


# In[37]:


###מתי אנשים נוהגים להתלונן


nyc['Month'] = nyc['Created Date'].dt.month
nyc['DayOfWeek'] = nyc['Created Date'].dt.day_name()

# per month
complaints_by_month = nyc.groupby('Month')['Complaint Type'].count()

# per day of the week
complaints_by_day = nyc.groupby('DayOfWeek')['Complaint Type'].count()

# Plotting
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# Plotting complaints by month
axes[0].bar(complaints_by_month.index, complaints_by_month.values)
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Number of Complaints')
axes[0].set_title('Number of Complaints by Month')

# Plotting complaints by day of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
axes[1].bar(complaints_by_day.reindex(days_order).index, complaints_by_day.reindex(days_order).values)
axes[1].set_xlabel('Day of the Week')
axes[1].set_ylabel('Number of Complaints')
axes[1].set_title('Number of Complaints by Day of the Week')

plt.tight_layout()
plt.show()


# In[60]:


###בכמה זמן בד״כ התלונות נסגרות

nyc['Request_Closing_Time'] = pd.to_timedelta(nyc['Request_Closing_Time'])
time_close=nyc['Request_Closing_Time']
merged_df = pd.concat([complaint_counts, time_close], axis=1)

closed_df = merged_df[merged_df['Status'] == 'Closed']
closed_df_sorted = closed_df.sort_values(by='Request_Closing_Time', ascending=False)

closed_df_sorted

