#!/bin/bash
# Displays the size of the body of a response in bytes for a given URL
curl -s "$1" | wc -c
