#!/bin/sh

sleep 5

echo - Stopping django

pkill -SIGINT -f 'manage.py runserver'

echo - Ok