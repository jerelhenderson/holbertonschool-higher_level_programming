#!/bin/bash
# takes in, sends requests from URL, and displays the body size of response
curl -sI "$1" | grep "Content-Length:" | cut -d: -f2 | cut -d' ' -f2
