# Outline:

- These 2 programs use Google Takeout and the YouTube API in order to automate the tedious task of unsubscribing from old channels that I do not watch anymore. A more detailed description lies below.

# Purpose:

- Through this project I was able to use my knowledge of python and craft a project that meant I could automate a tedious task and better appreciate programming and its usefulness. Being made to interact with the tricky yet well documented YouTube Data API, I learned how APIs truly work and their finer nuances, which will go some way in helping me as I try to build my own.

# Description:

- Program 1 - unsub_hist.py
    - This program looks at 2 JSON files from Google Takeout, watch-history and subscriptions.
    - It loops through the 2, first creating a dictionary of channels I have watched more than once in the past 3 months and then ultimately creating a dictionary of channels I have not watched along with their unique subscription id.
    - It then shelves this data for program 2 to access.
- Program 2 - unsub_api.py
    - This program accesses the tedious YouTube DATA API in order to unsubscribe.
    - It requires an API Key and since it is user consent based, it requires a OUATH CLIENT SECRET JSON file and a particular scope under which to run. It takes in the file and scope to create a flow object under the InstalledAppFlow method and creates credentials using the console log method of the flow object which is passed onto the build function when creating the request object.
    - Run the code from the command line as it requires a verification code during runtime, and there is a api request limit of 10,000 points per day with an unsubscribe request being 50 points.
