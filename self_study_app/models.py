from django.db import models
from ckeditor.fields import RichTextField


class Course(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, related_name='questions')
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.question
