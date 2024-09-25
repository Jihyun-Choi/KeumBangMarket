from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta definition for AddressSerializer."""

        model = Address
        fields = [
            "id",
            "address_line",
            "postal_code",
        ]
        read_only_fields = [
            "id",
        ]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Address.objects.create(user_id=user_id, **validated_data)
