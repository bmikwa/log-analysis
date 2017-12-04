# LOG ANALYSIS
 
####Implementation
Four views were used to complete this project. All the views used are included below. Log.py is the python code that accesses the database and print the output to log_analysis.txt. The output gives  the answers to the three (3) questions asked in the project. The following souruces that were used to  accomplish this project;`https://www.postgresql.org/message-id/F268gEHCqHkl9UP1X010000eae4%40hotmail.com`,`https://www.postgresql.org/docs/9.1/static/functions-datetime.html,http://postgresguide.com/tips/dates.html,https://stackoverflow.com/questions/13113096/how-to-round-an-average-to-2-decimal-places-in-postgresql, and http://www.sqlbook.com/sql-string-functions/sql-concatenate/`.

#### Views
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
