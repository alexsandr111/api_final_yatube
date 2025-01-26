from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор постов"""

    author = serializers.SlugRelatedField(slug_field='username',read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'group', 'image']


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев"""

    author = serializers.SlugRelatedField(read_only=True,slug_field='username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
        read_only_fields = ['author', 'post']

class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор групп"""
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']

class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор подписок"""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:

        fields = ('user','following')
        model = Follow

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user','following'),
            message='Подписка уже совершена'
        )
    ]

    def validate(self, data):
        """Валидация"""
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Подписка на самого себя недоступна.'
            )
        return data