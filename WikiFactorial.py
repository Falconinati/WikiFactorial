from bs4 import BeautifulSoup
import urllib2

# Based off this comment
# https://www.reddit.com/r/ProgrammerHumor/comments/7gcbiw/perfect_factorial_program/dqimnug/

wiki = 'https://en.wikipedia.org/wiki/Factorial'
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find("table", {"class": "wikitable"})
values = []
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 2:
        values.append((cells[0].find(text=True), cells[1].find(text=True)))

value = raw_input('Insert a number to get the factorial: ')
if int(value) > 6:
    print 'DIY: ' + wiki
    exit(0)

for i in range(len(values)):
    if value == values[i][0]:
        print values[i][1]
        exit(0)
