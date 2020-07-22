#!/bin/bash

ssh ubuntu@18.138.24.228 -L 4000:localhost:$1 -L 4001:localhost:$2 -R $3:localhost:4002
