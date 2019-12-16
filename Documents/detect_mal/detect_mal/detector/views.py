from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://www.alexa.com/topsites")
bsObject=BeautifulSoup(html,"html.parser")

print(bsObject.head.) 

# Create your views here.
def home(request):
    return render(request,'index.html')

#def get_url():
    