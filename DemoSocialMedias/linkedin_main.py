import requests
import json

from linkedin_utils import auth, headers


def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
    user_info = response.json()
    return user_info

def save_data(filename, data):
    """
    Write token to credentials file.
    """
    data = json.dumps(data, indent=4)
    with open(filename, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    credentials = 'credentials.json'
    access_token = auth(credentials)  # Authenticate the API
    headers = headers(access_token)  # Make the headers to attach to the API call.
    user_info = user_info(headers)  # Get user info


    print(user_info)
    save_data('me_data.json', user_info)
