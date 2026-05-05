from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Complaint
from .serializer import ComplaintSerializer

from django.db.models import Q, When, Case, IntegerField

# Create your views here.

# set token
from rest_framework.permissions import IsAuthenticated
class ComplaintView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        complaint=Complaint.objects.all()
        serializer=ComplaintSerializer(complaint, many=True)

        return Response({
            "Message":"Data fetched successfully",
            "Data":serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message":"Data created successfully",
                "Data":serializer.data
            }, status=status.HTTP_201_CREATED)
        
     
        
class ComplaintIDView(APIView):
    def get(self, request, id):
        try:
            complaint=Complaint.objects.get(pk=id)
            serializer=ComplaintSerializer(complaint)
            return Response({
                "Message":"data fetched successfully",
                "Data":serializer.data
            },status=status.HTTP_200_OK)
        
        except Complaint.DoesNotExist:
            return Response({
                "Message":"Data not found",

        }, status=status.HTTP_404_NOT_FOUND)


    def delete(sefl, request, id):
        try:
            complaint=Complaint.objects.get(pk=id)
            if complaint:
                complaint.delete()
                return Response({
                    "Message":"Data deleted successfully"
                },status=status.HTTP_200_OK)
            
        except Complaint.DoesNotExist:
            return Response({
                "Message":"Data not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        try:
            complaint=Complaint.objects.get(pk=id)
            if complaint:
                serializer=ComplaintSerializer(complaint, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "Message":"Data updated successfully",
                        "Data":serializer.data
                    }, status=status.HTTP_202_ACCEPTED)
                else:
                     return Response({
                "Message":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
                

        except Complaint.DoesNotExist:
             return Response({
                "Message":"Data not found"
            },status=status.HTTP_404_NOT_FOUND)
           


# Filter 
class ComplaintFilter(APIView):
    def get(self, request):
        complaint=Complaint.objects.all()

        status_filter = request.GET.get("status") 
        if status_filter:
            complaint = complaint.filter(status=status_filter)

        priority_filter = request.GET.get("priority")
        if priority_filter:
            complaint = complaint.filter(priority=priority_filter)

        category_filter = request.GET.get("categroy")
        if category_filter:
            complaint = complaint.filter(category=category_filter)

        location_filter = request.GET.get("location")
        if location_filter:
            complaint=complaint.filter(location=location_filter)

        total_count = complaint.count()

        serializer = ComplaintSerializer(complaint, many=True)
        return Response({
            "Message":"data fetched successfully",
            "Count":total_count,
            "Data":serializer.data
            
        }, status=status.HTTP_200_OK)



# Dashbord
class ComplaintDashboardView(APIView):
    def get (self, request):

        total=Complaint.objects.count()
        pending=Complaint.objects.filter(status="Pending").count()
        resolved=Complaint.objects.filter(status="Resolved").count()
        in_progress=Complaint.objects.filter(status="In progress").count()
        high_priority=Complaint.objects.filter(priority="High").count()
        medium_priority=Complaint.objects.filter(priority="Medium").count()
        low_priority=Complaint.objects.filter(priority="Low").count()

        data={
            "Total":total,
            "Pending":pending,
            "Resolved":resolved,
            "In_progress":in_progress,
            "High":high_priority,
            "Medium":medium_priority,
            "Low":low_priority
        }

        return Response({
            "DATA":data
        }, status=status.HTTP_202_ACCEPTED)



# seaech
class ComplaintSearchView(APIView):
    def get(self,request):
        query=request.GET.get('search')

        complaint=Complaint.objects.all()

        if query:
            complaint=complaint.filter (Q(title__icontains=query) | 
                                        Q(description__icontains=query)| 
                                        Q(customer_name__contains=query) |
                                        Q(location__icontains=query))
                      
        serializer=ComplaintSerializer(complaint, many=True)
        return Response({
            "Data":serializer.data            
        }, status=status.HTTP_202_ACCEPTED)




# date ordering
class ComplaintOrderingView(APIView):

    def get(self, request):
        complaints = Complaint.objects.all()

        ordering = request.GET.get('ordering', '-created_at')  # default

        # ⭐ Priority mapping
        if 'priority' in ordering:
            complaints = complaints.annotate(
                priority_order=Case(
                    When(priority='Low', then=1),
                    When(priority='Medium', then=2),
                    When(priority='High', then=3),
                    output_field=IntegerField()
                )
            )

            # Replace 'priority' with 'priority_order'
            ordering = ordering.replace('priority', 'priority_order')

        # 🔹 Apply ordering (single line)
        complaints = complaints.order_by(ordering)

        serializer = ComplaintSerializer(complaints, many=True)

        return Response({
            "count": complaints.count(),
            "data": serializer.data
        })



#divide into page by page

from rest_framework.pagination import PageNumberPagination

class complaintPageView(APIView):
    def get(self, request):
        complaint = Complaint.objects.all()

        paginator = PageNumberPagination() #I created a paginator instance

        #I passed the queryset and request to paginate_queryset
        paginated_data = paginator.paginate_queryset(complaint, request) 

        # Then I serialized the paginated data.
        serializer = ComplaintSerializer(paginated_data, many=True)

        #I returned the response using get_paginated_response, which includes metadata like count, next, and previous links.
        return paginator.get_paginated_response(serializer.data)



# Singup
from .serializer import SingUpSerializer
class SignUpAPI(APIView):
    def post (self, request):
        serializer = SingUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message":"signUp successfully",
                "Data":serializer.data
            })
        else:
            return Response({"error":serializer.errors})
# LogIn
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class LogInAPI(APIView):
    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")

        user=authenticate(username = username,
                          password = password)
        print(user)
        data = {}
        if user:
            refresh = RefreshToken.for_user(user)
            data['user'] = {
                "username":user.username,
            }
            data['token'] = {
                "refresh":str(refresh),
                "access":str(refresh.access_token)
            }
        if user is not None:
            return Response({
                "Message":"LogIn successfully",
                "Data":data
            })
        else:
            return Response({
                "Message":"In valid user"
            })