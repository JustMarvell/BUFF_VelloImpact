import requests
from bs4 import BeautifulSoup

# Making a GET request
#link = 'https://genshin-impact.fandom.com/wiki/Talking_Stick'


def scrape_weapon():
    link = input("Input Link : ")
    
    r = requests.get(link)

    # check status code for response received
    # success code - 200
    print(r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    weapon_name = soup.find('h2', class_ = 'pi-item pi-item-spacing pi-title pi-secondary-background').decode_contents(formatter = lambda x: x.replace(u'\xad', ''))
    weapon_description = soup.find('div', class_ = 'description-content')
    
    for i in weapon_description.find_all('span'):
        i.unwrap()
    for i in weapon_description.find_all('a'):
        i.unwrap()
    for i in weapon_description.find_all('b'):
        i.unwrap()
    
    weapon_passive_name = soup.find('th', class_ = 'pi-horizontal-group-item pi-data-label pi-secondary-font pi-border-color pi-item-spacing').decode_contents()
        
    url = []
    for a in soup.find('div', class_ = 'pi-image-collection wds-tabber').find_all('a', href = True):
        url.append(a['href'])

    icon_url = url[1]

    weapon_base_atk = soup.find('div', class_ = 'pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color').decode_contents().strip()[5:]
    weapon_type = soup.find_all('section', class_ = 'pi-item pi-panel pi-border-color wds-tabber')[0].find('a', title = True)['title']
    weapon_quality = soup.find_all('section', class_ = 'pi-item pi-panel pi-border-color wds-tabber')[0].find_all('div', class_ = 'pi-item pi-data pi-item-spacing pi-border-color')[1].find('img', alt = True)['alt']
    weapon_sct = soup.find_all('div', class_ = 'pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color')[1].find('a', title = True)['title']
    weapon_sct_atr = soup.find_all('div', class_ = 'pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color')[2].decode_contents().strip()[5:]
    weapon_atr_dec = soup.find_all('td', class_ = 'pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing')

    for i in weapon_atr_dec[4].find_all('span'):
        i.unwrap()
    for i in weapon_atr_dec[4].find_all('a'):
        i.unwrap()
    for i in weapon_atr_dec[4].find_all('b'):
        i.unwrap()
        
    weapon_release_date = soup.find_all('section', class_ = 'pi-item pi-panel pi-border-color wds-tabber')[0].find('div', attrs = {'data-source' : 'releaseDate'}).find('div', class_ = 'pi-data-value pi-font')

    s = weapon_release_date.decode_contents().replace('<br/>', ' | ')


    print(f'Weapon Name : {weapon_name}')
    print(f'Weapon Type : {weapon_type}')
    #print(f'Weapon Quality : {weapon_quality}')
    print(f'Release Date : {s}')
    print("---------------------------")
    print(f'Weapon Description : {weapon_description.decode_contents()}')
    print("---------------------------")
    print(f'Passive Name : {weapon_passive_name}')
    print("---------------------------")
    print(f'Attribute Description : {weapon_atr_dec[4].decode_contents()}')
    print("---------------------------")
    print(f'Icon URL : {icon_url}')
    #print(f'Base ATK : {weapon_base_atk}')
    #print(f'Secondary Attribute : {weapon_sct_atr} {weapon_sct}')

        
    # #fb = soup.find('div', class_ = 'wds-tab__content wds-is-current').find('a', href = True).contents[0]

    #print(fb)

    confir = input("Again? [y/n]")

    if confir == "y":
        scrape_weapon()
    else:
        print("Godbye")