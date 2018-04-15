#!/usr/bin/env python

import sys
import boto3

db = sys.argv[1] #name of the instance to be deleted

rds = boto3.client('rds')
try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db
        SkipFinalSnapshot=True)
    print response
except Exception as error:
    print error