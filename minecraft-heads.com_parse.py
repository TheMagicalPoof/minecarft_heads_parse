import yaml
import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
import os

config = ConfigParser()

def main():
    config.read("config.ini")
    end = False
    shift = 0
    trades = {}
    while not end:
        urls = urls_chunk(shift)
        if len(urls) < 80:
            end = True
        shift += len(urls)
        for head_url in urls:
            key, data = get_data_dict(head_url)
            trades.update({key: data})

    with open("parsed.yml", "w") as file:
        yaml.dump({"trades": trades}, file, default_flow_style=False)

def create_config():
    if not os.path.exists("config.ini"):
        config["PARSER"] = {"scope_url": "https://minecraft-heads.com/custom-heads",
                             "sel_for": "DIAMOND",
                             "price": "10"}
        config.write(open("config.ini", "w"))
        print('"config.ini" file has been created. Check your settings.')
        exit()

def urls_chunk(shift):
    html = requests.get(config["PARSER"]["scope_url"] + "?start=" + str(shift))
    soup = BeautifulSoup(html.content, "html.parser")
    return list(map(lambda x: "https://minecraft-heads.com" + x.get("href"), soup.find("div", class_="itemList").find_all("a")))

def get_data_dict(head_url):
    print(head_url)
    html = requests.get(head_url)
    soup = BeautifulSoup(html.content, "html.parser")
    return head_url.split('/')[-1], {
        "experienceReward": True,
        "ingredients": {
            1: {
                "customname": "NONE",
                "material": config["PARSER"]["sel_for"],
                "amount": config["PARSER"]["price"]
            }
        },
        "result": {
            "customname": soup.find("title").text,
            "material": "head-" + soup.find("textarea", {"id": "UUID-Value"}).text,
            "amount": 1,
            "lore": ["  <green><italic>Head"]
        }
    }


if __name__ == '__main__':
    create_config()
    main()
