#!/bin/bash
# send JSON POST request to URL and display response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2"
