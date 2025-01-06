# Hotels Hub

Hotels Hub is a Django-based web application built using the Django Rest Framework (DRF) to manage hotels, bookings, and user profiles efficiently. It provides APIs for hotel management, user authentication, and booking functionalities.

## Features

- **Hotel Management:**
  - Add, update, and delete hotels with essential details like name, location, and amenities.
  - Filter and search hotels based on specific criteria (e.g., location, price).

- **Booking System:**
  - Create and manage hotel bookings.
  - Check room availability and validate booking dates.

- **User Authentication and Profiles:**
  - User registration and login system with secure authentication.
  - Role-based access for customers and administrators.

- **Email Notifications:**
  - Automated email notifications for booking confirmations and other events using **Mailpit** and Celery.

- **Task Queue and Background Processing:**
  - Efficient task handling with **Celery** for sending emails and other asynchronous processes.
  - **Redis** is used as the message broker for Celery.

- **Advanced API Features:**
  - Pagination for handling large datasets.
  - Custom error handling for improved user experience.

- **Scalable Design:**
  - Designed to handle multiple hotels, bookings, and users efficiently.
  - Integration-ready with third-party APIs for payment or external booking platforms.

## Tech Stack

- **Backend:**
  - Python
  - Django
  - Django Rest Framework

- **Database:**
  - PostgreSQL (or any compatible database supported by Django).

- **Task Queue:**
  - Celery (asynchronous task queue).
  - Redis (message broker).

- **Email Testing:**
  - Mailpit (for email notifications during development).

- **Deployment:**
  - Docker (for containerization).
  - Gunicorn (for running the application).

- **Development and Testing Tools:**
  - Postman (API testing).
  - Pytest (for unit testing).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Omarmoatz/Hotels-Hub-Using-Django-and-DRF.git
   cd Hotels-Hub-Using-Django-and-DRF

2. Create a virtual environment and activate it:
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install the dependencies:
      ```bash
      pip install -r requirements.txt


4. Apply migrations:

      ```bash
      python manage.py migrate
5. Start Redis server:

      ```bash
      redis-server


6. Start Celery worker:
      ```bash
      celery -A your_project_name worker --loglevel=info


7. Run Mailpit (for email testing during development):
      ```bash  
      mailpit


8. Run the development server:
      ```bash   
      python manage.py runserver


Access the application at http://localhost:8000.

## Contributing
- Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

## License
- This project is licensed under the MIT License. See the LICENSE file for more details.
- This version includes **Celery**, **Redis**, and **Mailpit** in the features, tech stack, and install
