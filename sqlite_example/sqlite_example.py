import sqlite3
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


# This is my path, set your own here!
path = "c:\\Python\\Python38-32\\myprojects\\sqlite_example\\"

# Read & Write file functions

def csvin(fname):
    " Read csv to list of tuples "
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # 0.row ignored
        data = [tuple(i) for i in reader] 
    return data

def csvout(out_csv, data):
    " Write fetched data to csv file "
    with open(out_csv, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in data:
            writer.writerow(i)
    return out_csv

# Create DB and connecting
db_name = f"{path}test_results.db"
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Test - Is table exists?
# With this, you can run the code more time in terminal!
try:
    c.execute("SELECT * FROM value_table")
except:
    pass
else:
    c.execute("DROP TABLE value_table")

# Read input csv file
fname = f"{path}my_table.csv"
file_cont = csvin(fname)

# Create table
create_res = " CREATE TABLE IF NOT EXISTS value_table (Id INTEGER PRIMARY KEY NOT NULL, my_id TEXT, my_value REAL); "
c.execute(create_res)

# Insert data from csv file to sql table
insert_res = " INSERT INTO value_table (Id,my_id,my_value) VALUES (?,?,?); "
c.executemany(insert_res, file_cont)

# Count means based on same my_id
result_atlag = " SELECT my_id, COUNT(*) as my_id, round(AVG(my_value),2) as result_avg FROM value_table GROUP BY my_id "
c.execute(result_atlag)

# Write fetched data to csv file
avgs = c.fetchall()
avgs.insert(0,("my_id","my_sample","my_value")) # + header 

# OUTPUT -> csv file -> pdf table
  
# Results to csv file
newFile = f"{path}results\\avg.csv"
csvout(newFile,avgs)

# Results to pdf file
width, height = A4
pdfmetrics.registerFont(TTFont('Times', 'Times.ttf'))
pdf_name = f"{path}results\\avg.pdf" 
c = canvas.Canvas(pdf_name) # filename
c.setFont('Times', 16)
title_names = "Means:"
c.drawCentredString(150,height-50,title_names)
c.setFont('Times', 12)

table = Table(avgs, 100, 25)
table.setStyle(TableStyle([            
            
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('FONTNAME', (0,0),(-1,-1), 'Times'),
    ('BACKGROUND',(0,0),(-1,-1), colors.whitesmoke),
    ('BACKGROUND',(0,0),(2,0), colors.lightskyblue),

    ]))

table.wrapOn(c, width,height)
table.drawOn(c, 100,height-180)
c.save()

# Close DB
conn.commit()
conn.close()
