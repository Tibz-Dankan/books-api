from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_pages(self, value):
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError("Pages must be an integer.")

    def create(self, validated_data):
        validated_data['pages'] = int(validated_data.get('pages', 0))
        print("validated_data['pages']: ",validated_data['pages'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['pages'] = int(validated_data.get('pages', 0))
        return super().update(instance, validated_data)
