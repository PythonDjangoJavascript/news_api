from rest_framework import serializers
from datetime import datetime
from django.utils.timesince import timesince

from news.models import Airticle


# class AirticleSerializer(serializers.Serializer):
#     """Serialize article model"""

#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         """Create airticle data in the database"""
#         print(validated_data)
#         return Airticle.objects.create(**validated_data)

#     def update(self, instace, validated_data):
#         """Update Airticle in the database"""

#         instace.author = validated_data.get('author', instace.author)
#         instace.title = validated_data.get('title', instace.title)
#         instace.description = validated_data.get(
#             'description', instace.description)
#         instace.body = validated_data.get('body', instace.body)
#         instace.location = validated_data.get('location', instace.location)
#         instace.publication_date = validated_data.get(
#             'publication_date', instace.publication_date)
#         instace.active = validated_data.get('active', instace.active)

#         instace.save()
#         return instace

#     def validate(self, data):
#         """Validate object level attrs"""

#         if data['title'] == data['description']:
#             raise serializers.ValidationError(
#                 "Title and Description must be different")
#         return data

#     def validate_title(self, value):
#         """Validated Field level attr here title"""

#         if len(value) < 10:
#             raise serializers.ValidationError(
#                 "Title must be 10 character long")
#         return value


# Model serializer Practice

class AirticleSerializer(serializers.ModelSerializer):
    """Seializes Article Model"""

    time_science_publication = serializers.SerializerMethodField()

    class Meta:
        model = Airticle
        exclude = ('id',)
        # fields = '__all__' # we can add all model fields
        # fields = ('title', 'description', 'body')  # we can add only these fields

    def get_time_science_publication(self, object):
        """define extra attribute besides Article Model"""

        # this pub_date is our model pub date and here object is article instance
        publication_date = object.publication_date
        now = datetime.now()
        # lets calculte time period between new and pub date
        time_delta = timesince(publication_date, now)

        return time_delta

    def validate(self, data):
        """validate object lavel validation"""

        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and Descripiton can not be same')
        return data

    def validate_title(self, value):
        """Validate field level attribute here title"""

        if len(value) < 20:
            raise serializers.ValidationError(
                'Title must be 20 character long')
        return value
