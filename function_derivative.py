from enum import Enum
import copy


class FuncType(Enum):
    POLY = 1
    TRIG = 2


class Function:
    def __init__(self, coeff: float, exp: float, func_type: FuncType, inside=None):
        self.coeff = coeff
        self.exp = exp
        self.inside = inside
        self.type = func_type
        if self.type == FuncType.TRIG:
            self.trig_vec = [1, 1]  # sin() exp, cos() exp
    
    def __str__(self):
        if self.coeff == 0:
            return "0"
        
        if self.type == FuncType.POLY:
            if self.inside is not None:
                return f"{self.coeff}({str(self.inside)})^{self.exp}"
            else:
                return f"{self.coeff}x^{self.exp}"
            
        if self.type == FuncType.TRIG:
            result = f"{self.coeff}("
            if not self.trig_vec[0] == 0:  # cos() is non-vanishing
                result += f"cos^{self.trig_vec[0]}"
                if self.inside is not None:
                    result += f"({str(self.inside)})"
            if not self.trig_vec[1] == 0:  # sin() is non-vanishing
                result += f"sin^{self.trig_vec[1]}"
                if self.inside is not None:
                    result += f"({str(self.inside)})"
            result += f")^{self.exp}"
            return result


def power_rule(func: Function):
    func.coeff *= func.exp
    func.exp -= 1
    

def take_derivative(func: Function):
    result = [func]
    
    if func.type == FuncType.POLY:
        power_rule(func)
    if func.inside is not None:
        result.append(take_derivative(copy.deepcopy(func).inside)[0])
        
    return result


if __name__ == "__main__":
    func1 = Function(2, 3, FuncType.POLY)
    func2 = Function(4, 11, FuncType.POLY, inside=func1)
    func3 = Function(0, 1, FuncType.TRIG, inside=func1)
    
    print(f"Function 1: {func1}")
    print(f"Function 2: {func2}")
    print(f"Function 3: {func3}")
    
    deriv1 = take_derivative(copy.deepcopy(func1))
    deriv2 = take_derivative(copy.deepcopy(func2))
    
    print(f"Derivative 1: ({deriv1[0]})")
    print(f"Derivative 2: ({deriv2[0]}) * ({deriv2[1]})")
