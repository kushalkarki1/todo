from django.db import models

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Priority(TimeStampModel):
    name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(TimeStampModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
