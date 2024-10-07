from project.models import Project, Tag, Task, Location
from django.db import transaction

def insert_project():
    project_data = {
        "name" : "Sun Moon",
        "location" : "17 no road, Banani",
        "description" : "Nice",
        "tasks" : ["Buying cement"],
        "tags" : ["medium"]
    }

    with transaction.atomic():
        p1 = Project.objects.create(
            name=project_data["name"],
            description=project_data["description"]
        )

        Location.objects.create(address=project_data['location'])

        for task in project_data["tasks"]:
            Task.objects.create(title=task, project=p1)
        
        created_tags = []
        for tag in project_data["tags"]:
            t = Tag.objects.create(name=tag)
            created_tags.append(t)
        
        # p1.tags.add(created_tags[0], created_tags[1])
        p1.tags.add(*created_tags)