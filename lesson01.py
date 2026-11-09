laps = [
    {"driver_number": 11, "lap_duration": 92.4},
    {"driver_number": 22, "lap_duration": 91.8},
    {"driver_number": 33, "lap_duration": None},
    {"driver_number": 44, "lap_duration": 93.2},
    {"driver_number": 55, "lap_duration": 90.7}
]

fastest_time = None
fastest_driver = None

for driver in laps:
    lap_time = driver["lap_duration"]

    # lap_time이 None이면 건너뛰기
    if lap_time is None:
        continue
    # fastest_time이 None이거나 현재 lap_time이 더 작다면
    if fastest_time is None or fastest_time > lap_time:
        # fastest_time 갱신하기
        fastest_time = lap_time
        fastest_driver = driver["driver_number"]
        
print(f"Fastest Driver: {fastest_driver}")
print(f"Fastest Lap: {fastest_time}")

