# Jeremy Cloyd
# web scraper for arbitrage engine
from urllib.request import Request, urlopen
import re

url = Request('http://old.starcitygames.com/decks/140285', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url).read()
html = page.decode("utf-8")
# print(html)

pattern = "<...>.*</a></li><...>"
match_results = re.search(pattern, html, re.IGNORECASE)
cardGroup = match_results.group()
cardGroup = re.sub("<.*?>", "\n", cardGroup)  # Remove HTML tags

cards = cardGroup.split()
print(cards)
for card in cards:
    print(card)

# 4 <a href="http://old.starcitygames.com/results/?name=Mayhem+Devil&auto=Y"
# rel="http://static.starcitygames.com/sales//cardscans/MTG/WAR/en/nonfoil/MayhemDevil.jpg"
# target="new">Mayhem Devil</a></li><li>

# 2 <a href="http://old.starcitygames.com/results/?name=Rankle%2C+Master+of+Pranks&auto=Y"
# rel="http://static.starcitygames.com/sales//cardscans/MTG/ELD/en/nonfoil/RankleMasterOfPranks.jpg"
# target="new">Rankle, Master of Pranks</a></li></ul>
