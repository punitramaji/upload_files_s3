#!/usr/bin/python

import os
import sys
import boto3

path = 'public/'
local_directory = os.path.dirname(path)
bucket = "fileuploaddemobucket"
if sys.argv[1] == 'blue':
  destination = "blue"
else:
  destination = "green"

client = boto3.client('s3')

# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    # construct the full Dropbox path
    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = os.path.join(destination, relative_path)

    # relative_path = os.path.relpath(os.path.join(root, filename))

    print 'Searching "%s" in "%s"' % (s3_path, bucket)
    try:
        client.head_object(Bucket=bucket, Key=s3_path)
        print "Path found on S3! Skipping %s..." % s3_path

         #try:
             #client.delete_object(Bucket=bucket, Key=s3_path)
         #except:
             #print "Unable to delete %s..." % s3_path
    except:
        print "Deleting %s..." % s3_path
        client.delete_object(Bucket=settings.bucket, Key=f"destination/")
        print "Uploading %s..." % s3_path
        client.upload_file(local_path, bucket, s3_path)
