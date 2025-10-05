from django.urls import path
from .views import SignupView, LoginView, MovieListView, ShowListView, BookSeatView, CancelBookingView, MyBookingsView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/shows/', ShowListView.as_view()),
    path('shows/<int:pk>/book/', BookSeatView.as_view()),
    path('bookings/<int:pk>/cancel/', CancelBookingView.as_view()),
    path('my-bookings/', MyBookingsView.as_view()),
]
