from pyspark import SparkConf, SparkContext

# Create a Spark Context and Configuration variable. 
conf = SparkConf().setMaster("local").setAppName("UserTradeCount")
sc = SparkContext(conf = conf)

# Create a function that is capable of parsing only the data that I want. 
def parseLine(line):
    fields = line.split('|')
    gender = fields[2]
    trade = fields[3]
    return (gender, trade)

# Loading u.user file into an RDD called Lines.
lines = sc.textFile('file:///SparkCourse/u.user')

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
Input Data: 
1|24|M|technician|85711
2|53|F|other|94043
3|23|M|writer|32067
4|24|M|technician|43537
5|33|F|other|15213
6|42|M|executive|98101

Output Data:
(('M', 'educator'), 69)
(('F', 'educator'), 26)
(('F', 'student'), 60)
(('M', 'technician'), 26)
(('F', 'engineer'), 2)
(('F', 'programmer'), 6)
'''