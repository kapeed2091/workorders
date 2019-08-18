from workorders.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('RDS_DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    }
}

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'sqreen-static-storage'
