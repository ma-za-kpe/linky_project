## Step 1: Create a new app:

`python manage.py startapp tags`

## Step 2: Add the app to `INSTALLED_APPS` in `settings.py`:

`'tags.apps.TagsConfig',`

## Step 3: Run migrations for the first time:

`python manage.py migrate`

## Step 4: Create a model called `Tags` with a many-to-many relationship to projects

## Step 5: Update the database by creating a new migration and running migrate:

- `python manage.py makemigrations tags`
- `python manage.py migrate`

## Step 6: Register the model in the admin app by adding to `tags/admin.py`: `admin.site.register(Tags)`

## Step 7: Restrict tag actions to admins only (add, delete, update)

## Step 8: Use Django REST Framework to create a RESTful API:

- Create a `urls.py` file for URL routes
- Create a `serializers.py` file to transform data into JSON
- Create a `views.py` file to apply logic to API endpoints

## Step 9: Update the project-level `urls.py`

## Step 10: Create a `urls.py` file in the tags app with the following code:

    ```python
    from django.urls import path
    from .views import TagsList, TagDetail

    urlpatterns = [
        path('/', TagDetail.as_view()),
        path('', TagList.as_view()),
    ]
    ```

## Step 11:Create a new `serializers.py` file in the tags app:

    ```python
    from rest_framework import serializers
    from .models import Tags

    class TagSerializer(serializers.ModelSerializer):
        class Meta:
            fields = ('id', 'title')
            model = Tags
    ```

## Step 12: Create views in `views.py`:

    ```python
    from rest_framework import generics
    from .models import Tags
    from .serializers import TagSerializer

    class TagList(generics.ListCreateAPIView):
        queryset = Tags.objects.all()
        serializer_class = TagSerializer

    class TagDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Tags.objects.all()
        serializer_class = TagSerializer
    ```

## Step 13: Start the development server: `python manage.py runserver`

<!-- ## Step 14: Add permission to let only admins update, add and delete something: `permission_classes = [IsAdminOrReadOnly]` -->
