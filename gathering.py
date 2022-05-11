import botometer
import pprint
import pandas
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

#Check a single account by screen name
result = bom.check_account('@UniqueTwitterId')

#Check a single account by id
result = bom.check_account(1548959833)

#Check a sequence of accounts
accounts = ['@clayadavis', '@onurvarol', '@jabawack']
for screen_name, result in bom.check_accounts_in(accounts):
    print(screen_name)
    print(result)
    #Do stuff with 'screen_name' and 'result'

accounts_info = []
accounts_place = []

for screen_name, result in bom.check_accounts_in(accounts):
    pprint.pprint(result)
    row = {}
    # we use a try-catch because we do not want it to stop execution if botometer fails to get stats on an account.
    try:
        if(result["user"]["majority_lang"] == 'en'):
# use the english results
            row = {
                "id": result["user"]["user_data"]["id_str"],
                "CAP": result['cap']['english'],
                "astroturf": result['display_scores']['english']['astroturf'],
                "fake_follower": result['display_scores']['english']['fake_follower'],
                "financial": result['display_scores']['english']['financial'],
                "other": result['display_scores']['english']['other'],
                "overall": result['display_scores']['english']['overall'],
                "self-declared": result['display_scores']['english']['self_declared'],
                "spammer": result['display_scores']['english']['spammer'],
            }
        else:
            row = {
                "id": result["user"]["user_data"]["id_str"],
                "CAP": result['cap']['universal'],
                "astroturf": result['display_scores']['universal']['astroturf'],
                "fake_follower": result['display_scores']['universal']['fake_follower'],
                "financial": result['display_scores']['universal']['financial'],
                "other": result['display_scores']['universal']['other'],
                "overall": result['display_scores']['universal']['overall'],
                "self-declared": result['display_scores']['universal']['self_declared'],
                "spammer": result['display_scores']['universal']['spammer'],
            }

    accounts_info.append(row)
    accounts_place.append(screen_name)

    print(f'{result["user"]["user_data"]["id_str"]} has been processed.')  # you can then add it to a dataframe or do whatever you want to here with the row
    except Exception as e:
    print("{} Could not be fetched:  {}".format(id, e))


accounts_info_df = pandas.DataFrame(accounts_info, index=accounts_place)
accounts_info_df.to_csv('completed_twitter_info_v2.csv')