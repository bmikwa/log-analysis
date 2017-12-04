
# import psycopg2
import psycopg2
#my first view
'''news=> CREATE VIEW log_and_articles as select path,articles.author, count(path) as num
from log JOIN articles ON log.path = CONCAT('/','article','/', articles.slug)
GROUP BY path,articles.author  order by num desc;

# second view
CREATE VIEW total_view as SELECT count(*) as per_day_total_view, date_trunc('day', time) as date
FROM log 
GROUP BY 2
ORDER BY 2 DESC;

# Third view
 CREATE VIEW error_view as SELECT count(*) as per_day_total_view, date_trunc('day', time) as date
FROM log where status='404 NOT FOUND' 
GROUP BY 2
ORDER BY 2 DESC;
# Forth view
CREATE VIEW percent_cal AS SELECT (CAST((error_view.per_day_total_view) AS FLOAT)/total_view.per_day_total_view)*100 as percent, total_view.date
from total_view JOIN error_view ON total_view.date = error_view.date ORDER BY percent desc;

'''
# Open log_analysis.txt to write to
file = open("Log_analysis.txt", "w")

# DBNAME stores name of the database
DBNAME = 'news'

     
# Output results to log_analysis.txt   
def output_result(results):
    for rows in results:
        print>>file, (rows[0] + '___ ' + str(rows[1]) + ' views.')
    print>>file,("______________________________")
    
    
#def my_f(): 
def articles_with_high_views():
    con_to_db = psycopg2.connect(database=DBNAME)
    cursor = con_to_db.cursor()
    cursor.execute("""select name,num 
            from log_and_articles JOIN authors
            ON log_and_articles.author = authors.id
            LIMIT 3;""")
    records = cursor.fetchall()
    con_to_db.close()
    print>>file, ("     Answers to the first question")
    return records
    
       
def authors_with_highest_view():
    
    con_to_db = psycopg2.connect(database=DBNAME)
    cursor = con_to_db.cursor()
    cursor.execute("""select name,sum(num) as sum 
            from log_and_articles JOIN authors
            ON log_and_articles.author = authors.id
            GROUP BY name ORDER BY sum desc;""")
    records = cursor.fetchall()
    con_to_db.close()
    print>>file, ("     Answers to the second question")
    return records
    
        
def more_than_one():

    con_to_db = psycopg2.connect(database=DBNAME)
    cursor = con_to_db.cursor()
    cursor.execute("""select DATE(date) AS date,round(percent::numeric,2) from percent_cal where percent > 1;""")    
    records = cursor.fetchall()
    con_to_db.close()
    print>>file,("\n")
    print>>file,("Answer to the third question ")
    for row in records:
        print>>file, (str(row[0]) + "--" + str(row[1]) + "%" + " errors")

        
if __name__ == '__main__':
    print>>file, ("     Log Results    ")
    output_result(articles_with_high_views())
    output_result(authors_with_highest_view())
    more_than_one()
   

file.close()

