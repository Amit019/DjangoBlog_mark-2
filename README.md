# DjangoBlog_mark-2
This is Blog website  reated in Django 

# About

This is a simple project to practice Django. The idea was to create some basic blogging platforms.

It was built using Python 3.6 + Django and the database is SQLite. Bootstrap 5 was used for styling.

It includes a login and registration functionality.

The user has his own blog page, where he can add new blog posts and new categories. Can comment on each of the posts

Each authenticated user can like and dislike posts made by other users.

It is very easy to use

# Features

 1. Font Hand user interface for Add Blog Posts and Categories
 2. Add new features easily
 3. Add new style easily and replace old style (style.css)
 

# How to run

1. Install requirements 
   1.1  Python 3.6 above versions
   1.2  Django 3.1 above versions
   1.3 Pillow
   1.4 Django-ckeditor
   
2. Default
   You can run the application from the command line with manage.py. Go to the root folder of the application.

    > Run migrations:   
    
    >>  python manage.py migrate
    
    >>>  python manage.py runserver 8000
    

#  Django Admin
     
     .  Default  superUser is create
     
     .  Default Username ==> admin
     
     .  Default Password  ==> admin
     
     . Default Email address ==> admin@gmail.com
     
 It is possible to add an additional admin user who can login to the admin site. Run the following command:
  
    python manage.py createsuperuser
    
  Enter your choice username and press Enter
  
    Username: admin_username 
  
  You will then be prompted for your email address:
  
    Email address: admin@example.com  
  
  The final step is to enter your desired password. You will be asked to enter your password twice, the second time as a confirmation of the first.
  
     Password: **********
  
     Password (again): *********
  
     Superuser created successfully.

  Go to the browser and visit http://localhost:8000/admin
