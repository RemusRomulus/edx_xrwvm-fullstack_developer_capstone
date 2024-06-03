# Uncomment the required imports before adding the code
from enum import Enum
from pprint import pformat

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Import Models
from .models import CarMake, CarModel
from .populate import initiate

# Import RESTAPIs
from .restapis import get_request, analyze_review_sentiments, post_review


# Get an instance of a logger
logger = logging.getLogger(__name__)


class CONSTANTS(Enum):
    REG_ERROR = -1
    SUCCESS = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 403

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {
        'userName': ''
    }
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    context = {}
    data = json.loads(request.body)
    username = data.get('userName', CONSTANTS.REG_ERROR)
    password = data.get('password', CONSTANTS.REG_ERROR)
    first_name = data.get('firstName', CONSTANTS.REG_ERROR)
    last_name = data.get('lastName', CONSTANTS.REG_ERROR)
    email = data.get('email', CONSTANTS.REG_ERROR)
    username_exist = False
    email_exist = False
    if CONSTANTS.REG_ERROR in data.values():
        data = {
            'userName': CONSTANTS.REG_ERROR.value,
            'error': 'Incomplete Registration Attempt'
        }
        logger.warning(f'Incorrect Registration Attempt: {pformat(data)}')
        return JsonResponse(data)
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))
    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
    else :
        data = {"userName":username,"error":"Already Registered"}
    return JsonResponse(data)

def get_cars(request):
    logger.info('visiting get_cars')
    count = CarMake.objects.filter().count()
    logger.info(count)

    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_models in car_models:
        cars.append(
            {
                'CarModel': car_model.name,
                'CarMake': car_model.car_make.name
            }
        )
    
    return JsonResponse(
        {'CarModels': cars}
    )
# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request, state=None):
    print(state)
    endpoint = '/fetchDealers'
    if state:
        endpoint = f'/fetchDealers/{state}'
    dealerships = get_request(endpoint)
    return JsonResponse(
        {
            'status': CONSTANTS.SUCCESS.value,
            'dealers': dealerships
        }
    )

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request,dealer_id):
    if (dealer_id):
        endpoint = f'/fetchReviews/dealer/{str(dealer_id)}'
        reviews = get_request(endpoint)
        for review in reviews:
            response = analyze_review_sentiments(review.get('review'))
            print(response)
            review['sentiment'] = response['sentiment']
        return JsonResponse(
            {
                'status': CONSTANTS.SUCCESS.value,
                'review': reviews
            }
        )
    else:
        return JsonResponse(
            {
                'status': CONSTANTS.BAD_REQUEST.value,
                'message': CONSTANTS.BAD_REQUEST.name
            }
        ) 

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    print('Get Dealer Details by ID')
    print(dealer_id)
    if (dealer_id):
        endpoint = f'/fetchDealer/{str(dealer_id)}'
        dealership = get_request(endpoint)
        review_endpoint = f'/fetchReviews/dealer/{str(dealer_id)}'
        reviews = get_request(review_endpoint)
        for review in reviews:
            response = analyze_review_sentiments(review.get('review'))
            review['sentiment'] = response['sentiment']
            review['sentiment'] = positive
            review['id'] = 4
            review['name'] = 'Gerald Jerblonski'
            review['car_make'] = 'Nissan'
            review['car_model'] = 'Casparian Velmar Mk 35'
            review['car_year'] = '2105'
        print(dealership)
        print(f'Reviews: {reviews}')
        return JsonResponse(
            {
                'status': CONSTANTS.SUCCESS.value,
                'dealer': dealership,
                'review': reviews
            }
        )
    else:
        return JsonResponse(
            {
                'status': CONSTANTS.BAD_REQUEST.value,
                'message': CONSTANTS.BAD_REQUEST.name
            }
        )

# Get Dealers by Rating
def get_dealers_by_rating(request, rating):
    if (rating):
        endpoint = f'/fetchDealers/rating/{rating}'
        dealers = get_request(endpoint)
        for rating_detail in dealers:
            response = analyze_review_sentiments(rating_detail['rating'])
            print(response)
            rating_detail['sentiment'] = f'This dealer has a {response["sentiment"]} review'
        return JsonResponse(
            {
                'status': CONSTANTS.SUCCESS.value,
                'dealers': dealers
            }
        )
    else:
        return JsonResponse(
            {
                'status': CONSTANTS.BAD_REQUEST.value,
                'message': CONSTANTS.BAD_REQUEST.name
            }
        )

def get_dealers_by_rating_state(request, rating, state):
    if (rating and state):
        endpoint = f'/fetchDealers/rating/{str(rating)}/location/{state}'
        dealers = get_request(endpoint)
        for rating_detail in dealers:
            response = analyze_review_sentiments(rating_detail['rating'])
            print(response)
            rating_detail['sentiment'] = f'This dealer has a {response["sentiment"]} review'
        return JsonResponse(
            {
                'status': CONSTANTS.SUCCESS.value,
                'dealers': dealers
            }
        )
    else:
        return JsonResponse(
            {
                'status': CONSTANTS.BAD_REQUEST.value,
                'message': CONSTANTS.BAD_REQUEST.name
            }
        )

# Create a `add_review` view to submit a review
def add_review(request):
    OUT = {'status': CONSTANTS.REG_ERROR.value}
    if(request.user.is_anonymous == False):
        data = json.loads(request.body)
        try:
            response.post_review(data)
            OUT['status'] = CONSTANTS.SUCCESS.value
            OUT['message'] = f'::SUCCESS:: Posted: {data}'
            return JsonResponse(OUT)
        except Exception as err:
            OUT['status'] = CONSTANTS.BAD_REQUEST.value
            OUT['message'] = f'::ERROR:: Error in Posting Review: {data}'
            return JsonResponse(OUT)
    else:
        OUT['status'] = CONSTANTS.UNAUTHORIZED.value
        OUT['message'] = CONSTANTS.UNAUTHORIZED.name
        return JsonResponse(OUT)
