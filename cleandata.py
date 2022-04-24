#Cameron,David,Kaitleigh
#4/5/22

import csv
import re

search_list = [" trian" , "triangle "]
data = [1]
data_no = [0]

outputCol = open('keywordCol.csv', 'w', newline = '')

writer = csv.writer(outputCol)
# we want to create keywords but we want to make sure there are no mistakes,
# for instance, we have "fired", "bored", and these contain "red", so we 
# do not want to count those, so our keywords need to be " red ", " reddish ",
# etc, but if there is a special character beside " red" or "red ",
# then we would still count, because it would be a /.
#open our dataset in "read-mode" 
with open('deepCleanedData.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if re.compile('|'.join(search_list),re.IGNORECASE).search(row[7]):
            writer.writerow(data)
        else:
            writer.writerow(data_no)
