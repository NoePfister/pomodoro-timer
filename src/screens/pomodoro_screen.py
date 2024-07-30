from screen import Screen


class PomodoroScreen(Screen):

    def start_loop(self) -> None:
        while True:
            self.clear()
            self.print_menu()
            key: bytes = self.wait_for_input()
            match key:
                case _:
                    continue

    def print_menu(self) -> None:
        print("")
