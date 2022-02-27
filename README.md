# minecraft-heads.com custom heads parser 
## Description
This utility parse a [`Custom heads`](https://minecraft-heads.com/custom-heads) data, for importing to [`Wandering Trades`](https://www.spigotmc.org/resources/wandering-trades-easily-customize-wandering-traders-1-16-1-18.79068/) minecraft plugin.

#### Parse scope:
- https://minecraft-heads.com/custom-heads/search?searchword=pumpkin
- https://minecraft-heads.com/custom-heads/food-drinks
- https://minecraft-heads.com/custom-heads
- and other similar.

## Launch
To run this script, you need to follow these steps:
#### for Windows
1. make sure that you have installed 3.x.x `Python` version, and `pip`.
1. execute command `pip install -r requirements.txt` in `cmd`.
3. run `start.bat` file.

### Change settings:
Edit `config.ini` file, to configure parser.

1. ```[parser]```
 `scope_url = https://minecraft-heads.com/custom-heads`
  
    - This is parsing scope, also you can use links like:
    - https://minecraft-heads.com/custom-heads/search?searchword=pumpkin
    - https://minecraft-heads.com/custom-heads/food-drinks
    - https://minecraft-heads.com/custom-heads
    - and other similar.


2. ```[parser]```
`requests = 16`

    - number of concurrent requests to the server.


3. ```[parser]```
`vis = true`

    - very important setting :)

4. ```[buy_price]```
`material = DIAMOND`

    - Resource for which you can buy a head, you can use: 
    - EMERALD, DRAGON_EGG, GRASS, GOLD_INGOT and etc.

5. ```[buy_price]```
`amount = 3:10`

    - payment resource amount, number 6 equal 6 
    - 5:10 is equal of range from 5 to 10.
    
6. ```[wandering_trader]```
 `heads_chance = 1`
    - the chance that the seller will trade heads, 0.3 equal 30% 
    
7. ```[wandering_trader]```
 `heads_amount = 2:5`
    - number of heads seller shows at one time, 2:5 equal from 2 to 5 heads

### To integrate into ["Wandering Trades"](https://www.spigotmc.org/resources/wandering-trades-easily-customize-wandering-traders-1-16-1-18.79068/) plugin you need:

1. After parsing, copy `heads.yml` file to `you_server\plugins\WanderingTrades/trades/` catalog.
2. Use `/wt reload`command - for reload plugin settings in you server.
3. Use `/wt summon heads ~ ~ ~` command for summon test NPC.
