from pyspark import SparkConf, SparkContext

# Create a Spark Context and Configuration variable. 
conf = SparkConf().setMaster("local").setAppName("UserTradeCount")
sc = SparkContext(conf = conf)

# Create a function that is capable of parsing the data that I want. 
def parseLine(line):
    fields = line.split('|')
    gender = fields[2]
    trade = fields[3]
    return (gender, trade)

# Loading u.user file into an RDD called Lines.
lines = sc.textFile('file:///Spark/u.user')

#Applying parseLine function to every item in RDD. 
parsedLines = lines.map(parseLine)

# Creating a Tuple with every line. 
genderAndTradesCounts = parsedLines.map(lambda x: (x, 1))

# Reduce by Key and total up occurances. 
totals = genderAndTradesCounts.reduceByKey(lambda x, y: x + y)

# Collect the results. 
results = totals.collect()

# Print out the results to the console. 
for x in results:
    print(x)
'''
Input: 
1|24|M|technician|85711
2|53|F|other|94043
3|23|M|writer|32067

Output: 
(('F', 'artist'), 13)
(('M', 'engineer'), 65)
(('F', 'scientist'), 3)
(('M', 'salesman'), 9)
(('M', 'scientist'), 28)
(('F', 'administrator'), 36)
(('M', 'lawyer'), 10)
(('F', 'librarian'), 29)
'''