from rest_framework import serializers

from posts.models import Post, Group, Comment


class NameRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class PostSerializer(serializers.ModelSerializer):
    author = NameRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author',
                  'image', 'group', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug',
                  'description')


class CommentSerializer(serializers.ModelSerializer):
    author = NameRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post',
                  'text', 'created')
        read_only_fields = ('post',)
