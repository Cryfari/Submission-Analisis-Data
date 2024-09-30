import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

<<<<<<< HEAD
day_df = pd.read_csv("dashboard\\day_data.csv")
hour_df = pd.read_csv("dashboard\\hour_data.csv")
=======
day_df = pd.read_csv("dashboard/day_data.csv")
hour_df = pd.read_csv("dashboard/hour_data.csv")
>>>>>>> 9de2045 (update-path)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()
 
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Dashboard')

col1, col2 = st.columns(2)

with col1:
    total_orders = day_df.cnt.sum()
    st.metric("Total rental", value=total_orders)
with col2:
    total_orders = day_df.cnt.sum()
    total_registered_order = day_df.registered.sum()
    percent = round((total_registered_order/total_orders)*100, 2)
    st.metric("persentase member", value=str(percent)+"%")


main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]

hour_main_df = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                (hour_df["dteday"] <= str(end_date))]

st.subheader('Rental Harian')
 
col1, col2 = st.columns(2)
 
with col1:
    total_orders = main_df.cnt.sum()
    st.metric("Total rental", value=total_orders)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(main_df['dteday'], main_df['cnt'], 
    color="#90CAF9")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.subheader('Rental Bulanan')
fig, ax = plt.subplots(figsize=(16, 8))
# ax.plot(main_df['mnth'], main_df['cnt'], 
#     color="#90CAF9")
sns.pointplot(x=main_df['mnth'], y=main_df['cnt'], hue=main_df['yr'])
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xlabel('Bulan', fontsize=20)
plt.ylabel('Rata-rata Temperatur', fontsize=20)
plt.legend(title='Year')
 
st.pyplot(fig)


st.subheader('Temperatur perbulan')
fig, ax = plt.subplots(figsize=(16, 8))
# ax.plot(main_df['mnth'], main_df['cnt'], 
#     color="#90CAF9")
sns.pointplot(x=main_df['mnth'], y=main_df['atemp'], hue=main_df['yr'])
plt.xlabel('Bulan', fontsize=20)
plt.ylabel('Rata-rata Temperatur', fontsize=20)
plt.legend(title='Year')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.subheader('Rental permusim')
season_hour_cnt = hour_main_df.groupby(['season', 'hr'])['cnt'].mean().unstack()

# Plot the line graph for each season
fig, ax = plt.subplots(figsize=(16, 8))
for season in season_hour_cnt.index:
  plt.plot(season_hour_cnt.columns, season_hour_cnt.loc[season], label=season)

plt.xlabel('Hour of the Day', fontsize=20)
plt.ylabel('Average Bike Rentals', fontsize=20)
plt.xticks(range(0, 24))
plt.legend()
plt.grid(True)
st.pyplot(fig)