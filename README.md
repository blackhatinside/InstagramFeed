<!-- 

Author:Post		1:M
Post:Comment	1:M


Author:
	name
	email

Post:
	author (who posted)
	title
	content
	created_at

Comment:
	post (under which post)
	author (who commented)
	content
	created_at

 -->

create an app 'social'
```
	python manage.py startapp social
```
add the new app to the list of installed apps
after creating the models, do
```
	python manage.py makemigrations
	python manage.py migrate
```
in cmd, add an author
```
	python manage.py shell
	from social.models import Author
	Author.objects.create(name="Adi", email="adi@gmail.com")
```

```

# to delete
http://127.0.0.1:8000/ --> http://127.0.0.1:8000/authors/ --> http://127.0.0.1:8000/authors/1/ --> CLICK 'DELETE' button -->  http://127.0.0.1:8000/authors/ --> 

# to update
http://127.0.0.1:8000/comments/3/ --> CHANGE text in 'Content' field and click 'PUT' button

```


# DOCKER COMMANDS
to restart the docker container
`docker-compose up`

to rebuild and restart the docker container
`docker-compose up --build`

to stop the docker container
`docker-compose down`


# IMPLEMENTATION NOTES
CRUD operations are implemented through Django REST framework's ModelViewSet

CRUD operations should be implemented through Django REST framework's Generic views