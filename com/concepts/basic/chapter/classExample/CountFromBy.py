class CountFromBy:
    class_Variable = 100

    def __init__(self, v: int) -> None:
        self.val = v

    def increase(self) -> None:
        self.val += self.class_Variable

    def __repr__(self) -> str:
        return str(self.val)