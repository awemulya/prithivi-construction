import datetime
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from progress.models import Rows, Task
from project.models import Project


class TaskRowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rows
        fields = ('id', 'description', 'progress_status', 'status', 'start_date', 'deadline')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class TaskSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    site_name = serializers.ReadOnlyField(source='site.name')
    rows = TaskRowSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'description', 'progress_status', 'status', 'start_date', 'deadline', 'rows', 'site_id',
                  'site_name')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        task = Task.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            row = Rows()
            row.description = data.get('description')
            row.progress_status = data.get('progress_status','started')
            row.status = data.get('status', False)
            row.start_date = data.get('start_date', datetime.datetime.today)
            row.deadline = data.get('deadline', datetime.datetime.today)
            row.task = task
            row.save()
        return task

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        task = Task.objects.get(pk=instance.id)
        task.description = validated_data.pop('description')
        task.progress_status = validated_data.pop('progress_status','started')
        task.status = validated_data.pop('status', False)
        task.start_date = validated_data.pop('start_date', datetime.datetime.today)
        task.deadline = validated_data.pop('deadline', datetime.datetime.today)
        task.save()
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if id:
                row = Rows.objects.get(pk=id)
                row.description = data.get('description')
                row.progress_status = data.get('progress_status','started')
                row.status = data.get('status', False)
                row.start_date = data.get('start_date', datetime.datetime.today)
                row.deadline = data.get('deadline', datetime.datetime.today)
                row.task = task
                row.save()
            else:
                row = Rows()
                row.description = data.get('description')
                row.progress_status = data.get('progress_status','started')
                row.status = data.get('status', False)
                row.start_date = data.get('start_date', datetime.datetime.today)
                row.deadline = data.get('deadline', datetime.datetime.today)
                row.task = task
                row.save()

        return task


class SiteProgressSerializer(serializers.ModelSerializer):
    progresses = SerializerMethodField('get__site_progresses', read_only= True)

    class Meta:
        model = Project
        fields = ('id', 'progresses',)

    def get__site_progresses(self, site):
        progress_list = site.task.all()
        serializer = TaskSerializer(instance=progress_list, many=True)
        return serializer.data