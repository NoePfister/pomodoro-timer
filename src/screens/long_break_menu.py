from screen import Screen


class LongBreakMenu(Screen):

    def start_loop(self) -> None:
        while True:
            self.clear()
            self.print_screen()
            key: bytes = self.wait_for_input()
            match key:
                case _:
                    continue

    def print_screen(self) -> None:
        print("")
