#!/usr/bin/env python
import sys
import boto3

ec2 = boto3.resource('ec2')
for instance_id in sys.argv[1:]:
    response = ec2.instances.terminate(instance_id)
    print (response)


