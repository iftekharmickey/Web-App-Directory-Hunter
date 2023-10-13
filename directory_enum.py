# Import the 'requests' library for making HTTP requests
import requests

# Prompt the user to enter the target URL and the file containing directories
target_url = input('[*] Enter Target URL: ')
file_name = input('[*] Enter List Containing Directories: ')

# Define a function to send an HTTP GET request to a given URL
def request(url):
    try:
        # Send an HTTP GET request to the given URL
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        # Handle a ConnectionError exception, which may occur if the URL is not reachable
        pass

# Open the file containing the list of directories for reading
file = open(file_name, 'r')

# Iterate through each line (directory) in the file
for line in file:
    directory = line.strip()  # Remove leading/trailing whitespace
    full_url = target_url + '/' + directory  # Create the full URL by combining the target URL and the directory
    response = request(full_url)  # Send an HTTP GET request to the full URL
    if response:
        # If a response is received (status code 200 or similar), print the discovered directory
        print('[*] Discovered Directory: ' + full_url)

