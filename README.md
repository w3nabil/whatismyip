# WhatIsMyIP

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12.x-green?style=for-the-badge&logo=python" alt="Python Version 3.12.x">
  <img src="https://img.shields.io/codacy/grade/b38941dc42f046df8601495bdfbe9672?style=for-the-badge&logo=codacy&label=Codacy%20GRADE" alt="Codacy Grade">
  <img src="https://img.shields.io/github/license/w3nabil/whatismyip?style=for-the-badge&logo=github&label=License" alt="License">
</div>

## Overview
**WhatIsMyIP** is a lightweight Flask-based web application that allows users to retrieve their public IP address along with key location and security details. This tool is useful for network diagnostics, security analysis, and general IP-related inquiries.

## Features
- Retrieve public IP details, including:
  - **IP Address**
  - **IP Version**
  - **Geolocation Data** (Latitude, Country, City, Region)
  - **Proxy Detection**
- Lightweight, fast, and easy to use
- Simple web interface

## Prerequisites
- Python 3.12 or later
- [Ngrok](https://ngrok.com/) (for external access)

## Installation
Follow these steps to install and run the application:

1. Clone the repository:
    ```sh
    git clone https://github.com/w3nabil/WhatIsMyIP.git
    ```
2. Navigate to the project directory:
    ```sh
    cd WhatIsMyIP
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration
1. Rename `.env.example` to `.env` and update it with your desired configuration values.
   - If using the project for testing purposes, you may set:
     ```
     DB_URI=./test.db
     APP_SECRET_KEY=test
     ```
   - Database configuration is optional unless you plan to store data.
   
2. Obtain an API token from [ipinfo.io](https://ipinfo.io/) and set it in the `.env` file:
   ```
   TOKEN=your_api_token_here
   ```

## Usage
Start the application by running:
```sh
py app.py
```
Once running, open a browser and navigate to `http://localhost:5000/` to verify that the service is working correctly.

To make the application accessible from the internet:
1. Start Ngrok:
   ```sh
   ngrok http 5000
   ```
2. Copy the generated `*.ngrok.io` URL and access it from any browser.

## Troubleshooting
### Rate Limit Reached
If you encounter a "Rate Limit Reached" message, it may be due to:
- Exceeding API request limits
- A blacklisted or flagged IP address

Refer to the [ipinfo.io documentation](https://ipinfo.io/developers) for more details on API limits and restrictions.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact
For questions, feedback, or collaboration opportunities, feel free to reach out at **w3nabil@gmail.com**.
