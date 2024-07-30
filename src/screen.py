import msvcrt
import sys

import utils


class Screen:
    def __init__(self, program) -> None:
        from program import Program
        self.program: Program = program

    def start_loop(self) -> None:
        pass

    def print_screen(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def change_screen(self, screen: str) -> None:
        self.reset()
        self.program.screens[screen].start_loop()

    @staticmethod
    def clear() -> None:
        utils.clear()

    def exit(self) -> None:
        self.clear()
        print("EXITING")
        sys.exit()

    @staticmethod
    def wait_for_input() -> bytes:
        """Wait for key input and return it."""
        return msvcrt.getch()


    @staticmethod
    def check_input() -> bool:
        return msvcrt.kbhit()

    @staticmethod
    def format_time(seconds: int) -> str:
        return utils.format_time(seconds)
