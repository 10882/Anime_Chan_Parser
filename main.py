user_agent = {'user_agent' : ''}

from bs4 import BeautifulSoup
import requests

def imagelistget(urllist, user_agent):
    imglist = []
    for url in urllist:
        soup = BeautifulSoup(requests.get(url, user_agent).content, features="lxml")
        posts_block = soup.find('div', class_ = 'posts_block' )
        imgs = posts_block.findAll('span', class_ = 'img_block_big')
        for i in imgs:
            img = i.find('a')
            imgdata = img.attrs
            imglist.append(imgdata['href'])
    return(imglist)



def urlcreate():
    tagstr = ''
    urllist = []
    charter = input('Input charter name     ')
    tags = input('Input other tags  ').split()
    count_of_pg = int(input('Input count of pages   '))
    for i in tags:
        tagstr = tagstr+i+'||'
    charter.replace(' ', '_')
    for i in range(count_of_pg):
        urllist.append('https://anime-pictures.net/pictures/view_posts/'+str(i)+'?search_tag='+tagstr + charter+'&lang=ru')
    return(urllist)

def dowloadall(images):
    for addurl in images:
        soup = BeautifulSoup(requests.get('https://anime-pictures.net'+addurl).content)
        razdel = soup.find('div', class_ = 'post_vote_block')
        downloadbut = razdel.find('a', class_ = 'download_icon')
        data = downloadbut.attrs
        url = 'https://anime-pictures.net'+data['href']
        resp = requests.get(url)
        f1le = open(addurl[20:26]+'.png', 'wb')
        f1le.write(resp.content)
        f1le.close()


url = urlcreate()
if user_agent[user agent] = '':
    print('Пожалуйста, введите свой user agent в 1 строке')
    exit()
images = imagelistget(url, user_agent)
dowloadall(images)
