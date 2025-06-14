from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from account.models import SpotifyUser
from account.serializers import SpotifyUserSerializer
from post.models import Post
from post.serializers import PostSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search(request):
    data = request.data
    query = data['query']
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    users = SpotifyUser.objects.filter(display_name__icontains=query)
    users_serializer = SpotifyUserSerializer(users, many=True)

    posts = Post.objects.filter(
        Q(body__icontains=query, is_private=False) | 
        Q(created_by_id__in=list(user_ids), body__icontains=query)
    )

    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }, safe=False)