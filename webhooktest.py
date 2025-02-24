import requests
import controllers.weapons as wp

url = "https://discord.com/api/webhooks/1343569939260379208/VT63XQQI07TafusuXQPUPy4xiYWkzu8PSx_WvVkAGRPanqpHLmrWCAMloq6ViGCawn8j"

embed_tittle = {
    "title" : "WEAPON LIST",
}

onestarweapon = wp.get_weapon_list_based_on_quality(1)
field1 = ""
oneindex = 1

for weapon in onestarweapon:
            field1 += f'{oneindex}. {weapon}\n'
            oneindex += 1
            
embed_1sw = {
    "title" : "1 STAR WEAPONS",
    "description" : field1
}

twostarweapon = wp.get_weapon_list_based_on_quality(2)
field2 = ""
twoindex = 1

for weapon in twostarweapon:
            field2 += f'{twoindex}. {weapon}\n'
            twoindex += 1
            
embed_2sw = {
    "title" : "2 STAR WEAPONS",
    "description" : field2
}

fourstarweapon = wp.get_weapon_list_based_on_quality(4)
field4 = ""
fourindex = 1

for weapon in fourstarweapon:
            field4 += f'{fourindex}. {weapon}\n'
            fourindex += 1
            
embed_4sw = {
    "title" : "4 STAR WEAPONS",
    "description" : field4
}

fivestarweapon = wp.get_weapon_list_based_on_quality(5)
field5 = ""
fiveindex = 1

for weapon in fivestarweapon:
            field5 += f'{fiveindex}. {weapon}\n'
            fiveindex += 1
            
embed_5sw = {
    "title" : "5 STAR WEAPONS",
    "description" : field5
}

data = {
    "content": "",
    "username": "[/] BUFF_VelloImpact",
    "embeds": [
        embed_tittle,
        embed_1sw,
        embed_2sw,
        embed_4sw,
        embed_5sw
    ]
}

result = requests.post(url, json=data)
if 200 <= result.status_code < 300:
    print(f"Webhook sent {result.status_code}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result.json()}")