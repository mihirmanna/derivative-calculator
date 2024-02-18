from enum import Enum


class FunTyp(Enum):
    POLY = 1  # a = coefficient, b = exponent
    EXP = 2  # a = coefficient, b = base
    LOG = 3  # a = coefficient, b = base
    SIN = 4  # a = coefficient
    COS = 5  # a = coefficient


class Function:
    def __init__(self, function_type: FunTyp, a: float, b: float = 0, inside: list = None):
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
            else:
                to_return += "x"
            if not self.b == 1:
                to_return += f"^{self.b}"

        elif self.type == FunTyp.EXP:
            if not self.a == 1:
                to_return += f"{self.a}*"
            to_return += f"{self.b}^"
            if self.inside is not None:
                to_return += f'({"+".join(list(map(lambda x: str(x), self.inside)))})'
            else:
                to_return += "x"

        elif self.type == FunTyp.LOG:
            if not self.a == 1:
                to_return += f"{self.a}"
            to_return += f"log_{self.b}("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.SIN:
            if not self.a == 1:
                to_return += f"{self.a}"
            to_return += "sin("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.COS:
            if not self.a == 1:
                to_return += f"{self.a}"
            to_return += "cos("
            if self.inside is not None:
                to_return += "+".join(list(map(lambda x: str(x), self.inside)))
            else:
                to_return += "x"
            to_return += ")"

        return to_return


def power_rule(func: Function):
    func.a *= func.b
    func.b -= 1


if __name__ == "__main__":
    pass
    