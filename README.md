# Repository for: IT Grow Division Test
The repository contains notebook, script and pdf files as required for the test for Middle Python Developer (Machine Learning/AI). 
## Table of Contents

- [Getting Started](#getting-started)
- [Task 1](#task-1)
- [Task 2](#task-2)
- [Task 3](#task-3)
- For explaination for Task 2 and 3, please refer to `Task Explanation Document.pdf`. For task 1, the notebook contains explanation.

## Getting Started 
1. Clone the repository:
   ```bash
   git clone https://github.com/tawhidwasik08/itgd-test.git
   ```
2. Move into project directory in command line
    ```bash 
    cd itgd-test/
    ```
3. Create a new python virtual environment
    ```bash
      python -m venv itgd_venv
     ```
4. Activate the virtual environment (for windows)
    ```bash
      itgd_venv\Scripts\Activate.bat
     ```
5. Run the following command to install all the required pacakges
      ```bash
      pip install -r requirements.txt
      ```
6. For each file to run kindly look in the following sections.

## Task 1 
1. Make sure you are in the repo directory. Run the following command to open up the notebook. 
      ```bash
      jupyter notebook task_1.ipynb
      ```
2. The notebook contains the necessary details regarding this task.

## Task 2 
1. Make sure you are in the repo directory and the virtual environment is active. Run the following command to execute the script. 
      ```bash
      python task_2.py
      ```
2. If the database file is missing it will be auto created and some dummy data will be generated upon first execution.
3. You will be prompted with 10 different options for interacting with database. 
4. User table related functions:
- `Add User` :Adds a new user to the database with a specified name and email.
- `Get user info by id`: Returns user information based on the provided user ID.
- `Update user`:Updates the name and email of an existing user based on their ID.
- `Delete user`:Deletes a user based on their ID.
5. User table related functions:
- `Add Post`:Adds a new post associated with a specified user, with a given title and text.
- `Get post info by id`: Returns post information based on the provided post ID.
- `Get all posts for a user`: Returns a list of all posts associated with a specific user.
- `Update post`: Updates the title and text of an existing post based on its ID.
- `Delete post`: Deletes a post based on its ID.
6. `See current db tables`: View all data from each table

## Task 3
1. Utilizes the gspread library to interact with Google Sheets, requiring the service account credentials file. So, make sure `itgd-tasks-72817a0cdc72.json` file exists in the working directory.
2. Run the following command to execute the script. 
      ```bash
      python task_3.py
      ```
3. You will be greeted with 2 options.
- `Show data from sheet`: You can view the full data from the [sheet]( https://docs.google.com/spreadsheets/d/1aaUWd0m2RKZ1H5QoScPUgZGkk9w2-pyIrPw_o6aXuBE/edit?usp=sharing) resided in google drive. 
- `Add a new row to existing sheet`: Once seleted, you will be given proper prompts to input a new data row in the sheets file.
