import requests

# Step 1: Set up your credentials
client_id = '130208'
client_secret = '27e2ad6b4be13544e7e02fbe523c7d20d8a52f4a'
redirect_uri = 'http://localhost:8000/exchange_token'

auth_url = f'https://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&approval_prompt=force&scope=read_all,activity:read_all'
print(f'Go to this URL and authorize the app: {auth_url}')
auth_code = input('Enter the authorization code: ')
grant_type = auth_code

# Manually input the authorization code you get after authorizing the app

# Step 3: Exchange authorization code for access token
def get_access_token(client_id, client_secret, code):
    response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )
    return response.json()

token_response = get_access_token(client_id, client_secret, auth_code)
access_token = token_response['access_token']
print(f'Access Token: {access_token}')

# Step 4: Make API requests
def get_athlete_data(access_token):
    response = requests.get(
        'https://www.strava.com/api/v3/athlete',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    return response.json()

athlete_data = get_athlete_data(access_token)
print(athlete_data)

def get_activities(access_token, per_page=30, page=1):
    response = requests.get(
        f'https://www.strava.com/api/v3/athlete/activities?per_page={per_page}&page={page}',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    return response.json()

activities = get_activities(access_token)
print(activities)