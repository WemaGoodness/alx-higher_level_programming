#!/bin/bash
# This script makes a request to a URL and causes the server to respond
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
