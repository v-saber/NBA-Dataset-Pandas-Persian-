#!/usr/bin/env python
# coding: utf-8

# <h1 align=center style="line-height:200%;font-family:B nazanin;color:#0099cc">
# <font face="B nazanin" color="#0099cc">
#     بسکتبالیست‌ها
# </font>
# </h1>

# <p dir=rtl style="direction: rtl;text-align: right;line-height:200%;font-family:B nazanin;font-size:medium">
#     <font face="B nazanin" size=4>
#         در این سوال قصد داریم تا داده‌های مربوط به عملکرد بازیکنان لیگ بسکتبال NBA را تحلیل کنیم.
#         پس کافی است تا کار‌هایی که از شما خواسته شده را مرحله به مرحله انجام دهید.
#     </font>
# </p>

# <h2 align=right style="line-height:200%;font-family:B nazanin;color:#0099cc">
#     <font face="B nazanin" color="#0099cc">
#         مجموعه‌داده
#     </font>
# </h2>
# 
# <p dir=rtl style="direction: rtl;text-align: right;line-height:200%;font-family:B nazanin;font-size:medium">
#     <font face="B nazanin" size=4>
#         مجموعه‌داده‌ای که در اختیار شما قرار گرفته است شامل اطلاعات عملکرد بازیکنان NBA در فصل‌های ۲۰۰۰ الی ۲۰۰۹ است.
#     این مجموعه شامل ۱۸۳۰ سطر و ۱۸ ستون می‌باشد که هر سطر آن شامل اطلاعات یک بازیکن در یک فصل است. توضیحات مربوط به ستون‌ها نیز در جدول زیر آمده است.
#     </font>
# </p>
# 
# <center>
# <div dir=rtl style="direction: rtl;line-height:200%;font-family:B nazanin;font-size:medium">
# <font face="B nazanin" size=4>
#     
# |ستون|توضیحات|
# |:------:|:---:|
# |<code>PlAYER</code>|نام بازیکن|
# |<code>TEAM</code>|مخفف اسم تیم بازیکن در آن فصل|
# |<code>YEAR</code>|سال (فصل مسابقات)|
# |<code>GP</code>|تعداد بازی‌های انجام شده|
# |<code>MIN</code>|میانگین دقایق بازی کرده|
# |<code>PTS</code>|میانگین امتیاز|
# |<code>FGM</code>|میانگین تعداد پرتاب‌های ۲ امتیازی موفق|
# |<code>FGA</code>|میانگین تعداد کل پرتاب‌های ۲ امتیازی|
# |<code>3PM</code>|میانگین تعداد پرتاب‌های ۳ امتیازی موفق|
# |<code>3PA</code>|میانگین تعداد کل پرتاب‌های ۳ امتیازی|
# |<code>FTM</code>|میانگین تعداد پرتاب‌های آزاد (پنالتی) موفق|
# |<code>FTA</code>|میانگین تعداد کل پرتاب‌های آزاد (پنالتی)|
# |<code>OREB</code>|میانگین تعداد ریباند‌ها در حمله|
# |<code>DREB</code>|میانگین تعداد ریباند‌ها در دفاع|
# |<code>AST</code>|میانگین تعداد پاس‌های منجر به امتیاز|
# |<code>STL</code>|میانگین تعداد دفعات توپ‌ربایی|
# |<code>BLK</code>|میانگین تعداد بلاک‌ها|
# |<code>TOV</code>|میانگین تعداد دفعات لو دادن توپ|
#     
# </font>
# </div>
# </center>

# <p dir=rtl style="direction: rtl; text-align: justify; line-height:200%; font-family:B nazanin; font-size:medium">
# <font face="B nazanin" size=4>
#    با استفاده از سلول زیر کتابخانه‌های مورد نیاز خود را <code>import</code> کنید و سپس مجموعه‌داده را که در فایلی به نام <code>NBA2000-2009.csv</code> قرار دارد، بخوانید. 
# </font>
# </p>

# In[325]:


import os
import numpy as np
import pandas as pd
from pprint import pprint
import warnings


# In[ ]:


warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv(r"C:\Users\Administrator\Jupyter_Notebook_Default_Home\quera_contest\1403-07-06\1.NBA\question\Data\NBA2000-2009.csv")
df.head()


# <h2 align=right style="line-height:200%;font-family:B nazanin;color:#0099cc">
#     <font face="B nazanin" color="#0099cc">
#         قسمت اول
#     </font>
# </h2>
# 
# <p dir=rtl style="direction: rtl;text-align: justify;line-height:200%;font-family:B nazanin;font-size:medium">
#     <font face="B nazanin" size=4>
#          لیستی از بازیکن‌ها و فصل‌ها را بدست آورید که در آن فصل، آن بازیکن در حداقل ۲ تا از ۵ ملاک اصلی آمار دو رقمی (بزرگتر مساوی ۱۰) ثبت کرده باشد. 
#         <br>
#         منظور از ۵ ملاک اصلی میانگین امتیاز، میانگین تعداد ریباند (مجموع ریباند در دفاع و حمله)، میانگین تعداد پاس‌های منجر به گل، میانگین تعداد بلاک‌ها و میانگین تعداد توپ‌ربایی‌ها است.
#     </font>
#     <br>
#     <font face="B nazanin" color="red">
#         خروجی:
#     </font>
#     نتیجه‌ی درخواست را در دیتافریمی با نام <code>double_double</code> قرار دهید.
#     این دیتافریم باید شامل ۷ ستون باشد که ستون‌ها از چپ به راست به ترتیب نام بازیکن، سال، میانگین امتیاز، میانگین تعداد پاس‌های منجر به گل، میانگین تعداد ریباند‌ها، میانگین تعداد بلاک‌ها و میانگین تعداد توپ‌ربایی‌ها باشند. همچنین کل دیتافریم باید به ترتیب برحسب سال و نام بازیکن به صورت صعودی مرتب باشد. دو سطر اول این دیتافریم به شکل زیر است:
# </p>
# 
# <center>
# <div style="line-height:200%;font-family:B nazanin;font-size:medium">
# <font face="B nazanin" size=4>
#     
# |PLAYER|YEAR|PTS|AST|REB|STL|BLK|
# |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
# |Antonio Davis|2000|13.7|1.4|10.1|0.3|1.9|
# |Antonio McDyess|2000|20.8|2.1|12.0|0.6|1.5|
#     
# </font>
# </div>
# </center>


# ********** Question 1 **********

print("\n", 10*"*", "Question 1", 10*"*", "\n")

# In[10]:


df1 = df[['PLAYER', 'YEAR', 'PTS', 'AST', 'OREB', 'DREB', 'STL', 'BLK']]
# df1 = df.iloc[:, [0, 2, 5, 12, 13, 14, 16, 15]]
df1.insert(6, 'REB', df1['OREB'] + df1['DREB'])
df1.drop(columns=['OREB', 'DREB'], inplace=True)

double_double = pd.DataFrame(columns=df1.columns)

for i in range(len(df1.index)):
    n = 0
    for j in range(2, len(df1.columns)):
        if (df1.iloc[i][j] >= 10):
            n += 1
        if n == 2:
            a = pd.DataFrame(df1.loc[i])
            double_double = pd.concat([double_double, a.T])  # ignore_index=True پایینتر در سورت هم داریم این را
            break
            
double_double = double_double.sort_values(by=[double_double.columns[1], double_double.columns[0]], ignore_index=True)
pprint(double_double)


# ********** Question 2 **********

print("\n", 10*"*", "Question 2", 10*"*", "\n")

# <h2 align=right style="line-height:200%;font-family:B nazanin;color:#0099cc">
#     <font face="B nazanin" color="#0099cc">
#         قسمت دوم
#     </font>
# </h2>
# 
# <p dir=rtl style="direction: rtl;text-align: justify;line-height:200%;font-family:B nazanin;font-size:medium">
#     <font face="B nazanin" size=4>
#          باارزش‌ترین بازیکنان این ۱۰ فصل را مشخص کنید.
#         ارزش یک بازیکن در یک فصل با استفاده از فرمول زیر بدست می‌آید:
#     </font>
#     $$ (PTS + OREB + DREB + AST + STL + BLK) - (TOV + Missed FG + Missed FT) $$
#     منظور از <code>Missed FG</code> و <code>Missed FT</code> به ترتیب میانگین تعداد پرتاب‌های ۲ امتیازی و آزاد از دست رفته است.  
#     <br>
#     ارزش یک بازیکن در کل ۱۰ فصل برابر است با میانگین ارزش او در هر فصل.
#     <br>
#     <font face="B nazanin" color="red">
#         خروجی:
#     </font>
#     نتیجه‌ی درخواست را در دیتافریمی با نام <code>best_player</code> قرار دهید.
#     این دیتافریم شامل دو ستون است که یکی نام بازیکن و دومی ارزش آن بازیکن است که تا دو رقم اعشار باید گرد شود. همچنین این دیتافریم باید بر اساس ارزش به صورت نزولی و سپس بر اساس نام بازیکن به‌صورت صعودی مرتب باشد.
#     دو سطر اول این دیتافریم به شکل زیر است:
# </p>
# 
# <center>
# <div style="line-height:200%;font-family:B nazanin;font-size:medium">
# <font face="B nazanin" size=4>
#     
# |PLAYER|VALUE|
# |:------:|:---:|
# |Kevin Garnett|29.74|
# |LeBron James|27.9|
#     
# </font>
# </div>
# </center>

# In[25]:


best_player = pd.DataFrame(df['PLAYER'])
best_player['VALUE'] = df['PTS']+df['OREB']+df['DREB']+df['AST']+df['STL']+df['BLK']-(df['TOV']+(df['FGA']-df['FGM'])+(df['FTA']-df['FTM']))

best_player = pd.DataFrame(best_player.groupby('PLAYER')['VALUE'].mean().round(2))
best_player = best_player.sort_values(by=['VALUE', 'PLAYER'], ascending=[False, True])  # inplace=True
pprint(best_player)


# ********** Question 3 **********

print("\n", 10*"*", "Question 3", 10*"*", "\n")

# <h2 align=right style="line-height:200%;font-family:B nazanin;color:#0099cc">
#     <font face="B nazanin" color="#0099cc">
#         قسمت سوم
#     </font>
# </h2>
# 
# <p dir=rtl style="direction: rtl;text-align: justify;line-height:200%;font-family:B nazanin;font-size:medium">
#     <font face="B nazanin" size=4>
#          در هر سال چه تیمی بیشترین میانگین امتیاز را ثبت کرده است؟
#         <br>
#         توجه داشته باشید که میانگین امتیاز یک تیم برابر است با مجموع میانگین امتیاز بازیکن‌هایش.
#     </font>
#     <br>
#     <font face="B nazanin" color="red">
#         خروجی:
#     </font>
#     نتیجه‌ی درخواست را در دیتافریمی با نام <code>max_PTS_of_year</code> قرار دهید.
#     این دیتافریم باید شامل سه ستون باشد که ستون‌ها از چپ به راست به ترتیب سال، نام تیم و میانگین امتیاز است که امتیاز‌ها باید تا دو رقم اعشار گرد شوند. همچنین کل دیتافریم باید برحسب سال به صورت صعودی مرتب باشد. دو سطر اول این دیتافریم به شکل زیر است:
# </p>
# 
# <center>
# <div style="line-height:200%;font-family:B nazanin;font-size:medium">
# <font face="B nazanin" size=4>
#     
# |YEAR|TEAM|PTS|
# |:------:|:---:|:---:|
# |2000|SAC|100.2|
# |2001|LAL|95.9|
#     
# </font>
# </div>
# </center>

# In[322]:


df3 = df.copy()
df3_1 = pd.DataFrame(df3.groupby(['YEAR', 'TEAM'], as_index=False)['PTS'].sum().round(2))
df3_2 = pd.DataFrame(df3_1.groupby(['YEAR'], as_index=False).max('PTS'))

max_PTS_of_year = pd.DataFrame()

for i in range(len(df3_2)):
    for j in range(len(df3_1)):
        if df3_2['YEAR'][i]==df3_1['YEAR'][j]:
            if df3_2['PTS'][i]==df3_1['PTS'][j]:
                max_PTS_of_year = pd.concat([max_PTS_of_year, pd.DataFrame(df3_1.iloc[j]).T], ignore_index=True)

pprint(max_PTS_of_year)

