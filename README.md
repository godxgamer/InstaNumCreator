# InstaNumCreator - Instagram Account Number Creator

InstaNumCreator is a Python script designed to automate the creation of Instagram accounts using numerical patterns. This script leverages the InstaGenPro API, allowing users to streamline the process of creating multiple Instagram accounts efficiently.

## Features

- Seamless integration with the InstaGenPro API.
- User-friendly interface for quick account creation.
- Proxy support for secure and anonymous operations.
- SMS-based OTP verification for enhanced security.

## Prerequisites

Before using InstaNumCreator, ensure you have the following:

- InstaNumCreator API key: Obtain your API key from [InstaNumCreator](http://telegram.me/god_x_gamer).

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/InstaNumCreator.git
    cd InstaNumCreator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install requests
    ```

3. **Replace placeholder values:**

   - Replace `YOUR_API_KEY` in the `headers` with your actual InstaNumCreator API key.
   - Update `number` with the desired phone number for Instagram registration.
   - Modify `proxy_path` with your proxy details.

## Usage

Execute the script by running:

```bash
python instanumcreator.py
```

## InstaNumCreator API Documentation

## Overview

InstaNumCreator is a Python script designed to automate the creation of Instagram accounts using numerical patterns. This script utilizes the InstaGenPro API to streamline the process of creating multiple Instagram accounts efficiently.

## API Endpoints

### 1. Send OTP to Email
- **Baseurl:** `http://128.140.99.16:5623`
- **Endpoint:** `/api/insta/android/number/send`
- **Method:** `POST`
- **Description:** Sends an OTP to the provided number for Instagram registration.
- **Request Headers:**
  ```json
  {
      "Content-Type": "application/json",
      "X-API-Key": "None"
  }
  ```
- **Request Body:**
```{
    "number": "Number",
    "proxy": "Proxy",
}
```
- **cURL Example:**
```
curl -X POST \
  http://128.140.99.16:5622/api/insta/android/number/send \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: Your-API-Key' \
  -d '{
    "number": "number",
    "proxy": "username:password@host:port",
  }'
```



