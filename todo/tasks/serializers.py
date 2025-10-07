from rest_framework import serializers
from .models import Task, Category
from datetime import date


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'category', 'due_date', 'status']
        permission_fields = ['user','created_at']


    # 1️⃣ Validate title (not empty or too short)
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    # 2️⃣ Validate due_date (cannot be in the past)
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    # 3️⃣ Validate status (custom rule)
    def validate_status(self, value):
        if value not in ['Pending', 'Completed']:
            raise serializers.ValidationError("Status must be either 'Pending' or 'Completed'.")
        return value

    # 4️⃣ Object-level validation (check multiple fields together)
    def validate(self, data):
        if data['status'] == 'Completed' and not data['description']:
            raise serializers.ValidationError("Completed tasks must have a description.")
        return data

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)

    def create(self, validated_data):
        # view থেকে context এর মাধ্যমে user পাওয়া যায়
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

