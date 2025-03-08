from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,
        related_name='courses'
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        related_name='enrolled_courses',
        blank=True
    )
    materials = models.FileField(upload_to='course_materials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Feedback Model
class Feedback(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='feedback'
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student.username} on {self.course.title}"

# StatusUpdate Model
class StatusUpdate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,
        related_name='status_updates'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status by {self.user.username}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
