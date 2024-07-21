

# Create your models here.
from django.db import models
import uuid

def user_directory_path(instance, filename):
    return f'user_{instance.unique_code}/{filename}'

class FileUpload(models.Model):
    unique_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.unique_code})"
