#!/bin/bash
# Sends a POST request with email and subject variables to a given URL
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
