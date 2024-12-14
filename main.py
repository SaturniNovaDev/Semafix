# [!] PyLight script. Base code written by Peter Vega, around 21% by AI.
"""
This code basically gets random values that represent a lane\'s
vehicles and how much time they\'ve waited.

The code then evaluates each lane\'s wait time and determines
which lane needs green light more urgently.

 -- Written by Peter Vega. Modified and enhanced with Blackbox AI.
"""


# Imports:
import time, pysercom as psc, random as rd


# Define class 'Lane':
class Lane:
    """Stores `cars` and has a `wait time`, used to determine priority across drivers."""

    def __init__(self, cars_amount, wait_time, lane_number):
        self.cars_amount = cars_amount  # Amount of cars
        self.wait_time = wait_time  # Wait time to determine green light
        self.lane_number = lane_number  # Attribute to identify the lane
        self.green_light = False  # Attribute to indicate green light


# Define 'give_priority()':
def give_priority(lane, time_for):
    """Gives priority to a specific `lane` for a specific `time` in seconds."""

    # Code
    lane.green_light = True
    print(f"Lane number {lane.lane_number} has priority for {time_for} seconds.")
    time.sleep(time_for)  # Wait for the specified time
    lane.green_light = False
    lane.cars_amount = 0
    print(f"Lane number {lane.lane_number} has finished its priority time.")


# Define 'control_traffic()':
def control_traffic(lane1, lane2, time_for):
    """Controls traffic by giving priority to the `lane` with more `cars` or longer `wait time`."""

    # Print header:
    print(f"{'Lane':<15} | {'Cars amount':<20} | {'Wait time (s)':<20}")
    print(f"{'-'*15} | {'-'*20} | {'-'*20}")

    while lane1.cars_amount > 0 or lane2.cars_amount > 0:
        # Print lane status:
        print(
            f"{lane1.lane_number:<15} | {lane1.cars_amount:<20} | {lane1.wait_time:<20}"
        )
        print(
            f"{lane2.lane_number:<15} | {lane2.cars_amount:<20} | {lane2.wait_time:<20}"
        )

        if lane1.wait_time > lane2.wait_time:
            give_priority(lane1, time_for)
            lane2.wait_time += time_for
            lane1.cars_amount = rd.randint(0, 15)
            lane1.wait_time = rd.randint(1, 35)
        elif lane1.wait_time < lane2.wait_time:
            give_priority(lane2, time_for)
            lane1.wait_time += time_for
            lane2.cars_amount = rd.randint(0, 15)
            lane2.wait_time = rd.randint(1, 35)

    print("Both lanes are empty. Exiting the traffic control system...")
    time.sleep(2.5)
    print("Traffic control system has been terminated.")


# Test --------------------------------------------------------------------------------------------
laneA = Lane(12, 15, 1)
laneB = Lane(4, 35, 2)
control_traffic(laneA, laneB, 15)
# Traffic values will eventually change due to the `control_traffic` function.
