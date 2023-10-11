# Web Directory and File Enumerator #

This Python tool is designed to facilitate the enumeration of directories and files on web and application servers. It allows users to input a target URL and a list of directories, after which the tool systematically attempts to access these directories using HTTP requests. While not a comprehensive iterative search, it provides a basic directory and file name enumeration method for initial web application assessment.

Key Features:

- Input a target URL for directory enumeration
- Utilize a list of directories for testing
- Efficiently discover accessible directories and potential file paths
- Please note that this tool is intended for ethical and responsible use, such as website security assessments, and should not be used for any unauthorized or malicious activities

## Usage ##

```python3 dirscanner.py```

- Deploy with Target IP
- Execute with Directory List

# FAQ #

## What is get()? ##

The `get()` method sends a GET request to the specified URL. It is used to retrieve and request data from a specified resource in a server.

## What is ConnectionError? ##

In the event of a network problem (e.g., DNS failure, refused connection, etc.), requests will raise a `ConnectionError` exception.
