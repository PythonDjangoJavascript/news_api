from rest_framework import serializers

from news.models import Airticle


class AirticleSerializer(serializers.Serializer):
    """Serialize airticle model"""

    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """Create airticle data in the database"""
        print(validated_data)
        return Airticle.objects.create(**validated_data)

    def update(self, instace, validated_data):
        """Update Airticle in the database"""

        instace.author = validated_data.get('author', instace.author)
        instace.title = validated_data.get('title', instace.title)
        instace.description = validated_data.get(
            'description', instace.description)
        instace.body = validated_data.get('body', instace.body)
        instace.location = validated_data.get('location', instace.location)
        instace.publication_date = validated_data.get(
            'publication_date', instace.publication_date)
        instace.active = validated_data.get('active', instace.active)

        instace.save()
        return instace

    def validate(self, data):
        """Validate object level attrs"""

        if data['title'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description must be different")
        return data

    def validate_title(self, value):
        """Validated Field level attr here title"""

        if len(value) < 10:
            raise serializers.ValidationError(
                "Title must be 10 character long")
        return value
