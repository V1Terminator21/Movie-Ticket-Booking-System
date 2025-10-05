from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Movie, Show, Booking
from .serializers import UserSerializer, MovieSerializer, ShowSerializer, BookingSerializer

# Signup
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Login
class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Movies
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Shows for a movie
class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']
        return Show.objects.filter(movie_id=movie_id)

# Book a seat
class BookSeatView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        seat_number = request.data.get('seat_number')
        show = Show.objects.get(id=pk)
        # Prevent overbooking
        if Booking.objects.filter(show=show, status='booked').count() >= show.total_seats:
            return Response({'error': 'No seats available'}, status=status.HTTP_400_BAD_REQUEST)
        # Prevent double booking
        if Booking.objects.filter(show=show, seat_number=seat_number, status='booked').exists():
            return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
        booking = Booking.objects.create(user=request.user, show=show, seat_number=seat_number)
        return Response(BookingSerializer(booking).data)

# Cancel booking
class CancelBookingView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        booking = Booking.objects.get(id=pk, user=request.user)
        booking.status = 'cancelled'
        booking.save()
        return Response({'message': 'Booking cancelled successfully'})

# User bookings
class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
