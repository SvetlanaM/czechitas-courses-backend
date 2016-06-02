from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import CourseVenue

class CitySerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.CharField(source='get_city')
    dates = serializers.SerializerMethodField()
    states = serializers.SerializerMethodField()

    def get_dates(self, obj):
        temp = Course.objects.get(id=obj.id).audit_log.all()
        for i in temp:
            return i.action_date

    def get_states(self, obj):
        temp = Course.objects.get(id=obj.id).audit_log.all()
        for i in temp:
            return i.action_date

    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'city',
            'dates',
            'states',
        )

class CourseVenueSerializer(serializers.HyperlinkedModelSerializer):
    dates = serializers.SerializerMethodField()
    states = serializers.SerializerMethodField()

    def get_dates(self, obj):
        temp = CourseVenue.objects.get(id=obj.id).audit_log.all()
        for i in temp:
            return i.action_date

    def get_states(self, obj):
        temp = CourseVenue.objects.get(id=obj.id).audit_log.all()
        for i in temp:
            return i.action_date

    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'title',
            'street_name',
            'street_number',
            'city',
            'dates',
            'states',
        )
