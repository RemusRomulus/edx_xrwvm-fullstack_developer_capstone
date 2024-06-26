# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # path for user registration
    path(route='register', view=views.registration, name='register'),

    # path to get cars
    path(route='get_cars', view=views.get_cars, name='get_cars'),

    # path for dealer info view
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(
        route='get_dealers_with_rating/<str:rating>',
        view=views.get_dealers_by_rating,
        name='get_dealers_by_rating'
    ),

    # path for dealer details view
    path(
        route='dealer/<int:dealer_id>',
        view=views.get_dealer_details,
        name='dealer_details'
    ),

    # Get Dealer Review
    path(
        route='reviews/dealer/<int:dealer_id>',
        view=views.get_dealer_reviews,
        name='dealer_reviews'
    ),

    # path for add a review view
    path(
        route='add_review',
        view=views.add_review,
        name='add_review'
    )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
