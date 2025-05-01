# Streamlit Keep Alive

## Description
This is a simple app that is designed to keep your Streamlit app alive so that it doesn't go to sleep. It checks to see if the app is running and if it is not, it will click the "Yes, get this app back up!" button. It is designed to be run as a cron job once a day.

## Environment Variables
Pass in the urls you want to keep alive as an environment variable separated by a comma. If you have an .env file.
```
STREAMLIT_URLS="https://abc.streamlit.app/,https://def.streamlit.app/"
```

