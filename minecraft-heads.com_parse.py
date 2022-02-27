import grequests, yaml, os, random
from bs4 import BeautifulSoup
from configparser import ConfigParser
config = ConfigParser()

def main():
    is_search = False
    if "searchword=" in config["parser"]["scope_url"]:
        is_search = True

    end = False
    shift = 0
    urls = []
    heads_yml_cont = {"enabled": True,
                      "chance": config.getfloat("wandering_trader", "heads_chance"),
                      "randomized": True,
                      "randomAmount": config.get("wandering_trader", "heads_amount"),
                      "invincible": False,
                      "customName": "heads.yml",
                      "disableHeroOfTheVillageGifts": False}

    trades = {"Easter_egg": {"experienceReward": True, "ingredients": {1: {"material": "DRAGON_EGG", "amount": 1}}, "result": {"customname": "<gradient:aqua:blue:yellow:green>Magical_PooF's head", "material": "head-ewogICJ0aW1lc3RhbXAiIDogMTY0NTkxNDM0OTQ2MiwKICAicHJvZmlsZUlkIiA6ICI1MzVmMmIwZTM4MmE0MGM3YTRlMTdlZGIyMjIyNDJmOCIsCiAgInByb2ZpbGVOYW1lIiA6ICJNYWdpY2FsX1Bvb0YiLAogICJ0ZXh0dXJlcyIgOiB7CiAgICAiU0tJTiIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzI1ZTQzMzFiOWU4NjI2MDUyZDUwYmNkOWM5ZWY1NDZmYzM0ZTg2Y2JkOWNjZTA1MjBhZTVhZDNhYTJlYjlmYSIKICAgIH0KICB9Cn0=", "amount": 1, "lore": ["  <grey><italic>This head belongs to the hero, who", "  <grey><italic>thousands of years ago slain", "  <grey><italic>the first dragon."]}}} if config.getboolean("parser", "vis") else {}
    while not end:
        urls.insert(0, config.get("parser", "scope_url") + ("&start=" if is_search else "?start=") + str(shift))
        shift += 80
        rs = [grequests.get(head_url) for head_url in urls]
        for greq_obj in grequests.imap(rs, size=config.getint("parser", "requests")):
            soup = BeautifulSoup(greq_obj.content, "html.parser")
            if "start=" in greq_obj.url:
                urls = urls_chunk_when_search(soup) if is_search else urls_chunk(soup)
                if not urls:
                    end = True
            else:
                print(greq_obj.url)
                trades.update({greq_obj.url.split('/')[-1]: get_data_dict(soup)})

    heads_yml_cont.update({"trades": trades})

    with open("heads.yml", "w") as file:
        yaml.dump(heads_yml_cont, file, default_flow_style=False)

    print("\n\n\nParsing is complete.\n\n")

def create_config():
    if not os.path.exists("config.ini"):

        config.add_section("parser")
        config.set("parser", "scope_url", "https://minecraft-heads.com/custom-heads")
        config.set("parser", "requests", "16")
        config.set("parser", "vis", "true")

        config.add_section("buy_price")
        config.set("buy_price", "material", "DIAMOND")
        config.set("buy_price", "amount", "3:10")

        config.add_section("wandering_trader")
        config.set("wandering_trader", "heads_chance", "1")
        config.set("wandering_trader", "heads_amount", "2:5")

        config.write(open("config.ini", "w"))
        print('"config.ini" file has been created. Check your settings.')
        exit()

def urls_chunk(soap):
    data = soap.find("div", class_="itemList")
    return None if not data else list(map(lambda x: "https://minecraft-heads.com" + x.get("href"), data.find_all("a")))

def urls_chunk_when_search(soap):
    finds = soap.find_all("div", class_="item")
    return None if not finds else list(map(lambda x: "https://minecraft-heads.com" + x.find("a").get("href"), finds))

def config_get_price():
    price = config.get("buy_price", "amount").split(":")
    if len(price) > 1:
        return random.randint(int(price[0]), int(price[1]))
    return int(price[0])

def get_data_dict(soup):
    return {
        "experienceReward": True,
        "ingredients": {
            1: {
                "material": config.get("buy_price", "material"),
                "amount": config_get_price()
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
    config.read("config.ini")
    main()
