# DjangoBlog_mark-2
This is Blog website  reated in Django 

# About

This is a Simple project for practicing Django. The idea was to build some basic blogging platform.

It was made using Python 3.6 + Django and database is SQLite. Bootstrap 5 was used for styling. 

There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts and new Categories. Every one can comment on posts 

Every authenticated user can likes and dislikes on posts made by other users.

It very Easy to Used

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
    
    >>  python manage.py runserver 8000
    

#  Django Admin
     
     Default  superUser was created
     
     Default Username admin
     
     Default Password admin
     
     Default Email Id  admin@gmail.com
     
  It is possible to add additional admin user who can login to the admin site. Run the following command:
  
  python manage.py createsuperuser
  
  Username: admin_username (Enter your desired username and press enter.)
  
  Email address: admin@example.com  (You will then be prompted for your desired email address:)
  
  The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
  Password: **********
  Password (again): *********
  Superuser created successfully.

  Go to the web browser and visit http://localhost:8000/admin
