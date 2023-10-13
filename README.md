# Web-App-Directory-Hunter

## Overview

This Python script is a simple directory enumeration tool that checks a target URL for the existence of directories specified in a list. It uses the requests library to send HTTP GET requests to the target URL with each directory appended, and then checks the response. If a valid response is received, it is considered a "discovered directory."

### Usage

To use this tool, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/directory-enumeration-tool.git
   ````
2. Install the required dependencies. You can use `pip` to install the `requests` library:
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

### Dependencies

This script relies on the following external Python library:

- [requests](https://pypi.org/project/requests/): Used for sending HTTP GET requests to the target URL.

### Legal and Ethical Considerations

- This script is provided for educational purposes only. Using it for unauthorized access to any system is illegal and unethical.
- Ensure that you have explicit permission to test the security of the target website.
- Always adhere to applicable laws, regulations, and ethical guidelines.

### Disclaimer

The author of this script is not responsible for any illegal or unethical use of the script. Use it responsibly and with permission.

### Author

This tool was developed by Iftekhar Tahir. If you have any questions or feedback, feel free to contact me at iftekhar.tahir@proton.me.
