# python 3

import os

sync_command = f"aws s3 sync s3://fileuploaddemobucket/blue s3://fileuploaddemobucket1/"
os.system(sync_command)
