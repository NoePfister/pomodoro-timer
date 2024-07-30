import sys

from screen import Screen


class Menu(Screen):

    def start_loop(self) -> None:
        while True:
            self.clear()
            self.print_menu()
            key: bytes = self.wait_for_input()
            match key:
                case '1':
                    self.program.screens["pomodoro_menu"].start_loop()
                case '2':
                    self.program.screens["short_break_menu"].start_loop()
                case '3':
                    self.program.screens["long_break_menu"].start_loop()
                case '4':
                    sys.exit()
                case _:
                    continue

    def print_menu(self) -> None:
        print("POMODORO TIMER \n" +
              "Use __Your Time__ more effectivly! \n" +
              "Options: \n" +
              "- (1) Start new Pomodoro (25 min) \n" +
              "- (2) Start short break (5 min) \n" +
              "- (3) Start long break (20 min) \n" +
              "- (4) Quit -> Quit \n")
