# LINKY - _Revolutionizing Knowledge Management_

## ABOUT

- Welcome to [Linky](), a revolutionary tool designed to streamline the research and education workflow for educators, researchers, and students. Our platform recognizes the diverse needs of knowledge workers and offers a comprehensive solution to address common challenges such as information overload, fragmented workflows, and the absence of effective collaboration tools. With [linky](), users have the power to group their research materials and resources into organized projects, facilitating efficient management and collaboration within their academic and research endeavors.

## KEY FEATURES

- **Add** Links: Easily add URLs and links to projects, allowing users to collect and organize relevant research materials,
  articles, papers, and resources.
- **View** a list of projects created by other users
- **View** a private list of projects
- **Delete** project
- **Delete** link
- More features can be found here: [Docs](https://linky-3il1.onrender.com/swagger/)

## GOAL

- The project aims to be a game-changer for startup founders by providing a comprehensive and practical guide on how to rapidly develop a robust Minimum Viable Product (MVP) in less than a week using Django. By leveraging the power of Django and a carefully curated selection of cutting-edge dependencies, the project empowers startup founders to quickly bootstrap their MVPs while adhering to the Lean Startup methodology.

## DEPLOYMENT

- The project has been deployed to [Deploying Django on Render](https://docs.render.com/deploy-django)
- Documentation [Redoc](https://linky-3il1.onrender.com/redoc/)
- Documentation [Swagger](https://linky-3il1.onrender.com/swagger/)

## ENTITIES

- For a complete list of features, please refer to the documentation [Swagger](https://linky-3il1.onrender.com/swagger/)

### Users:

- **` username`**: _The username of the user._
- **`email`**: _The email address of the user. _
- **`password`**: _The hashed password of the user._
- **`full_name`**: _The full name of the user._
- **`bio`**: _A short biography or description provided by the user._
- **`profile_picture`**: _The profile picture of the user._
- **`registration_date`**: _The date when the user registered on the platform._
- **`role`**: _The role of the user (e.g., professor, researcher, student)._
- **`institution`**: _The educational institution or organization associated with the user._

### Links (URLs):

- **` url`**: _The URL of the link._
- **`title`**: _The title or name associated with the link._
- **`description`**: _A brief description or summary of the content of the link._
- **`added_by`**: _The user who added the link to a project._
- **`date_added`**: _The date when the link was added to the project._
- **`tags`**: _Optional tags or labels to categorize the link (e.g., research, reference, article)._

### Projects:

- **`title`**: _The title or name of the project._
- **` description`**: _A description of the project, outlining its purpose and goals._
- **`created_by`**: _The user who created the project._
- **`date_created`**: _The date when the project was created._
- **`last_modified`**: _The date when the project was last modified._
- **`visibility`**: _The visibility settings of the project (e.g., public, private, shared)._
- **`collaborators`**: _A list of users who have access to the project and can collaborate on it._
- **`links`**: _A collection of links associated with the project._

## LIBRARIES

1.  [Django REST framework](https://www.django-rest-framework.org/)
2.  [django-cors-headers](https://pypi.org/project/django-cors-headers/)
3.  [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/installation.html)
4.  [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html)
5.  [PyYAML](https://pypi.org/project/PyYAML/)
6.  [uritemplate](https://pypi.org/project/uritemplate/)
7.  [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
8.  [More ...]()

## INSTALLATION (MAC OS)

- Always refer to the [Django Installation](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

1. clone this repo and navigate to the linky_project folder
2. Set Up Virtual Environment: `python3 -m venv linky-env`
3. Activate Virtual Environment: `source linky-env/bin/activate`

## INSTALLATION (WINDOWS OS)

1. clone this repo and navigate to the linky_project folder
2. Set Up Virtual Environment: `python -m venv linky-env`
3. Activate Virtual Environment: `env\Scripts\activate`

## CONTINUE ...

4. Install all dependecies: `pip install -r requirements.txt`
5. Create `.env` file in the root folder.
6. Perform Initial Database Migrations: `python3 manage.py migrate`
7. (Optional) Create Superuser: `python3 manage.py createsuperuser`
8. Run Development Server: `python3 manage.py runserver`

## COMMANDS USED

- `python3 -m venv linky-env`
- `source linky-env/bin/activate`
- `python -m pip install Django`
- `django-admin startproject clinky-apiore .`
- `python3 manage.py migrate`
- `python3 manage.py runserver`
- `python3 manage.py makemigrations posts`
- `python3 manage.py migrate`
- `python3 manage.py startapp posts`

## BEST PRACTICES

## CONTRIBUTION

- Please refer to the [CONTRIBUTING.md](https://github.com/ma-za-kpe/linky_project/blob/main/CONTRIBUTING.md)

## TUTORIAL

- Please refer to this for a tutorial on how to add Tags app to the project: [A Project and Tags relationship](https://github.com/ma-za-kpe/linky_project/blob/main/STEPS.md)
