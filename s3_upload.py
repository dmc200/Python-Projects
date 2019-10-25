import boto3
from __future__ import print_function
import base64
import json

print('Loading function')


def lambda_handler_orion_data(event, context):
    s3 = boto3.client('s3')
    
    #Open File for writing stream data to. 
    f = open('test_document.csv','w')

    #Loop over records in source Kinesis stream.
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        #write each record to a csv file with a new line character.
        f.write(payload + ',' + '\n')
        
    #upload file to whatever s3 bucket is needed. 
    s3.upload_file('*fileName*','*bucketName*','*destinationFileName*')
    f.close()
    return 'Successfully processed {} records into Orion Bucket.'.format(len(event['Records']))



