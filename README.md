# social_network

# Friend Request API

This is a Django-based API for managing friend requests between users. It includes endpoints to send, accept, reject, list friends, and list pending friend requests. The API also includes rate-limiting to prevent users from sending more than three friend requests within a minute.

## Features

- API to search other users by email and name(paginate up to 10 records per page).
    - a) **If search keyword matches exact email then return user associated with the email.**
    - b) **If the search keyword contains any part of the name then return a list of all users.**
    eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
    then all of these users should be shown in the search result because "am"
    substring is part of all of these names.
    - c) **There will be only one search keyword that will search either by name or email.**
- API to send/accept/reject friend request
- API to list friends(list of users who have accepted friend request)
- List pending friend requests(received friend request)
- Users can not send more than 3 friend requests within a minute.



## Requirements

- Python 
- Django 
- Django REST Framework

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/imabhishekpatel/social_network.git
cd social_network
```

### 2. Create and Activate a Virtual Environment

```bash
# For Windows
python -m venv env
env\Scripts\activate

# For macOS and Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Set Up Django Project

```bash
python manage.py migrate

```

### 5. Create a Superuser

```bash
python manage.py createsuperuser

```

### 6. Run the Development Server

```bash
python manage.py runserver

```

## Postman Collection

You can download and import the Postman collection to easily test all endpoints. Click the link below to access the collection:

https://api.postman.com/collections/36003342-a6192e26-ea9d-4d80-9924-f6d5566b91e7?access_key=PMAT-01J6Q9Y8345NYHG4TSAH203TJZ
