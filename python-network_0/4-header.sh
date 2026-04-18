#!/bin/bash
# Sends a GET request with a header variable X-School-User-Id=98
curl -sH "X-School-User-Id: 98" "$1"
