import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://www.google.com.np/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiy4I3S7tzcAhUD448KHTsqCGYQjRx6BAgBEAU&url=https%3A%2F%2Fwww.pinterest.co.uk%2Fheroinesneha%2Fsneha-stills%2F&psig=AOvVaw0s6JggnTHFPw-Pl53LfUMj&ust=1533797373775308")