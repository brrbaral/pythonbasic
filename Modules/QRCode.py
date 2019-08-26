import pyqrcode
url=pyqrcode.create("www.ncit.edu.np")
url.svg("myqrcode.svg",scale=8)
