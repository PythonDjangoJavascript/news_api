from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework import serializers, status
from job_news.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    """Serializes Job offers model"""

    time_science_publicaiton = serializers.SerializerMethodField()

    class Meta:
        model = JobOffer
        exclude = ('id',)

    def get_time_science_publicaiton(self, object):
        """Define Extra field time science in the api"""
        created_at = object.created_at
        now = datetime.now(timezone.utc)
        # Calculate Time Science
        return timesince(created_at, now)

    def validate(self, data):
        """Validet attributes of the model"""

        if data['company_name'] == data['job_title']:
            raise serializers.ValidationError(
                detail='company name and job title must be different',
                code=status.HTTP_400_BAD_REQUEST
            )
        return data

    def validate_job_title(self, value):
        """Validate Title length"""
        if len(value) < 10:
            raise serializers.ValidationError(
                detail='Title must be at least 10 charecter long',
                code=status.HTTP_400_BAD_REQUEST
            )
        return value
