import time

from const import Colors
from screen import Screen


class ShortBreakScreen(Screen):

    def __init__(self, program) -> None:
        super().__init__(program)
        self.DURATION: int = 5 * 1  # 5 minutes in seconds
        self.start_time: int = 0
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
                        self.change_screen("short_break_menu")
                    case b'3':
                        self.exit()
                    case _:
                        continue
            else:
                self.update_remaining()
                time.sleep(1)

    def update_remaining(self) -> None:
        self.remaining = self.start_time + self.DURATION - int(time.time())

    def print_screen(self) -> None:
        print("SHORT BREAK \n" +
              f"{Colors.BOLD}Remaining Time:{Colors.NORMAL} \n" +
              f"{self.format_time(self.remaining)} \n" +
              "Options: \n" +
              "- (1) Cancel \n" +
              "- (2) Restart \n" +
              "- (3) Quit"
              )
