import os

def clear() -> None:
    os.system("cls")


def format_time(seconds: int) -> str:
    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Create a formatted string
    time_str = f"{hours}:{minutes}:{seconds}"

    return time_str