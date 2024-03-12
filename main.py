from bs4 import BeautifulSoup
import requests

html_request = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_request, "html.parser")
books = soup.find_all('li', class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")


for index,book in enumerate(books):
    book_url = book.find('a')['href']
    book_url = "https://books.toscrape.com/" + book_url
    book_response = requests.get(book_url).text
    soup2 = BeautifulSoup(book_response,"html.parser")
    book_names = soup2.find('h1').text
    book_price = soup2.find('p').text.replace("Â","")
    book_stock = soup2.find('p', class_= "instock availability").text.replace("  ","").replace("\n","") 
    book_desciption = soup2.select('p')[3].text
    book_table= soup2.select('th')[0].text +" : "+ soup2.select('td')[0].text
    
    #book_table = soup2.find('table', class_= "table table-striped").text.replace("  ","").replace("\n","") 
    #book_table = book_table.find("upc") 
    with open (f'posts/{index}.txt', 'w', encoding="utf-8") as f:   
        f.write(f"""\n Book Name: {book_names}
          \n {book_table}
          \n Book Price: {book_price}
          \n Book Stock: {book_stock}
          \n Book Description : \n {book_desciption}       
          """) 
        print(f"File Saved {index}") 
    
    
     
    
    #print(book_response)
    #content_inner > article > div.row > div.col-sm-6.product_main
    