from django.shortcuts import render
from user_management.models.customUserModel import CustomUser
from rest_framework.response import Response
from rest_framework import generics
from user_management.serializers.userSerializer import UserSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # get data from request
        search_keyword = request.query_params.get('search', '')
        page = int(request.query_params.get('page', 1))
        per_page_limit = int(request.query_params.get('per_page_limit', 10))
        
        if '@' in search_keyword:
            # Search by exact email match
            users = CustomUser.objects.filter(email=search_keyword)
        else:
            # Search by partial name match
            users = CustomUser.objects.filter(
                Q(first_name__icontains=search_keyword) |
                Q(last_name__icontains=search_keyword)  |
                Q(username__icontains=search_keyword)
            )
        
        # Paginate the results
        total_count = users.count()
        start = (page - 1) * per_page_limit
        end = start + per_page_limit
        paginated_users = users[start:end]
        
        serializer = UserSerializer(paginated_users, many=True)
        
        return Response({
            'results': serializer.data,
            'total_count': total_count,
            'page': page,
            'per_page_limit': per_page_limit
        })
    