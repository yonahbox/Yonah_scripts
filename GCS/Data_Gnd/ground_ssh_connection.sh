#!/bin/bash

ssh -i $(find -name *YonahAWSPrivateKey-30Jul19) ubuntu@ec2-18-138-24-228.ap-southeast-1.compute.amazonaws.com -L 4000:localhost:$1 -L 4001:localhost:$2 -R $3:localhost:4002
