from django.core.management.base import BaseCommand, CommandError
from Myapp.models import MyQuotes
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Scrap the 20 Quotes and save in Database'

    def handle(self, *args, **options):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.goodreads.com/quotes/tag/life")

        quote=[] 
        rating=[] 
        author= []

        content = driver.page_source
        soup = BeautifulSoup(content,features="html.parser")
        for a in soup.findAll('div', attrs={'class':'quoteDetails'}):
            Quote=a.find('div', attrs={'class':'quoteText'})
            Author=a.find('span', attrs={'class':'authorOrTitle'})
            quote.append(Quote.text.replace('\n','').strip() )
            author.append(Author.text.replace('\n','').strip())
            
        for a in soup.findAll('div', attrs={'class':'right'}):
            Rating=a.find('a', attrs={'class':'smallText'})
            rating.append(Rating.text)
            
        rating_list = list(map(lambda sub:int(''.join([i for i in sub if i.isnumeric()])), rating))
        for x,y,z in zip(author[0:20],quote[0:20],rating_list[0:20]):
            obj = MyQuotes.objects.create(Author=x,Quote=y,likes=z)
            

