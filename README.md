# Web-App-Directory-Hunter

## Overview

This Python script is a simple directory enumeration tool that checks a target URL for the existence of directories specified in a list. It uses the requests library to send HTTP GET requests to the target URL with each directory appended, and then checks the response. If a valid response is received, it is considered a "discovered directory."

### Usage

To use this tool, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/directory-enumeration-tool.git
   ````
2. Install the required dependencies. You can use **pip** to install the **requests** library:
   ```bash
   pip install requests
   ```
3. Run the script with the following command, replacing [target_url] and [list_file] with your target URL and the file containing the list of directories to check:
   ```bash
   python directory_enum.py
   ```
4. The script will iterate through the directories in the list and check if they exist on the target URL. If a directory is found, it will be displayed in the console.

### Example

```bash
[*] Enter Target URL: https://example.com
[*] Enter List Containing Directories: directories.txt
[*] Discovered Directory: https://example.com/directory1
[*] Discovered Directory: https://example.com/directory2
[*] Discovered Directory: https://example.com/directory3
```
