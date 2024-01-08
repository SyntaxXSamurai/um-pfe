import sqlite3
import time
import zlib

dbname = input("Please provide the sqlite DB filename to load: ")
if (len(dbname) < 1): 
    dbname = "raw_content_metorite_landing.sqlite"

num_bars = input('Enter the amount of bars you want to visualise: ')
bars = int(num_bars)

connection = sqlite3.connect(dbname)
cursor = connection.cursor()

cursor.execute('''
    SELECT COUNT(*)
    FROM metorite_landing_data
    ''')
total_sample_count = float(cursor.fetchone()[0])

cursor.execute('''
    SELECT rec_class, COUNT(*)
    FROM metorite_landing_data
    GROUP BY rec_class
    ORDER BY COUNT(*) DESC
    ''')

counts = dict()
for message_row in cursor :
    counts[message_row[0]] = int(message_row[1])
x = sorted(counts, key=counts.get, reverse=True)

# Spread the font size across 20-100 based on the count
bigfontsize = 80
smallfontsize = 20
count = 0
count_other = 0
other_category_size = 0

fhandler = open("dabar.js", "w")
fhandler.write("dabar = [['Class', 'Count of Metorites']") #, {role: 'annotation'}]")
for k in x[:100]:
    size = counts[k]
    percentage_of_sample = (size / total_sample_count) * 100
    #size = (size - lowest) / float (highest - lowest)
    #size = int((size * bigfontsize) + smallfontsize)
    if (count < bars or bars == -1) :
        fhandler.write(",\n")
        fhandler.write("['" + k + "', " + str(size) + "]") #", '" + str(size) + f" ({percentage_of_sample:.2f}%)'" + "]")
    else :
        count_other += 1
        other_category_size += size
    count += 1

if (bars > 0) :
    fhandler.write(",\n")
    percentage_of_sample = (other_category_size/ total_sample_count) * 100
    fhandler.write("['Other " + str(count_other) + " Meteorite Classes ', " + str(other_category_size) +"]") #", '" + str(other_category_size) + f" ({percentage_of_sample:.2f}%)'" + "]")

fhandler.write("\n];\n")
fhandler.close()

print("Output writtein to dabar.js")
print("Open dabar.htm in a browser to see the visualisation")