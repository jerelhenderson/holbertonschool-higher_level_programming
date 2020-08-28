#!/bin/bash
# send request to URL and display status code of response
curl -sLI "$1" -o /dev/null -w "%{http_code}"
