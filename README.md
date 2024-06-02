
# Udemy Course Scraper 📚

## Introduction 🌟
The Udemy Course Scraper is a Python-based tool designed to fetch and organize course data from Udemy. It leverages the Udemy API to gather information on courses across various categories, including Python, Data Science, and Web Development. The scraper extracts vital course details such as title, URL, paid/free status, description, subscriber count, and more, storing the data in a structured JSON format.

## Table of Contents 📑
- [Introduction](#introduction-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Features](#features-)
- [Dependencies](#dependencies-)
- [Configuration](#configuration-)
- [Documentation](#documentation-)
- [Examples](#examples-)
- [Troubleshooting](#troubleshooting-)
- [Contributors](#contributors-)
- [License](#license-)

## Installation 🛠️
To install the Udemy Course Scraper, you need Python 3.x installed on your system. Then, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Usage 🚀
To use the scraper, follow these steps:
1. Ensure you have the `course_urls.txt` file with the desired Udemy course URLs formatted correctly.
2. Run the scraper script:
   ```
   python Scraper.py
   ```
3. The scraped data will be stored in the specified directory as JSON files, organized by course category.

## Features ✨
- Fetches course details from Udemy through API calls.
- Supports multiple course categories.
- Extracts comprehensive course information.
- Stores data in a structured JSON format for easy access and analysis.

## Dependencies 📦
- `requests>=2.25.1`
- `beautifulsoup4>=4.9.3`

These can be installed via pip as mentioned in the [Installation](#installation-) section.

## Configuration ⚙️
Modify the `course_urls.txt` file to include URLs for the courses you wish to scrape. Each URL should be preceded by a comment indicating the course category, for example:
```
# Python Course
https://www.udemy.com/course-url...
```

## Documentation 📖
Refer to the official documentation of the `requests` and `beautifulsoup4` libraries for more detailed information on how the scraping and parsing operations are performed.

## Examples 🌈
An example `course_urls.txt` file is included in the project. You can add or modify URLs as needed to scrape data for different courses or categories.

## Troubleshooting 🔧
If you encounter any issues with scraping, ensure the Udemy API endpoints have not changed and that your internet connection is stable. Check the `requests` status code to debug any failed requests.

## Contributors 🤝


Feel free to contribute to the project by submitting pull requests or opening issues.

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.
