import pandas as pd
import os

df = pd.read_csv("arrivals.csv")

df["Minutes_Delayed"] = df["Minutes_Delayed"].fillna(0)

class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time

    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print(f"Warning: Flight {self.flight_num} is moderately delayed.")
        elif self.delay_time > 60:
            print(f"Severe Warning: Flight {self.flight_num} is heavily delayed!")

delayed_df = df[df["Minutes_Delayed"] > 30]

most_delayed = delayed_df.loc[delayed_df["Minutes_Delayed"].idxmax()]

flight = Flight(most_delayed["Flight_Number"], most_delayed["Minutes_Delayed"])
flight.check_severity()

new_entry = pd.DataFrame([{
    "Flight_Number": most_delayed["Flight_Number"],
    "Airline": most_delayed["Airline"],
    "Minutes_Delayed": most_delayed["Minutes_Delayed"]
}])

file_name = "severe_delays_log.csv"

if os.path.exists(file_name):
    log_df = pd.read_csv(file_name)
    log_df = pd.concat([log_df, new_entry], ignore_index=True)
else:
    log_df = new_entry

log_df.to_csv(file_name, index=False)

print("Log updated successfully!")