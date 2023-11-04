from phonenumber_field import serializerfields
from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_image = serializers.ImageField(source="author.image")

    class Meta:
        model = Comment
        fields = (
            "pk",
            "text",
            "author_id",
            "author_first_name",
            "author_last_name",
            "created_at",
            "ad_id",
            "author_image",
        )


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_id = serializers.ReadOnlyField(source="author.id")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = (
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id",
        )



class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
