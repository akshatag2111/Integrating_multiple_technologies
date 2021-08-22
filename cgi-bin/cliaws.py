#Python Program for creating a connection
import boto3

ec2 = boto3.client('ec2',
                   'ap-south-1',
                   aws_access_key_id='',
                   aws_secret_access_key='')

#This function will describe all the instances
#with their current state
response = ec2.describe_instances()
print(response)
