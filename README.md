# Django Blog App

A simple blog application built with Django that allows users to create, read, update, and delete blog posts.

## Features
- User authentication (Login/Register)
- Create, edit, and delete blog posts
- View all blog posts with pagination
- Comment system for posts
- Responsive design

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/django-blog.git
   cd django-blog
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Demo Video  

<video width="560" height="315" controls>
  <source src="https://github.com/Mariam1341/Django-Course-Projects/blob/main/Final%20Project/bandicam%202021-11-20%2013-53-55-456.mp4" type="video/mp4">
</video>

## Technologies Used
- Python
- Django
- SQLite/PostgreSQL
- HTML, CSS, Bootstrap

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-source and available under the [MIT License](LICENSE).
