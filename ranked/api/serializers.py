from rest_framework import serializers
from ranked.models import SixMans

class RankedSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SixMans
        fields = [
            'url',
            'user',
            'elo',
            'mmr',
            'rank',
        ]

    # Converts to JSON
    # Validates data

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_name(self, value):
        qs = SixMans.objects.filter(user__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This player is already in the database")
        return value