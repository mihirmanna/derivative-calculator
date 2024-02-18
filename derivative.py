from enum import Enum


class FunTyp(Enum):
    POLY = 1  # a = coefficient, b = exponent
    EXP = 2  # a = coefficient, b = base
    LOG = 3  # a = coefficient, b = base
    SIN = 4  # a = coefficient
    COS = 5  # a = coefficient


class Function:
    def __init__(self, function_type: FunTyp, a: float = 0, b: float = 0, inside: list = None, inside_is_product: bool = False):
        self.type = function_type
        self.a = a
        self.b = b
        self.inside = inside
        self.inside_is_product = inside_is_product

    def __str__(self):
        to_return = ""
        
        if self.type == FunTyp.POLY:
            if self.a != 1:
                to_return += f"{self.a}"
            if self.inside is not None:
                if not self.inside_is_product:
                    to_return += f'({"+".join(list(map(lambda x: str(x), self.inside)))})'
                else:
                    to_return += f'({"*".join(list(map(lambda x: str(x), self.inside)))})'
            elif self.b == 0:
                to_return += "1"
            elif self.b > 0:
                to_return += "x"
            if self.b != 1 and self.b != 0:
                to_return += f"^{self.b}"

        elif self.type == FunTyp.EXP:
            if self.a != 1:
                to_return += f"{self.a}*"
            to_return += f"{self.b}^"
            if self.inside is not None:
                if not self.inside_is_product:
                    to_return += f'({"+".join(list(map(lambda x: str(x), self.inside)))})'
                else:
                    to_return += f'({"*".join(list(map(lambda x: str(x), self.inside)))})'
            else:
                to_return += "x"

        elif self.type == FunTyp.LOG:
            if self.a != 1:
                to_return += f"{self.a}"
            to_return += f"log_{self.b}("
            if self.inside is not None:
                if not self.inside_is_product:
                    to_return += f'{"+".join(list(map(lambda x: str(x), self.inside)))}'
                else:
                    to_return += f'{"*".join(list(map(lambda x: str(x), self.inside)))}'
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.SIN:
            if self.a != 1:
                to_return += f"{self.a}"
            to_return += "sin("
            if self.inside is not None:
                if not self.inside_is_product:
                    to_return += f'{"+".join(list(map(lambda x: str(x), self.inside)))}'
                else:
                    to_return += f'{"*".join(list(map(lambda x: str(x), self.inside)))}'
            else:
                to_return += "x"
            to_return += ")"

        elif self.type == FunTyp.COS:
            if self.a != 1:
                to_return += f"{self.a}"
            to_return += "cos("
            if self.inside is not None:
                if not self.inside_is_product:
                    to_return += f'{"+".join(list(map(lambda x: str(x), self.inside)))}'
                else:
                    to_return += f'{"*".join(list(map(lambda x: str(x), self.inside)))}'
            else:
                to_return += "x"
            to_return += ")"

        return to_return


def power_rule(fun: Function):
    fun.a *= fun.b
    fun.b -= 1


def sine_rule(fun: Function):
    fun.type = FunTyp.COS


def cosine_rule(fun: Function):
    fun.type = FunTyp.SIN
    fun.a *= -1


if __name__ == "__main__":
    pass
    