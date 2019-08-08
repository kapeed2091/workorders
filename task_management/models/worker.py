from django.contrib.auth.models import AbstractUser
from django.db import models
from task_management.models import AbstractDateTime


class Worker(AbstractUser):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('task_management.Company',
                                on_delete=models.CASCADE)
    # email field is included in AbstractUser model

    class Meta:
        app_label = 'task_management'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @classmethod
    def create(cls, name, email, company_name):
        from task_management.models import Company
        company, _ = Company.objects.get_or_create(name=company_name)
        worker = cls.objects.create(
            username=cls._generate_random_string(),
            name=name, email=email, company=company)
        return {'worker_id': worker.id}

    @classmethod
    def remove(cls, worker_id):
        try:
            worker = cls.objects.get(id=worker_id)
            worker.delete()
        except cls.DoesNotExist:
            raise Exception

    @classmethod
    def _generate_random_string(cls, size=8):
        import string
        import random
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(size))

    @classmethod
    def is_valid(cls, worker_id):
        try:
            cls.objects.get(id=worker_id)
            return True
        except cls.DoesNotExist:
            return False
