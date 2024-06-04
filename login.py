import requests

def login_to_mattermost():
    # Prompt the user for username and password
    username = input("Enter your Mattermost username: ")
    password = input("Enter your Mattermost password: ")

    # Define the Mattermost API login URL
    api_url = "https://<your-mattermost-url>/api/v4/users/login"

    # Create the login payload
    payload = {
        "login_id": username,
        "password": password
    }

    # Make the API request to login
    response = requests.post(api_url, json=payload)

    # Check if the login was successful
    if response.status_code == 200:
        # Extract the token from the response headers
        token = response.headers.get('Token')
        if token:
            print("Login successful. Your token is: ", token)
            return token
        else:
            print("Login failed. Token not found in response headers.")
    else:
        print("Login failed. Status code: ", response.status_code)

if __name__ == "__main__":
    login_to_mattermost()
