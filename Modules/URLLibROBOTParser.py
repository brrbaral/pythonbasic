# IMPORTING ROBOTPARSER CLASS
import urllib.robotparser

bot=urllib.robotparser.RobotFileParser()
# CHECK WHERE THE WBBSITE ROBOT.TXT FILE EXISTS
x=bot.set_url('https://www.geeksforgeeks.org / robot.txt')
print(x)
#READ THE FILES
y=bot.read()
print(y)

#WE CAN CRAWL THE MAIN SITE
z=bot.can_fetch('*','https://www.geeksforgeeks.org/')
print(z)

#BUT WE CANNOT CRAWL THE DISALLOWED URL
w=bot.can_fetch('*','https://www.geeksforgeeks.org / wp-admin/')
print(w)