import msvcrt

from const import Colors
from screen import Screen
import time


class PomodoroScreen(Screen):

    def __init__(self, program) -> None:
        super().__init__(program)
        self.start_time: int = 0
        self.DURATION: int = 25 * 1  # 25 minutes in seconds
        self.remaining: int = 0

    def start_loop(self) -> None:
        self.start_time = int(time.time())
        self.update_remaining()
        while True:
            # Check if time is up
            if self.start_time + self.DURATION < int(time.time()):
                self.change_screen("menu")

            self.clear()
            self.print_screen()
            if self.check_input():
                key: bytes = self.wait_for_input()
                match key:
                    case b'1':
                        self.change_screen("menu")
                    case b'2':
                        self.change_screen("pomodoro_menu")
                    case b'3':
                        self.exit()
                    case _:
                        continue
            else:
                self.update_remaining()
                time.sleep(1)

    def reset(self) -> None:
        self.remaining = 0
        self.start_time = 0

    def update_remaining(self) -> None:
        self.remaining = self.start_time + self.DURATION - int(time.time())

    def print_screen(self) -> None:
        print(f"POMODORO \n " +
              f'{Colors.BOLD}Remaining Time:{Colors.NORMAL} \n ' +
              f" {self.format_time(self.remaining)}\n " +
              f"Options: \n" +
              f"- (1) Cancel \n" +
              f"- (2) Restart \n" +
              f"- (3) Quit"
              )
