import csv
def loadArr(dataFile):
    with open(dataFile,'r') as csv_file:
        reader=csv.reader(csv_file)
        urls_data=[]
        for row in reader:
            urls_data.append(row)
    return urls_data
