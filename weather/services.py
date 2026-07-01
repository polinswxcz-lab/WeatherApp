import requests

from django.conf import settings
from django.core.cache import cache


def get_weather(city):

    cache_key = (
        f"weather_{city}"
    )

    cached = (
        cache.get(
            cache_key
        )
    )

    if cached:

        return cached

    url = (
        "https://api.openweathermap.org"
        "/data/2.5/weather"
    )

    params = {

        "q": city,

        "appid":
        settings.OPENWEATHER_API_KEY,

        "units":
        "metric",

        "lang":
        "uk"

    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        data = (
            response.json()
        )

        if response.status_code != 200:

            return None

        cache.set(

            cache_key,

            data,

            timeout=600

        )

        return data

    except:

        return False


def get_forecast(city):

    cache_key = (
        f"forecast_{city}"
    )

    cached = (
        cache.get(
            cache_key
        )
    )

    if cached:

        return cached

    url = (
        "https://api.openweathermap.org"
        "/data/2.5/forecast"
    )

    params = {

        "q": city,

        "appid":
        settings.OPENWEATHER_API_KEY,

        "units":
        "metric",

        "lang":
        "uk"

    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        data = (
            response.json()
        )

        if response.status_code != 200:

            return None

        forecast_list = (
            data["list"][::8]
        )

        result = []

        for item in forecast_list:

            result.append({

                "date":
                item["dt_txt"],

                "temp":
                item["main"]["temp"],

                "description":
                item["weather"][0]["description"],

                "icon":
                item["weather"][0]["icon"]

            })

        final = {

            "city":
            data["city"]["name"],

            "country":
            data["city"]["country"],

            "forecast":
            result

        }

        cache.set(

            cache_key,

            final,

            timeout=600

        )

        return final

    except:

        return False