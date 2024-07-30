from screen import Screen


class LongBreakMenu(Screen):

    def start_loop(self) -> None:
        while True:
            self.clear()
            self.print_screen()
            key: bytes = self.wait_for_input()
            match key:
                case b'1':
                    self.change_screen("long_break_screen")
                case b'2':
                    self.change_screen("menu")
                case b'3':
                    self.exit()
                case _:
                    continue

    def print_screen(self) -> None:
        print("START LONG BREAK \n\n " +

              "__20 minutes__ \n\n " +

              "Options: \n " +
              "- (1) Start \n " +
              "- (2) Cancel \n " +
              "- (3) Quit ")
