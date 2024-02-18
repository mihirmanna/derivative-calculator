from enum import Enum


class FunTyp(Enum):
    POLY = 1  # a = coefficient, b = exponent
    EXP = 2  # a = base
    LOG = 3  # a = base
    SIN = 4
    COS = 5


class Function:
    def __init__(self, function_type: FunTyp, a: float = 0, b: float = 0, inside: list = None):
        self.type = function_type
        self.a = a
        self.b = b
        self.inside = inside

    def __str__(self):
        to_return = ""
        
        if self.type == FunTyp.POLY:
            if not self.a == 1:
                to_return += f"{self.a}"
            if self.inside is not None:
                to_return += f'({"+".join(list(map(lambda x: str(x), self.inside)))})'
            elif self.b == 0:
                to_return += "1"
            elif self.b > 0:
                to_return += "x"
            if not self.b == 1 and not self.b == 0:
                to_return += f"^{self.b}"

        elif self.type == FunTyp.EXP:
            to_return += f"{self.a}^"
            if self.inside is not None:
                to_return += f'({"+".join(list(map(lambda x: str(x), self.inside)))})'
            else:
                to_return += "x"

        elif self.type == FunTyp.LOG:
            to_return += f"log_{self.a}("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.SIN:
            to_return += "sin("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.COS:
            to_return += "cos("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        return to_return


if __name__ == "__main__":
    pass
    