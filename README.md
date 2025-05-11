# YouTube API & Google Sheets Integration: Video Pulse Writer

This project automates fetching video metrics ("pulse" data) from the YouTube Data API v3 and writing them to a Google Sheet. It utilizes a Google Service Account for authentication.

## Prerequisites

*   Python 3.x (ensure your environment meets the requirements in `requirements.txt`)
*   A Google Cloud Project with the following APIs enabled:
    *   YouTube Data API v3
    *   Google Sheets API
*   A `service_account.json` file:
    *   Obtain this file from your Google Cloud Project's "IAM & Admin" > "Service Accounts" section.
    *   The service account associated with this file must have appropriate permissions (e.g., roles/iam.serviceAccountUser and any roles needed for YouTube Data API access and Google Sheets editing).

## Setup

1.  **Clone the Repository (if applicable):**
    If this project is in a Git repository, clone it to your local machine.

2.  **Install Dependencies:**
    Navigate to the project directory in your terminal and install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Service Account Configuration:**
    *   Place your downloaded `service_account.json` file into the root directory of this project.
        *(Alternatively, update the script to point to the correct path of your `service_account.json` file if it's stored elsewhere.)*
    *   **Share Google Sheet:** Open the Google Sheet you intend to write data to. Click on "Share" and add the `client_email` (found within your `service_account.json` file) as an Editor.

## Usage

1.  **Configure Script (if necessary):**
    Open the main Python script for this project. You may need to update variables such as:
    *   The ID or name of the target Google Sheet.
    *   Specific YouTube video IDs, channel IDs, or search queries for fetching data.
    *   Any other parameters specific to the script's logic.

2.  **Run the Script:**
    Execute the main Python script from your terminal:
    ```bash
    python your_main_script_name.py
    ```
    *(Note: Replace `your_main_script_name.py` with the actual filename of the Python script that orchestrates the API calls and sheet writing.)*

This will initiate the process of fetching data from YouTube and populating your Google Sheet. Check the script's output or logs for any status messages or errors.
