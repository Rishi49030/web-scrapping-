#!/usr/bin/env python
# coding: utf-8

# In[84]:


pip install beautifulsoup4

pip install requests
# In[152]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[121]:


url='https://www.flipkart.com/search?q=cameradlsr&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'
response = requests.get(url)


# In[122]:


print(response.status_code)


# In[153]:


print(response.content)


# In[124]:


htmlcontent = response.content 
soup = BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify())


# In[125]:


print(soup.title)


# In[126]:


print(soup.title.string)


# In[127]:


print(soup.p)


# In[128]:


print(soup.find_all('a'))


# In[129]:


for link in soup.find_all('a'):
    print(link.get('href')) 


# In[130]:


for image in soup.find_all('img'):
    print(image.get('src')) 


# In[131]:


product = soup.find_all('div',class_='_3pLy-c row')
print(product)


# In[132]:


product = soup.find('div',attrs={'class':'_3pLy-c row'})
print(product)


# In[171]:


titles = []
prices = []
images = []
ratings = []

for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    title = d.find('div' , attrs={'class':'_4rR01T'})
   # print(title.string)
titles.append(title.string)
print(titles)


# In[182]:


for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    rating = d.find('div' , attrs={'class':'_3LWZlK'})
    if rating is not None:
        rating_string = rating.string
    else:
        rating_string = None
    ratings.append(rating_string)
print(ratings)


# In[134]:


for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    price = d.find('div' , attrs={'class':'_30jeq3 _1_WHN1'})
    #print(price.string)
    prices.append(price.string)
    print(prices)


# In[135]:


for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    image = d.find('img' , attrs={'class':'_396cs4'})
   # print(image.get('src'))
images.append(image.get('src'))
print(images)


# In[136]:


d = {'price': [prices], 'image': [images], 'title': [titles]}
df = pd.DataFrame(d)
df


# In[188]:


final = pd.DataFrame()

for j in range(1, 4):
    url = f'https://www.flipkart.com/search?q=cameradlsr&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={j}'
    response = requests.get(url)

    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')

    product = soup.find_all('div', class_='_3pLy-c row')
    titles = []
    prices = []
    images = []
    ratings = []


    for d in soup.find_all('div', attrs={'class': '_2kHMtA'}):
        title = d.find('div', attrs={'class': '_4rR01T'})
        titles.append(title.string)
        price = d.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        prices.append(price.string)
        image = d.find('img', attrs={'class': '_396cs4'})
        images.append(image.get('src'))
        rating = d.find('div', attrs={'class': '_3LWZlK'})
        if rating is not None:
            rating_string = rating.string
        else:
            rating_string = None
        ratings.append(rating_string)
        

    d = {'price': prices, 'image': images, 'title': titles, 'rating': ratings}
    df = pd.DataFrame(d)
    final = pd.concat([final, df])


# In[189]:


df


# In[151]:


df.to_csv('Flipkart_dslrc_camera.csv')


# In[ ]:




