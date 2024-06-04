# Mattermost Login Script

This Python script prompts the user for a username and password, logs into Mattermost via an API call, and extracts the `Token` from the response headers for use in subsequent Mattermost API calls.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your system.
3. Install the `requests` library if you haven't already:

    ```bash
    pip install requests
    ```

## Usage

1. Replace `"https://<your-mattermost-url>"` in the script with the base URL of your Mattermost server.  (Remember to confirm http/https at the beginning, and to add any port to the end).

2. Run the script:

    ```bash
    python mattermost_login.py
    ```

3. Enter your Mattermost username and password when prompted.

4. If the login is successful, the script will print your token, which can be used for subsequent Mattermost API calls.

## Example

Here is an example of how to use the script:

```bash
$ python mattermost_login.py
Enter your Mattermost username: john.doe
Enter your Mattermost password: ********
Login successful. Your token is: xxxxxxx
```

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
