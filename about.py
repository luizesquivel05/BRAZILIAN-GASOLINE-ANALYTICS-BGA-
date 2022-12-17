a = '''What is Brazilian Gasoline Analytics (BGA) all about?

This is the analysis of average gasoline prices in Brazil during the years 2000 to 2019, in an attempt to study its evolution.

Source: https://transparencia.petrobras.com.br/dados-abertos

'''

b = '''\n\n The present problem intends to study the gasoline database in Brazil through 17 questions:

1. What are the values contained in both bases and what are their appearance frequencies?
2. What are the appearances of common gasoline and its variations in times between 2000 and 2010?
3. What is the average gasoline resale price in August 2008?
4. What is the average resale price of gasoline in May 2014 in São Paulo?
5. When and in which state was the R$5.00 flag exceeded?
6. What is the average price in the southern region in 2012?
7. In the State of Rio de Janeiro, what was the year-on-year percentage change?
8. Which states have the greatest absolute differences between the cheapest and most expensive gasoline prices? And how long has it belonged?
'''

c = '''\n\n Some technical details:

-This data analysis was produced by combining native Python themes with functions from the Pandas library.
-In some cells we will display NaN - which means empty.
- The data source is in Brazilian Portuguese so the presentations will be in Portuguese.
- The subtitles page shows translations of terms that appear in the base.
'''

d = '''\n\nAbout developer:

-Hello, my name is Luiz Esquivel, I'm 19 years old and currently I work as a Jr IT Analyst at Ultracom, being essentially co-responsible for the management activities of the mailing (I manage the data of clients and potential clients that we need to contact or have already contact us), I also manage data about customers and potential customers (such as: availability to serve their region with internet/telephrony products; primary credit analysis; primary analysis of data provided by the customer...) .
-I have been a development student since 2019, when I started studying WEB development, migrating to the data area in 2022, as I feel more confident in this area and recognize the importance of data in the lives and projects of companies and people.
-In the data area, my knowledge is centered on Office Package (especially Word and Excel); Business Intelligence methodology and tools (such as PowerBI); Database and its Management Systems (SQL and MySQL); Python focused on data analysis (automation of routines with Python).
'''

def about():
    texto = ""
    texto += a + b + c + d
    txt = texto.split("\n\n ")
    
    for i in txt:
        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        print(i)