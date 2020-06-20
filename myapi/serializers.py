from rest_framework import serializers

from .models import Userinfo, ActivityPeriod

import datetime


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


'''
class ActivityPeriodFormat(serializers.RelatedField):
    def to_representation(self, value, read_only=True):
        # duration = time.strftime('%M:%S', time.gmtime(value.duration))
        # return 'Track %d: %s (%s)' % (value.order, value.name, duration)
        return value.start_time.strftime(("%b %d %Y %I %M %p "))
'''


class UserinfoSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)
    # activity_periods = ActivityPeriodFormat(many=True,)

    class Meta:
        model = Userinfo
        fields = ('id', 'real_name', 'tz', 'activity_periods',
                  )
