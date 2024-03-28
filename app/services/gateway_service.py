from datetime import datetime
from app.repositories.gateway_repository import GatewayRepository
import matplotlib.pyplot as plt

class GatewayService:
    def __init__(self):
        self.repository = GatewayRepository()
        self.url = "https://ivt-api.azitek.io/position_logs"
        self.id = 187723572702721
        self.start_date_17 = "2023-11-17T10:00:00"
        self.end_date_17 = "2023-11-17T17:00:00"
        self.start_date_18 = "2023-11-18T10:00:00"
        self.end_date_18 = "2023-11-18T17:00:00"

    def get_shifts(self):
        start_date_timestamp_17 = int(datetime.fromisoformat(self.start_date_17).timestamp())
        end_date_timestamp_17 = int(datetime.fromisoformat(self.end_date_17).timestamp())

        start_date_timestamp_18 = int(datetime.fromisoformat(self.start_date_18).timestamp())
        end_date_timestamp_18 = int(datetime.fromisoformat(self.end_date_18).timestamp())
    
        response_timestamp_17 = self.repository.fetch_shift(self.url, self.id, start_date_timestamp_17, end_date_timestamp_17)
        response_timestamp_18 = self.repository.fetch_shift(self.url, self.id, start_date_timestamp_18, end_date_timestamp_18)

        shifts = response_timestamp_17 + response_timestamp_18

        try:
            beacon_occurrences = self._count_beacons_occurrences(shifts)
            average_times = self._get_average_time_beacon(shifts, beacon_occurrences)
            self._generate_graph(self.id, average_times)
        except ValueError as ve:
            return {"error": f"{ve}"}


    def _count_beacons_occurrences(self, shifts):
        beacon_occurrences = {}

        if len(shifts) == 0:
            raise ValueError("there's no shifts to calculate")
        
        for shift in shifts:
            if shift["beacon_id"] not in beacon_occurrences.keys():
                beacon_occurrences[shift["beacon_id"]] = 1
            else:
                beacon_occurrences[shift["beacon_id"]] += 1

        return beacon_occurrences

    def _get_average_time_beacon(self, shifts, beacon_occurrences):
        time_differences = {}
        average_times = {}
        
        for shift in shifts:
            if shift["beacon_id"] not in time_differences.keys():
                time_differences[shift["beacon_id"]] = (datetime.fromtimestamp(shift["last_seen_at"]) - datetime.fromtimestamp(shift["seen_at"])).total_seconds()
            else:
                time_differences[shift["beacon_id"]] += (datetime.fromtimestamp(shift["last_seen_at"]) - datetime.fromtimestamp(shift["seen_at"])).total_seconds()

        for beacon_id, time_difference in time_differences.items():
            if beacon_id in beacon_occurrences.keys() and beacon_occurrences[beacon_id] > 0:
                average_times[beacon_id] = time_difference / beacon_occurrences[beacon_id]
            else:
                average_times[beacon_id] = 0 
                
        return average_times

    def _generate_graph(self, gateway_id, average_times):
        average_times_list = average_times.items()

        x, y = zip(*average_times_list)

        plt.figure(figsize=(18, 6))

        plt.plot(x, y)
        plt.title(f"Average Time of Positions of the {gateway_id} Gateway")
        plt.ylabel("Average time spent positions (seconds)")
        plt.xlabel("Positions ID")

        plt.savefig('average_time_chart.png')