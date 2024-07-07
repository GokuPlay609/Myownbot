#!/bin/bash

# Check if MONGO_URI is set
if [ -z "${MONGO_URI}" ]; then
  # If not, use Railway's built-in database
  echo "Using Railway's built-in database"
  DATABASE_URL=$(railway db url)
  export MONGO_URI=$DATABASE_URL
fi

# Run the Python script
python bot.py
