# TopicTalk - Django Project

TopicTalk is a web platform developed using Django that allows users to engage in discussions on various topics. Users can create topics, post messages, and interact with other users through comments.

## Features

- **User Registration and Authentication:** Users can sign up and log in to the platform to create and participate in discussions.

- **Topic Creation:** Users can create new discussion topics and provide descriptions.

- **Message Posting:** Users can post messages within discussion topics.

- **Commenting:** Users can comment on messages within topics to engage in conversations.

- **User Profiles:** Users can view their profiles, including their created topics, posted messages, and comments.

- **Search Functionality:** Users can search for specific topics or keywords.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/salahsaeed19/Dashboard_Boards.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database by applying migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. Register or log in to start using the platform.

2. Create new topics and provide descriptions.

3. Post messages within topics to initiate discussions.

4. Interact with other users by commenting on messages.

5. Explore other users' profiles to see their activities.

6. Use the search functionality to find specific topics or keywords.

## Project Structure

- **`topics` Directory:** Contains the Django app for managing topics, messages, and comments.

- **`accounts` Directory:** Contains the app for user registration and authentication.

- **`templates` Directory:** Holds HTML templates for rendering web pages.

- **`static` Directory:** Contains static assets like CSS, JS, and images.

- **`urls.py`:** Defines URL patterns for different views.

- **`models.py`:** Defines the database models for topics, messages, comments, and user profiles.

- **`views.py`:** Contains view functions for rendering pages and handling user actions.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request or issue on the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/salahsaeed19/) file for details.

## Created By

- Salahuddin Abu Saif

## Date

1st September 2023
```
