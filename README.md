# Catalyst Count

## Overview
Catalyst Count is a web application built using Django 3.x/4.x, PostgreSQL, and Bootstrap 4/5. The application allows users to log in and upload large CSV data files (up to 1GB) with visual progress indicators. Once the file is uploaded, the application updates the database with the contents of the file and provides a form for users to filter the data and view the count of records based on the applied filters.

## Features
1. **User Authentication**: Secure login and registration using Django AllAuth.
2. **File Upload**: Upload large CSV files with chunk upload method for efficient handling.
3. **Database Update**: Update the PostgreSQL database with the uploaded CSV data.
4. **Data Filtering**: Filter the uploaded data using a form and display the count of records that match the filter criteria.
5. **API Integration**: Use Django Rest Framework to return the filtered result count.

## Expected Pages
1. **Login Page**: User authentication page.
2. **Upload Data Page**: Page for users to upload large CSV files.
3. **Query Builder Page**: Page for users to filter the data and view the count of matching records.
4. **Users Page**: Manage user accounts.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x/4.x
- PostgreSQL
- Git

### Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/catalyst-count.git
    cd catalyst-count
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    - Create a `.env` file in the root directory of the project.
    - Add the following environment variables:
        ```
        DEBUG=1
        SECRET_KEY=your_secret_key
        DATABASE_NAME=your_db_name
        DATABASE_USER=your_db_user
        DATABASE_PASSWORD=your_db_password
        DATABASE_HOST=your_db_host
        DATABASE_PORT=your_db_port
        ```

5. **Run the initial migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

7. **Download and unzip the test data set**
    - Download the dataset from [here](https://www.dropbox.com/s/at6f63rdznw4bqs/free-7-million-company-dataset.zip?dl=0)
    - Unzip the file in a suitable directory.

8. **Run the development server**
    ```bash
    python manage.py runserver
    ```

## Usage
1. Navigate to the login page and log in with your credentials.
2. Go to the upload data page to upload a CSV file.
3. Use the query builder page to filter the data and view the count of matching records.
4. Manage user accounts on the users page.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [django-environ](https://github.com/joke2k/django-environ)
- [django-allauth](https://github.com/pennersr/django-allauth)
