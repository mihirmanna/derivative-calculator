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
            to_return += f"{self.a}("
            if self.inside is not None:
                for func in self.inside:
                    to_return += f"{str(func)} + "
            else:
                to_return += "x"
            to_return += f")^{self.b}"

        elif self.type == FunTyp.EXP:
            to_return += f"{self.a}*{self.b}^("
            if self.inside is not None:
                for func in self.inside:
                    to_return += f"{str(func)} + "
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.LOG:
            to_return += f"{self.a}log_{self.b}("
            if self.inside is not None:
                for func in self.inside:
                    to_return += f"{str(func)} + "
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.SIN:
            to_return += f"{self.a}sin("
            if self.inside is not None:
                for func in self.inside:
                    to_return += f"{str(func)} + "
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.COS:
            to_return += f"{self.a}cos("
            if self.inside is not None:
                for func in self.inside:
                    to_return += f"{str(func)} + "
            else:
                to_return += "x"
            to_return += ")"

        return to_return


def power_rule(func: Function):
    func.a *= func.b
    func.b -= 1


if __name__ == "__main__":
    pass
    