#!/bin/bash

pkill python
python /home/ubuntu/Development/tmp/twilio/server.py &
python /home/ubuntu/Development/tmp/twilio/call.py
