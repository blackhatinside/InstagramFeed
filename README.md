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