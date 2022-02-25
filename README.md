# minecraft-heads.com custom heads parser 
## Description
This utility parse a [`Custom heads`](https://minecraft-heads.com/custom-heads) data, for importing to [`Wandering Trades`](https://www.spigotmc.org/resources/wandering-trades-easily-customize-wandering-traders-1-16-1-18.79068/) minecraft plugin.

#### Parse scope:
- https://minecraft-heads.com/custom-heads/
- https://minecraft-heads.com/custom-heads/food-drinks
- https://minecraft-heads.com/custom-heads/plants
- etc.

## Launch
To run this script, you need to follow these steps:
#### for Windows
1. make sure that you have installed 3.x.x `Python` version, and `pip`.
1. execute command `pip install -r requirements.txt` in `cmd`.
3. run `start.bat` file.

### Change settings:
3. you need edit `config.ini` file, to configure parser.
  ```
[PARSER]
scope_url = https://minecraft-heads.com/custom-heads    <----scope of parsing
sel_for = DIAMOND                                       <----you also can use EMERALD and etc.
price = 10                                              <----amount of resource
```
### To integrate into ["Wandering Trades"](https://www.spigotmc.org/resources/wandering-trades-easily-customize-wandering-traders-1-16-1-18.79068/) plugin you need:

1. Copy all data from `parsed.yml` and paste instead of `trades` object of `you_server\plugins\WanderingTrades/trades/hermitheads.yml`
2. Save the file
3. Use `/wt reload` - for reload plugin.
4. Use `/wt summon hermitheads ~ ~ ~` for summon test NPC.
