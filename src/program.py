from screen import Screen
from screens.long_break_menu import LongBreakMenu
from screens.long_break_screen import LongBreakScreen
from screens.menu import Menu
from screens.pomodoro_menu import PomodoroMenu
from screens.pomodoro_screen import PomodoroScreen
from screens.short_break_menu import ShortBreakMenu
from screens.short_break_screen import ShortBreakScreen


class Program:
    def __init__(self) -> None:
        self.screens: dict[str, Screen] = {
            "menu": Menu(self),
            "pomodoro_menu": PomodoroMenu(self),
            "short_break_menu": ShortBreakMenu(self),
            "long_break_menu": LongBreakMenu(self),
            "pomodoro_screen": PomodoroScreen(self),
            "short_break_screen": ShortBreakScreen(self),
            "long_break_screen": LongBreakScreen(self),
        }

    def start_program(self) -> None:
        self.screens["menu"].start_loop()
