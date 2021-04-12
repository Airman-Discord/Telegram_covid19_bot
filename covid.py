import requests
import datetime as dt


class Covid:
    def __init__(self, country):
        self.country = country
        self.today = dt.date.today()
        self.endpoint = f"https://api.covid19api.com/country/{country}"

    def get_latest(self):
        yesterday = self.today - dt.timedelta(days=1)

        param = {
            "from": yesterday,
            "to": self.today
        }
        r = requests.get(self.endpoint, params=param)

        if  r.status_code == 404:
            return False
        return self._format_data(r.json())



    def get_by(self, start_date, end_date):
        
        param = {
            "from": start_date,
            "to": end_date
        }

        r = requests.get(self.endpoint, params=param).json()

        return self._format_data(r)



    def _format_data(self, data):
        formatted_data = {
            "country": self.country,
            "status": []
        }

        for i in data:
            formatted_data["status"].append({
                "recovered": i["Recovered"],
                "deaths": i["Deaths"],
                "confirms": i["Confirmed"],
                "active": i["Active"],
                "date": i["Date"]
            })
        return formatted_data