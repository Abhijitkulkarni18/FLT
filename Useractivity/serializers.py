from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from Useractivity.models import User, Activity
from Assignment import settings


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('real_name','tz')

class ActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format=settings.DATE_TIME_INPUT, input_formats=settings.DATE_TIME_INPUT_FORMATS)
    end_time = serializers.DateTimeField(format=settings.DATE_TIME_INPUT, input_formats=settings.DATE_TIME_INPUT_FORMATS)
    class Meta:
        model = Activity
        fields = ('id','start_time','end_time',)

class UserSerializer(serializers.ModelSerializer):
    activity_periods = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','real_name','tz','activity_periods')

    def get_activity_periods(self, obj):
        activity = Activity.objects.filter(user=obj.id)
        return ActivitySerializer(activity, many=True).data