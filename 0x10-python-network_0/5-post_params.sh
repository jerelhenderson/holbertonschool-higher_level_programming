#!/bin/bash
# take and send POST request to URL, and display response body
curl -sX -d POST "$1" "email=hr@holbertonschool.com&subject=I will always be here for PLD"
