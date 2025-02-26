import requests
from bs4 import BeautifulSoup
import random
import connections.dbConnect as db

def scrape_data(url : str, quality_input : str):

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    # DONE : Get artefact information board
    info_board = soup.find('div', id = 'content').find('div', id = 'mw-content-text').find('aside', class_ = 'portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default')

    # DONE : Get artefact name
    def get_set_name():
        res = info_board.find('h2', attrs = {'data-source' : 'title'}).decode_contents(formatter = lambda x: x.replace(u'\xad', ''))

        return f'{res}'
    set_name = get_set_name()



    # DONE : Get flower, feather, sands, goblet, circlet name

    def get_artifact_name(data_source : str):
        res = info_board.find('div', attrs = {'data-source' : f'{data_source}'}).find('div', class_ = 'pi-data-value pi-font').find('a', title = True)['title']

        return f'{res}'
    flower_name = get_artifact_name('flower')
    plume_name = get_artifact_name('plume')
    sands_name = get_artifact_name('sands')
    goblet_name = get_artifact_name('goblet')
    circlet_name = get_artifact_name('circlet')

    # DONE : Get piece bonus
    def get_piece_bonus(data_source : str):
        res = info_board.find('div', attrs = {'data-source' : f'{data_source}'}).find('div', class_ = 'pi-data-value pi-font')
        for i in res.find_all('b'):
            i.unwrap()
        for i in res.find_all('span'):
            i.unwrap()
        for i in res.find_all('a'):
            i.unwrap()
        for i in res.find_all('br'):
            i.extract()
            
        t = res.decode_contents()
        ts = t.replace('-Piece Bonus', '')
        ts = ts.replace(ts[0], "", 1)
        return f'{ts}'

    # DONE : Get 2-Piece Bonus
    two_piece_bonus = get_piece_bonus('2pcBonus')
        
    # DONE : Get 4-Piece Bonus
    four_piece_bonus = get_piece_bonus('4pcBonus')
        
    # DONE : Get flower, plume, etc... page link
    flower_page_link = f"https://genshin-impact.fandom.com/{(info_board.find('div', attrs = {'data-source' : 'flower'}).find('div', class_ = 'pi-data-value pi-font').find('a', href = True)['href'])}"
    plume_page_link = f"https://genshin-impact.fandom.com/{(info_board.find('div', attrs = {'data-source' : 'plume'}).find('div', class_ = 'pi-data-value pi-font').find('a', href = True)['href'])}"
    sands_page_link = f"https://genshin-impact.fandom.com/{(info_board.find('div', attrs = {'data-source' : 'sands'}).find('div', class_ = 'pi-data-value pi-font').find('a', href = True)['href'])}"
    goblet_page_link = f"https://genshin-impact.fandom.com/{(info_board.find('div', attrs = {'data-source' : 'goblet'}).find('div', class_ = 'pi-data-value pi-font').find('a', href = True)['href'])}"
    circlet_page_link = f"https://genshin-impact.fandom.com/{(info_board.find('div', attrs = {'data-source' : 'circlet'}).find('div', class_ = 'pi-data-value pi-font').find('a', href = True)['href'])}"

    # DONE : Get flower, plume, etc image link
    def get_image_link(url : str):
        ...
        # TODO : return image link in string format
        
        page_request = requests.get(url)
        img_soup = BeautifulSoup(page_request.content, 'html.parser')
        
        img_info_board = img_soup.find('div', id = 'content').find('div', id = 'mw-content-text').find('aside', class_ = 'portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default')
        img_link = img_info_board.find('figure', attrs = {'data-source' : 'image'}).find('a', href = True)['href']

        return f'{img_link}'

    flower_image_link = get_image_link(flower_page_link)
    plume_image_link = get_image_link(plume_page_link)
    sands_image_link = get_image_link(sands_page_link)
    goblet_image_link = get_image_link(goblet_page_link)
    circlet_image_link = get_image_link(circlet_page_link)

    # DONE : Set artefact quality

    quality = quality_input.strip()

    # TODO : Set ID
    """
    format :
        > 2 digit based on quality (1-3 = 13, 3-4 = 34, 4-5 = 45)
        > 3 random digit from 100 - 999
        > 2 random digit from 10 - 99
        > 1 random digit from 0 - 9
    """
    id = f'{quality.replace("-", "")}{random.randint(100, 999)}{random.randint(10, 99)}{random.randint(0, 9)}'
    """
    print(id)
    print(set_name)
    print(quality)
    print(flower_name)
    print(plume_name)
    print(sands_name)
    print(goblet_name)
    print(circlet_name)
    print(two_piece_bonus)
    print(four_piece_bonus)
    print(flower_image_link)
    print(plume_image_link)
    print(sands_image_link)
    print(goblet_image_link)
    print(circlet_image_link)
    """

    # DONE : Add to Database
    def add_to_db():
        mycursor = db.mycursor

        sql = "INSERT INTO artefacts (id, set_name, quality, 2_set_bonus, 4_set_bonus, flower_name, flower_icon, plume_name, plume_icon, sands_name, sands_icon, goblet_name, goblet_icon, circlet_name, circlet_icon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (id, set_name, quality, two_piece_bonus, four_piece_bonus, flower_name, flower_image_link, plume_name, plume_image_link, sands_name, sands_image_link, goblet_name, goblet_image_link, circlet_name, circlet_image_link)
        mycursor.execute(sql, data)

        db.mydb.commit()

    
    add_to_db()
    
link_list = []

def scrape13():
    i = 1
    for link in link_list:
        scrape_data(link, "1-3")
        print(f'{i} artefacts added of {len(link_list)}')
        i += 1
    print("done")
    ask = input("Again? [y/n]")
    if ask == "y":
        input_link()
    else:
        print("All Done!")
    
def scrape34():
    i = 1
    for link in link_list:
        scrape_data(link, "3-4")
        print(f'{i} artefacts added of {len(link_list)}')
        i += 1
    print("done")
    ask = input("Again? [y/n]")
    if ask == "y":
        input_link()
    else:
        print("All Done!")

def scrape45():
    i = 1
    for link in link_list:
        scrape_data(link, "4-5")
        print(f'{i} artefacts added of {len(link_list)}')
        i += 1
    print("done")
    ask = input("Again? [y/n]")
    if ask == "y":
        input_link()
    else:
        print("All Done!")

def input_link():
    link = input("Input Link Here [(n) if enough] > ")
    if link != "n":
        link_list.append(link)
        input_link()
    else:
        con = input("Input quality > ")
        if con == "1-3":
            scrape13()
        elif con == "3-4":
            scrape34()
        elif con == "4-5":
            scrape45()
            
input_link()