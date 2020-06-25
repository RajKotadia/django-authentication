# Django Authentication

- Django authentication boilerplate based on the default `User` model and the `UserCreationForm`.
- Uses `Bootstrap4` for styling.

## To run it locally

1. Clone the project and install the dependencies.

   ```bash
   cd django-authentication
   pip install -r requirements.txt
   ```

2. Make the necessary migrations to setup the default django models.

   ```bash
   python manage.py migrate
   ```

3. Create a superuser so that you can access the User model through the admin interface at `/admin`.

   ```bash
   python manage.py createsuperuser
   ```

4. Once the above steps are completed, the project will be up and running on `localhost:8000` by executing the following command.

   ```bash
   python manage.py runserver
   ```
