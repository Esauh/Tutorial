import botometer
import pandas as pd
import matplotlib.pyplot as plt

rapidapi_key = "Enter Your Key"
twitter_app_auth = {
    'consumer_key': 'Enter Your Key',
    'consumer_secret': 'Enter Your Key',
    'access_token': 'Enter Your Key',
    'access_token_secret':'Enter Your Key'
}
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)
training_set = pd.read_csv("Enter File Location for Your Training Set")
ids = training_set['id'].tolist()

human_eng = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
bot_eng = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
org_eng = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
human_univ = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
bot_univ = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
org_univ = pd.DataFrame(columns=["astroturf", "fake follower", "financial",
                                  "other", "overall", "self-declared", "spammer"])
