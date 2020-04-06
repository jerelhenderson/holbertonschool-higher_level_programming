#!/bin/bash
# send request to `0.0.0.0:5000/catch_me` and receive message "You got me!"
curl -sL 0.0.0.0:5000/catch_me -X PUT "You got me!" -d user_id=98
