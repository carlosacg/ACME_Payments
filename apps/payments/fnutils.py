from apps.payments.models import Day, Schedule, Rate
from datetime import datetime

def process_file(file) -> list:
    content = file.read().decode("utf-8")
    return content

def get_amount_to_pay(content: str) -> str:
    """
    This function receives a string containing the name and the range of hours 
    in days in which an employee worked and returns a message indicating the amount of money 
    to be paid to the employee and returns a message indicating the amount of money to be paid.
    """
    name, schedules = content.split("=")
    amount_to_pay = calculate_amount_to_pay(schedules)
    message = f"The amount to pay {name} is: {amount_to_pay} USD"
    return message


def calculate_amount_to_pay(schedules: str) -> float:
    """
    This function returns the amount to pay for an employee (float)
    given the schedules in which the employee works in a string format.
    """
    schedules_list = schedules.split(",")
    amount_to_pay = 0
    for schedule in schedules_list:
        day_obj = Day.objects.filter(code=schedule[:2]).first()
        schedule_obj, quantity_hours = get_schedule_and_hours(schedule[2:])
        rate_obj = Rate.objects.filter(
            day=day_obj, schedule=schedule_obj).first()
        amount_to_pay += rate_obj.price_by_hour * quantity_hours
    return amount_to_pay


def get_schedule_and_hours(range_time: str):
    """
    This function returns a Schedule object and working hours (float) 
    given a range of time in a string format.
    """
    time_format = "%H:%M"
    start_time, end_time = range_time.split("-")
    if end_time == "00:00":
        end_time = "23:59"
    start_time = datetime.strptime(start_time, time_format)
    end_time = datetime.strptime(end_time, time_format)
    working_hours = end_time - start_time
    working_hours = round(working_hours.total_seconds()/(60*60))
    schedule_obj = Schedule.objects.filter(
        start_time__lte=start_time.time(), end_time__gte=end_time.time()).first()
    return schedule_obj, working_hours
