#!/bin/bash
# take in URL, displays acceptable HTTP methods
curl -sI "$1" | grep "Allow" | cut -c 8-
