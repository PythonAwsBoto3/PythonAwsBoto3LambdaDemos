import sys
try:
    import boto3
    print"Sucessfully imported boto3"
except Exception as e:
    print"The error is: ",e
    sys.exit(1)
bucket=raw_input('Enter bucket name to delete: ')
print"Deleting  a  %s bucket ..............." %(bucket)
s3 = boto3.resource('s3')
try:
    response=s3.Bucket(bucket)
    response.delete()
    print"The bucket %s  is sucessfully deleted" %(bucket)
    sys.exit(0)
except Exception as e:
    print"The error is: ",e
    sys.exit(2)
