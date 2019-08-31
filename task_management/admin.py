from django.contrib import admin

from task_management.models import (
    Company, Worker, Order, OrderWorker
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company_id']


class OrderWorkerStackedInline(admin.StackedInline):
    model = OrderWorker
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'deadline']
    inline = [OrderWorkerStackedInline, ]