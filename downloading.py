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

for id, result in bom.check_accounts_in(ids):
    try:
        if result["user"]["majority_lang"] == 'en':
            row = pd.DataFrame([[
                result['display_scores']['english']['astroturf'],
                result['display_scores']['english']['fake_follower'],
                result['display_scores']['english']['financial'],
                result['display_scores']['english']['other'],
                result['display_scores']['english']['overall'],
                result['display_scores']['english']['self_declared'],
                result['display_scores']['english']['spammer']]],
                columns=["astroturf", "fake follower", "financial",
                         "other", "overall", "self-declared", "spammer"])

            if (training_set.iat[ids.index(id), 1]).lower() == 'human':
                human_eng = pd.concat([human_eng, row], ignore_index=True)
            elif (training_set.iat[ids.index(id), 1]).lower() == 'bot':
                 bot_eng = pd.concat([human_eng, row], ignore_index=True)
            elif (training_set.iat[ids.index(id), 1]).lower() == 'organization':
                org_eng = pd.concat([human_eng, row], ignore_index=True)




