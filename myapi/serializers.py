from rest_framework import serializers

from .models import Userinfo, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserinfoSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Userinfo
        fields = ('id', 'real_name', 'tz', 'activity_periods')
