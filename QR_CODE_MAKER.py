import pyqrcode
import png
from pyqrcode import *
#paste the link/source of any kind od data in below link
link=""
url=pyqrcode.create(link)
#filename must be specfied below follwed with .png
url.png(".png",scale=10)
print("QR CODE is Ready")
