import requests
from bs4 import BeautifulSoup
import random
import connections.dbConnect as db

def scrape_data(url : str):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    
    # DONE : Get character information board
    content_container = soup.find('div', id = 'content').find('div', id = 'mw-content-text').find('div', class_ = 'mw-parser-output')
    info_board = content_container.find('aside', class_ = 'portable-infobox pi-background pi-border-color pi-theme-char pi-layout-default')

    # DONE : Get character name
    def get_name():
        res = info_board.find('h2', attrs = {'data-source' : 'name'})
        if res != None:
            res = res.decode_contents(formatter = lambda x: x.replace(u'\xad', ''))
        return f'{res}'
    name = get_name()
    
    # DONE : Get quality
    def get_quality():
        res = info_board.find('td', attrs = {'data-source' : 'quality'})
        if res != None:
            res = res.find('img', alt = True)['alt']
        return f'{res[0]}'
    quality = get_quality()
    
    # DONE : Get weapon type
    def get_weapon_type():
        res = info_board.find('td', attrs = {'data-source' : 'weapon'})
        if res != None:
            res = res.find('a', title = True)['title']
        return f'{res}'
    weapon_type = get_weapon_type()
    
    # DONE : Get element
    def get_element():
        res = info_board.find('td', attrs = {'data-source' : 'element'})
        if res != None:
            res = res.find('a', title = True)['title']
        return f'{res}'
    element = get_element()
    
    # DONE : Get constelation
    def get_constellation():
        res = info_board.find('div', attrs = {'data-source' : 'constellation'})
        if res != None:
            res = res.find('div', class_ = 'pi-data-value pi-font').find('a', title = True)['title']
        return f'{res}'
    constellation = get_constellation()
    
    # DONE : Get region
    def get_region():
        res = info_board.find('div', attrs = {'data-source' : 'region'})
        if res != None:
            res = res.find('div', class_ = 'pi-data-value pi-font').find('a', title = True)['title']
        return f'{res}'
    region = get_region()
    
    # DONE : Get paragraph
    def get_paragraph():
        p_list = content_container.find_all('p', limit = 3)
        a = []
        for s in p_list:
            for i in s.find_all('b'):
                i.unwrap()
            for i in s.find_all('span'):
                i.unwrap()
            for i in s.find_all('a'):
                i.unwrap()
            for i in s.find_all('i'):
                i.unwrap()
            for i in s.find_all('u'):
                i.unwrap()
            for i in s.find_all('aside'):
                i.extract()
            for i in s.find_all('sup'):
                i.extract()
            s = s.decode_contents()
            a.append(s)            
        r = ""
        a = a[1:]
        for i in a:
            r += i
        return r
    description = get_paragraph()
    
    # DONE : Get character icon
    def get_icon():
        g_link = content_container.find('div', class_ = 'custom-tabs-default custom-tabs').find('a', title = f'{name}/Gallery', href = True)['href']
        g_request = requests.get(f'https://genshin-impact.fandom.com{g_link}')
        icon_soup = BeautifulSoup(g_request.content, 'html.parser')
        
        img_gallery0 = icon_soup.find('div', id = 'content').find('div', id = 'mw-content-text').find('div', class_ = 'mw-parser-output').find('div', id = 'gallery-0')
        img_url = img_gallery0.find('div', id = f'{name.replace(" ", "_")}_Icon-png').find('img', src = True)['src']
        
        img_url = img_url.replace('/scale-to-width-down/185', '')
                
        return f'{img_url}'
    icon = get_icon()
    
    # DONE : Set ID
    """
    format : 
        > 1 digit based on quality (4, 5, etc...)
        > 1 digit based on reqion :
            - None = 0
            - Mondstadt = 1
            - Liyue = 2
            - Inazuma = 3
            - Sumeru = 4
            - Fontaine = 5
            - Natlan = 6
            - Snezhnaya = 7
            - etc...
        > 1 digit based on weapon type : 
            - Sword = 1
            - Claymore = 2
            - Bow = 3
            - Catalyst = 4
            - Polearm = 5
        > 3 random digit from 100 - 999
        > 2 random digit from 10 - 99
        > 1 random digit from 0 - 9
        # 123444556
    """
    def set_id(quality : str, region : str, weapon_type : str):
        # python 3.8 did'nt have match(switch case) :(
        if region == "None":
            reg_id = "0"
        elif region == "Mondstadt":
            reg_id = "1"
        elif region == "Liyue":
            reg_id = "2"
        elif region == "Inazuma":
            reg_id = "3"
        elif region == "Sumeru":
            reg_id = "4"
        elif region == "Fontaine":
            reg_id = "5"
        elif region == "Natlan":
            reg_id = "6"
        elif region == "Snezhnaya":
            reg_id = "7"
        
        if weapon_type == "Sword":
            wpn_id = "1"
        elif weapon_type == "Claymore":
            wpn_id = "2"
        elif weapon_type == "Bow":
            wpn_id = "3"
        elif weapon_type == "Catalyst":
            wpn_id = "4"
        elif weapon_type == "Polearm":
            wpn_id = "5"
            
        rand1 = random.randint(100, 999)
        rand2 = random.randint(10, 99)
        rand3 = random.randint(0, 9)
        
        res = f'{quality}{reg_id}{wpn_id}{rand1}{rand2}{rand3}'
        return res
    id = set_id(quality, region, weapon_type)
    
    # TODO : Add to Database
    def add_to_db():
        mycursor = db.mycursor
        
        sql = 'INSERT INTO characters (id, char_name, char_desc, constelation, element, quality, weapon_type, char_icon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
        data = (id, name, description, constellation, element, quality, weapon_type, icon)
        mycursor.execute(sql, data)
        
        db.mydb.commit()
    add_to_db()
    return name

"""
scrape_data('https://genshin-impact.fandom.com/wiki/Aloy')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Venti')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Zhongli')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Kamisato_Ayaka')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Tighnari')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Furina')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Citlali')
print("----------------------------------------")
scrape_data('https://genshin-impact.fandom.com/wiki/Arlecchino')
"""
    
link_list = []
tmplink = []
    
ask = input("scrape data mannualy ? [y/n]")

def start_scraping(lists : list):
    print(f'begin scrapping characters, Remaining : {len(lists)} of {len(lists)}')
    i = 1
    for link in lists:
        if link != 'https://genshin-impact.fandom.com/wiki/Traveler':
            n = scrape_data(link)
            lists_count = len(lists)
            print(f'{n} Added to Database, Remaining : {lists_count - i} of {lists_count}')
            i += 1
        else:
            print('the link contained blacklisted character. Skipping!')
            i += 1
    print("All Characters Has Been Added To Database")

def input_manually():
    link = input("Input Link Here [(n) if enough] > ")
    if link != "n":
        link_list.append(link)
        input_manually()
    else:
        start_scraping(link_list)
        
def input_automatically(limit : int):
    link = input("Input link here > ")
    
    req = requests.get(link)
    sp = BeautifulSoup(req.content, 'html.parser')
    mwpu = sp.find('div', id = 'content').find('div', id = 'mw-content-text').find('div', class_ = 'mw-parser-output')
   
    table = mwpu.find_all('table').pop(1)
    tbody = table.find('tbody')
    
    if limit == 0:
        tr = tbody.find_all('tr')[1:]
    else:
        tr = tbody.find_all('tr', limit = limit+1)[1:]  
    
    for tds in tr:
        td = tds.find('td')
        
        href = td.find('a', href = True)['href']
        url = f'https://genshin-impact.fandom.com{href}'
        link_list.append(url)
    
    start_scraping(link_list)
        

if ask == "y":
    input_manually()
elif ask == "n":
    ask_lim = input("limit to how much? [0 if no limit]: ")
    input_automatically(int(ask_lim))