from screen import Screen


class Menu(Screen):

    def start_loop(self) -> None:
        while True:
            self.clear()
            self.print_screen()
            key: bytes = self.wait_for_input()
            match key:
                case b'1':
                    self.change_screen("pomodoro_menu")
                case b'2':
                    self.change_screen("short_break_menu")
                case b'3':
                    self.change_screen("long_break_menu")
                case b'4':
                    self.exit()
                case _:
                    continue

    def print_screen(self) -> None:
        print("POMODORO TIMER \n" +
              "Use __Your Time__ more effectivly! \n" +
              "Options: \n" +
              "- (1) Start new Pomodoro (25 min) \n" +
              "- (2) Start short break (5 min) \n" +
              "- (3) Start long break (20 min) \n" +
              "- (4) Quit -> Quit \n")
