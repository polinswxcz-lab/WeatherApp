from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import (
FavoriteCity
)

from django.shortcuts import redirect
from .services import get_forecast
from .forms import (
    CitySearchForm
)

from .services import (
    get_weather
)


def home(request):

    weather = None
    error = None

    form = CitySearchForm(
        request.GET or None
    )

    if form.is_valid():

        city = (
            form.cleaned_data[
                "city"
            ]
        )

        weather = (
            get_weather(city)
        )

        if weather is None:

            error = (
                "Місто не знайдено"
            )

        elif weather is False:

            error = (
                "API недоступний"
            )

    return render(
        request,
        "weather/index.html",
        {
            "form": form,
            "weather": weather,
            "error": error
        }
    )

def forecast(request, city):

    data = get_forecast(city)

    error = None

    if data is None:
        error = "Не знайдено місто"

    elif data is False:
        error = "Помилка API"

    return render(
        request,
        "weather/forecast.html",
        {
            "data": data,
            "error": error
        }
    )

@login_required
def favorites(request):

    cities = (
        FavoriteCity.objects
        .filter(
            user=request.user
        )
    )

    return render(
        request,
        "weather/favorites.html",
        {
            "cities": cities
        }
    )


@login_required
def add_favorite(
    request,
    city,
    country
):

    FavoriteCity.objects.create(

        user=request.user,

        city_name=city,

        country_code=country

    )

    return redirect(
        "favorites"
    )

@login_required
def remove_favorite(
    request,
    id
):

    city = (
        FavoriteCity.objects
        .get(
            id=id,
            user=request.user
        )
    )

    city.delete()

    return redirect(
        "favorites"
    )