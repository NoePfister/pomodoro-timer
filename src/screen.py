import msvcrt

import utils



class Screen:
    def __init__(self, program) -> None:
        from program import Program
        self.program: Program = program
    
    
    def start_loop(self) -> None:
        pass
    
    
    def print_menu(self) -> None:
        pass
    
    def reset(self) -> None:
        pass
    
    @staticmethod
    def clear() -> None:
        utils.clear()
    
    
    @staticmethod
    def wait_for_input() -> bytes:
        """Wait for key input and return it."""
        return msvcrt.getch()