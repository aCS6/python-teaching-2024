from rest_framework import serializers
from .models import Project, Task, Tag, Location
from django.contrib.auth.models import User



# serializers.py

from rest_framework import serializers
from .models import Project, Tag, Location

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['address']

class ProjectSerializer(serializers.ModelSerializer):
    location = LocationSerializer(write_only=True)
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'location', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        location_data = validated_data.pop('location')

        # Create or get Location
        location, created = Location.objects.get_or_create(address=location_data['address'])

        # Create the Project
        project = Project.objects.create(location=location, **validated_data)

        # Create tags and add to the project
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            project.tags.add(tag)

        return project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'project', 'created_by']



class LocationSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source='project', read_only=True)
    project_name = serializers.StringRelatedField(source='project')

    class Meta:
        model = Location
        fields = ['id', 'address', 'project_id', 'project_name']



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']



class ProjectDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    tasks = serializers.StringRelatedField(many=True)  # Or use TaskSerializer for more details
    tags = TagSerializer(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'location', 'tasks', 'tags', 'created_by']

class TaskDetailSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagSerializer(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'project', 'tags', 'created_by']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    


