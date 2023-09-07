# TopicTalk

TopicTalk is a forum-like Django application that allows users to engage in discussions on a variety of topics. Users can create boards, post topics, and contribute to discussions through posts.

## Features

- Create boards to categorize discussions.
- Post topics within boards to initiate discussions.
- Contribute to discussions with individual posts.
- Responsive design for easy access on different devices.
- User authentication and security measures.
- User registration, login, and password change functionalities.

## Getting Started

These instructions will help you set up and run TopicTalk on your local machine for development and testing purposes.

### Prerequisites

- Python (3.11 or higher)
- Django (3.2 or higher)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/salahsaeed19/Dashboard_Boards.git
   cd topictalk
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin panel:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the application in your browser at http://127.0.0.1:8000/.

## Usage

- Log in using the provided superuser credentials to access the Django admin panel (`http://127.0.0.1:8000/admin/`).
- Create boards and manage user accounts through the admin panel.
- Browse existing boards and discussions on the home page.
- Click on a board to view and participate in its discussions.
- Create new topics within boards and post messages to engage in discussions.
- User registration, login, and password change functionalities are available.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/salahsaeed19/Dashboard_Boards) file for details.

## Created By

- Salah Al-Din Saeed Abu Saif

## Date

8st September 2023
```
