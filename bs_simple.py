from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://github.com/topics/neural-vocoder?o=desc&s=updated'

content = requests.get(URL).text
soup = BeautifulSoup(content, 'lxml')

def data_point(item):
    datum = dict()
    datum['owner'] = item.find('a', attrs={
        'data-ga-click': "Explore, go to repository owner, location:explore feed"}).text.strip()
    datum['owner_page'] = 'https://github.com' + item.find('a', attrs={
        'data-ga-click': "Explore, go to repository owner, location:explore feed"}).attrs['href']
    datum['repo'] = item.find('a', class_='text-bold', attrs={
        'data-ga-click': "Explore, go to repository, location:explore feed"}).text.strip()
    datum['repo_page'] = 'https://github.com' + item.find('a', class_='text-bold', attrs={
        'data-ga-click': "Explore, go to repository, location:explore feed"}).attrs['href']
    datum['repo_date'] = item.find('relative-time', class_='no-wrap').text.strip()
    datum['repo_topics'] = [key.text.strip() for key in
                            item.find_all('a', class_='topic-tag topic-tag-link f6 mb-2')]

    try:
        datum['repo_desc'] = item.find('div', class_='px-3 pt-3').div.text.strip()
    except:
        datum['repo_desc'] = ''
    try:
        datum['repo_lang'] = item.find('span', itemprop='programmingLanguage').text.strip()
    except:
        datum['repo_lang'] = ''
    return datum

# repo_item = soup.find('article', class_='border rounded color-shadow-small color-bg-secondary my-4')
# print(data_point(repo_item))

data = [data_point(repo) for repo in
        soup.find_all('article', class_='border rounded color-shadow-small color-bg-secondary my-4')]

print(pd.DataFrame(data))