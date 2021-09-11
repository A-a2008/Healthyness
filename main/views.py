from django.shortcuts import render, redirect
import requests
import pandas as pd
from django.apps import apps

pd.options.plotting.backend = "plotly"
Yoga = apps.get_model("main", "Yoga")


def home(request):
    return render(request, "index.html")


class COVIDTrackerModel:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
        self.r = requests.get(self.url)
        self.data = None
        self.columns = []

    def covid_tracker(self, request):
        if request.method == "POST":
            country = request.POST["country"]
            fig = self.data.plot(y=f"{country}", template="plotly_white", title=f"Cases for <b>{country}</b>",
                                 labels=dict(index="Date", value="Cases", variable="Country"))
            fig = fig.to_html(full_html=False, default_width=1000, default_height=700)
            data = {
                "countries": self.columns,
                "selected": True,
                "country_selected": country,
                "plot": fig,
            }

            return render(request, "covid/covid.html", data)
        else:
            with open("main/country_data.csv", "wb") as file:
                file.write(self.r.content)
            data = pd.read_csv("main/country_data.csv")
            data = data.groupby("Country/Region").sum()
            data = data.drop(columns=["Lat", "Long"])
            data_transposed = data.T
            self.data = data_transposed
            columns_raw = data_transposed.columns
            for column in columns_raw:
                self.columns.append(column)

            data = {
                "countries": self.columns,
            }
            return render(request, "covid/covid.html", data)


class SugarCalculatorModel:
    def __init__(self):
        pass

    def sugar(self, request):
        if request.method == "POST":
            cereal = int(request.POST["cereal"])
            cola = int(request.POST["cola"])
            milkshake = int(request.POST["milkshake"])
            juice = int(request.POST["juice"])
            cake_bar = int(request.POST["cake_bar"])
            biscuit = int(request.POST["biscuit"])
            sweets = int(request.POST["sweets"])
            pudding = int(request.POST["pudding"])
            chocolate = int(request.POST["chocolate"])

            total_cubes = 0
            total_cubes += cereal * 3
            total_cubes += cola * 9
            total_cubes += milkshake * 10
            total_cubes += juice * 2
            total_cubes += cake_bar * 3
            total_cubes += biscuit * 1
            total_cubes += sweets * 4
            total_cubes += pudding * 5
            total_cubes += chocolate * 4

            message = ""
            if total_cubes > 7:
                message = "Oops, you have eaten a lot today, please stop eating more sugar of please reduce it"
            elif total_cubes > 40:
                message = "You should be consulting a doctor right now if you eat so much for a day"
            else:
                message = "You are perfectly fine and you meet the regular standards"

            total_grams = round(total_cubes * 2.3, 2)
            total_calories = round(total_cubes * 8.9, 3)

            data = {
                "cubes": total_cubes,
                "message": message,
                "grams": total_grams,
                "calories": total_calories
            }

            return render(request, "sugar/sugar.html", data)
        else:
            return render(request, "sugar/sugar.html")


class YogaModel:
    def __init__(self):
        pass

    def yoga(self, request):
        if request.method == "POST":
            if request.user.is_authenticated:
                exercises_list = request.POST.getlist("exercises")
                points = {
                    "mountain": 5,
                    "chair": 10,
                    "down_dog": 8,
                    "downward_dog": 10,
                    "triangle": 12,
                    "tree": 14,
                    "bridge": 10,
                    "bound_ankle": 6,
                    "seated_forward": 16,
                    "corpse": 5
                }
                total_points = 0
                for exercise in exercises_list:
                    total_points += points.get(exercise)
                user_yoga = Yoga.objects.filter(user=request.user)
                try:
                    print(user_yoga[0])
                    user_yoga.update(points=total_points)
                except IndexError:
                    Yoga.objects.create(
                        user=request.user
                    )
                    user_yoga.update(points=total_points)
                print(total_points)
                data = {
                    "highest_points": Yoga.objects.order_by("points")[:6]
                }
                return render(request, "yoga/yoga.html", data)
            else:
                return render(request, "error/error.html")
        else:
            data = {
                "highest_points": Yoga.objects.order_by("points")[:6]
            }
            return render(request, "yoga/yoga.html", data)


class InnerMind:
    def __init__(self):
        pass

    def inner_mind(self, request):
        return render(request, "inner_mind/inner_mind.html")

    def done(self, request):
        return render(request, "inner_mind/done.html")

    def stop(self, request):
        data = {
            "time": "00:00"
        }
        return render(request, "inner_mind/inner_mind.html", data)
