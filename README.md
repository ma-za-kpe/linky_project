# LINKY
## ABOUT
- Welcome to [Linky](), a revolutionary tool designed to streamline the research and education workflow for educators, researchers, and students. Our platform recognizes the diverse needs of knowledge workers and offers a comprehensive solution to address common challenges such as information overload, fragmented workflows, and the absence of effective collaboration tools. With [linky](), users have the power to group their research materials and resources into organized projects, facilitating efficient management and collaboration within their academic and research endeavors.
## Key Features
* __Add__ Links: Easily add URLs and links to projects, allowing users to collect and organize relevant research materials,
  articles, papers, and resources.
* __View__ a list of projects created by other users
* __View__ a private list of projects
* __Delete__ project
* __Delete__ link

## OBJECTIVES

## Entities
### Users:
- **` username`**: *The username of the user.*
- **`email`**: *The email address of the user. *
- **`password`**: *The hashed password of the user.*
- **`full_name`**: *The full name of the user.*
- **`bio`**: *A short biography or description provided by the user.*
- **`profile_picture`**: *The profile picture of the user.*
- **`registration_date`**: *The date when the user registered on the platform.*
- **`role`**: *The role of the user (e.g., professor, researcher, student).*
- **`institution`**: *The educational institution or organization associated with the user.*

### Links (URLs):
- **` url`**: *The URL of the link.*
- **`title`**: *The title or name associated with the link.*
- **`description`**: *A brief description or summary of the content of the link.*
- **`added_by`**: *The user who added the link to a project.*
- **`date_added`**: *The date when the link was added to the project.*
- **`tags`**: *Optional tags or labels to categorize the link (e.g., research, reference, article).*

### Projects:
- **`title`**: *The title or name of the project.*
- **` description`**: *A description of the project, outlining its purpose and goals.*
- **`created_by`**: *The user who created the project.*
- **`date_created`**: *The date when the project was created.*
- **`last_modified`**: *The date when the project was last modified.*
- **`visibility`**: *The visibility settings of the project (e.g., public, private, shared).*
- **`collaborators`**: *A list of users who have access to the project and can collaborate on it.*
- **`links`**: *A collection of links associated with the project.*

## LIBRARIES
1.  [Django REST framework](https://www.django-rest-framework.org/)
2. [django-cors-headers](https://pypi.org/project/django-cors-headers/)
3. [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/installation.html)
4. [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html)
5. [PyYAML](https://pypi.org/project/PyYAML/)
6. [uritemplate](https://pypi.org/project/uritemplate/)
7. [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
8. [More ...]()

## INSTALLATION (MAC OS)
- Always refer to the [Django Installation](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
1. clone this repo and navigate to the linky_project folder
2. Set Up Virtual Environment: ``` python3 -m venv linky-env ```
3. Activate Virtual Environment: ``` source linky-env/bin/activate ```
4. Install Dependencies: ``` pip install -r requirements.txt ```
5. Perform Initial Database Migrations: ``` python manage.py migrate ```
6. (Optional) Create Superuser: ``` python manage.py createsuperuser ```
7. Run Development Server: ``` python manage.py runserver ```

## COMMANDS USED
* ``` python3 -m venv linky-env ```
* ``` source linky-env/bin/activate ```
* ``` python -m pip install Django ```
* ``` django-admin startproject linky_api . ``` 
* ``` python3 manage.py migrate ```
* ``` python3 manage.py runserver ```
* ``` python3 manage.py makemigrations posts ```
* ``` python3 manage.py migrate ```
* ``` python3 manage.py startapp posts ```

[//]: # (## STEPS TO RECREATE FROM SCRATCH)

[//]: # (1. Open terminal and navigate to your desktop folder run: ``` mkdir linky-project ```)

[//]: # (2. Navigate into the project: ``` cd  linky-project``` Run steps 2 and 3 from the [INSTALLATION] stage above.)

[//]: # (3. )

## BEST PRACTICES

## TODO
- Add windows installation instructions
