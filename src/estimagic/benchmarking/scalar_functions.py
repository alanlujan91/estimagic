"""Define the Scalar Benchmark Set.

This benchmark set contains 78+ test cases for single objective optimization.
The test cases are built out of 78 functions, which originate from the python
implementation of benchmark test functions for single objective optimization by
Axel Thevenot.

We use the following sources of information to construct the
benchmark set:

- https://towardsdatascience.com/optimization-eye-pleasure-78-benchmark-test-functions-for-single-objective-optimization-92e7ed1d1f12
- https://github.com/AxelThevenot/Python_Benchmark_Test_Optimization_Function_Single_Objective
"""
import numpy as np
from estimagic.benchmarking import more_wild as mw


def ackley(x):
    res = -20 * np.exp(-0.2 * np.sqrt(np.mean(x ** 2)))
    out = res - np.exp(np.mean(np.cos(2 * np.pi * x))) + 20 + np.exp(1)
    return out


def ackley2(x):
    x_1, x_2 = x
    out = -200 * np.exp(-0.2 * np.sqrt(x_1 ** 2 + x_2 ** 2))
    return out


def ackley3(x):
    x_1, x_2 = x
    res = -200 * np.exp(-0.2 * np.sqrt(x_1 ** 2 + x_2 ** 2))
    out = res + 5 * np.exp(np.cos(3 * x_1) + np.sin(3 * x_2))
    return out


def ackley4(x):
    x_1, x_2 = x
    out = np.sum(
        np.exp(-0.2) * np.sqrt(x_1 ** 2 + x_2 ** 2)
        + 3 * (np.cos(2 * x_1) + np.sin(2 * x_2))
    )
    return out


def adjiman(x):
    x_1, x_2 = x
    out = np.cos(x_1) * np.sin(x_2) - x_1 / (x_2 ** 2 + 1)
    return out


def alpine1(x):
    out = np.sum(np.abs(x * np.sin(x) + 0.1 * x))
    return out


def alpine2(x):
    out = -np.prod(np.sqrt(x) * np.sin(x))
    return out


def bartels(x):
    x_1, x_2 = x
    out = (
        np.abs(x_1 ** 2 + x_2 ** 2 + x_1 * x_2)
        + np.abs(np.sin(x_1))
        + np.abs(np.cos(x_2))
    )
    return out


def beale(x):
    x_1, x_2 = x
    out = (
        (1.5 - x_1 + x_1 * x_2) ** 2
        + (2.25 - x_1 + x_1 * x_2 ** 2) ** 2
        + (2.625 - x_1 + x_1 * x_2 ** 3) * 2
    )
    return out


def bird(x):
    x_1, x_2 = x
    res = np.sin(x_1) * np.exp((1 - np.cos(x_2)) ** 2)
    out = res + np.cos(x_2) * np.exp((1 - np.sin(x_1)) ** 2) + (x_1 - x_2) ** 2
    return out


def bohachevsky1(x):
    x_1, x_2 = x
    out = (
        x_1 ** 2
        + 2 * x_2 ** 2
        - 0.3 * np.cos(3 * np.pi * x_1)
        - 0.4 * np.cos(4 * np.pi * x_2)
        + 0.7
    )
    return out


def bohachevsky2(x):
    x_1, x_2 = x
    out = (
        x_1 ** 2
        + 2 * x_2 ** 2
        - 0.3 * np.cos(3 * np.pi * x_1) * np.cos(4 * np.pi * x_2)
        + 0.3
    )
    return out


def bohachevsky3(x):
    x_1, x_2 = x
    out = (
        x_1 ** 2
        + 2 * x_2 ** 2
        - 0.3 * np.cos(3 * np.pi * x_1 + 4 * np.pi * x_2) * np.cos(4 * np.pi * x_2)
        + 0.3
    )
    return out


def booth(x):
    x_1, x_2 = x
    out = (x_1 + 2 * x_2 - 7) ** 2 + (2 * x_1 + x_2 - 5) ** 2
    return out


def branin(x):
    x_1, x_2 = x
    res = (x_2 - 5.1 / (4 * np.pi ** 2) * x_1 ** 2 + 5 / np.pi * x_1 - 6) ** 2
    out = res + 10 * (1 - 1 / (8 * np.pi)) * np.cos(x_1) + 10
    return out


def brent(x):
    x_1, x_2 = x
    out = (x_1 + 10) ** 2 + (x_2 + 10) ** 2 + np.exp(-(x_1 ** 2) - x_2 ** 2)
    return out


def brown(x):
    x_1, x_2 = x
    out = np.sum((x_1 ** 2) ** (x_2 ** 2 + 1) + (x_2 ** 2) ** (x_1 ** 2 + 1))
    return out


def bukin6(x):
    x_1, x_2 = x
    out = 100 * np.sqrt(np.abs(x_2 - 0.01 * x_1 ** 2)) + 0.01 * np.abs(x_1 + 10)
    return out


def colville(x):
    x_1, x_2, x_3, x_4 = x
    res = 100 * (x_1 ** 2 - x_2) ** 2 + (x_1 - 1) ** 2 + (x_3 - 1) ** 2
    out = (
        res
        + 90 * (x_3 ** 2 - x_4) ** 2
        + 10.1 * ((x_2 - 1) ** 2 + (x_4 - 1) ** 2)
        + 19.8 * (x_2 - 1) * (x_4 - 1)
    )
    return out


def crossintray(x):
    x_1, x_2 = x
    out = (
        -0.0001
        * (
            np.abs(np.sin(x_1) * np.sin(x_2))
            * np.exp(np.abs(100 - np.sqrt(x_1 ** 2 + x_2 ** 2) / np.pi))
            + 1
        )
        ** 0.1
    )
    return out


def dejong5(x):
    x_1, x_2 = x
    b = [-32, -16, 0, 16, 32]
    a = np.array([[x_1, x_2] for x_1 in b for x_2 in b])
    out = (
        0.002
        + np.sum(
            [
                1 / ((i + 1) + (x_1 - a1) ** 6 + (x_2 - a2) ** 6)
                for i, (a1, a2) in enumerate(a)
            ]
        )
    ) ** -1
    return out


def rosenbrock(x):
    out = mw.rosenbrock(x) @ mw.rosenbrock(x)
    return out


SCALAR_FUNCTION_PROBLEMS = {
    "ackley_good_start": {
        "criterion": ackley,
        "start_x": np.full(10, 3),
        "solution_x": np.zeros(10),
        "start_criterion": 9.023767278119472,
        "solution_criterion": 0,
    },
    "ackley_bad_start": {
        "criterion": ackley,
        "start_x": np.full(10, 30),
        "solution_x": np.zeros(10),
        "start_criterion": 19.950424956466673,
        "solution_criterion": 0,
    },
    "ackley2_good_start": {
        "criterion": ackley2,
        "start_x": np.full(2, 3),
        "solution_x": np.zeros(2),
        "start_criterion": -85.60889823804698,
        "solution_criterion": -200,
    },
    "ackley2_bad_start": {
        "criterion": ackley2,
        "start_x": np.full(2, 25),
        "solution_x": np.zeros(2),
        "start_criterion": -0.1698651409438339,
        "solution_criterion": -200,
    },
    "ackley3_good_start": {
        "criterion": ackley3,
        "start_x": np.full(2, 3),
        # no unique solution
        "solution_x": None,
        "start_criterion": -82.57324651934985,
        "solution_criterion": -170.07756299785044,
    },
    "ackley3_bad_start": {
        "criterion": ackley3,
        "start_x": np.full(2, 25),
        # no unique solution
        "solution_x": None,
        "start_criterion": 8.358584120180984,
        "solution_criterion": -170.07756299785044,
    },
    "ackley4_good_start": {
        "criterion": ackley4,
        "start_x": np.full(2, 3),
        "solution_x": np.array([-1.51, -0.755]),
        "start_criterion": 4.5901006651507235,
        "solution_criterion": -4.5901006651507235,
    },
    "ackley4_bad_start": {
        "criterion": ackley4,
        "start_x": np.full(2, 25),
        "solution_x": np.array([-1.51, -0.755]),
        "start_criterion": 31.054276897735043,
        "solution_criterion": -4.5901006651507235,
    },
    "adjiman": {
        "criterion": adjiman,
        "start_x": np.array([-1, 1]),
        "solution_x": np.array([2, 0.10578]),
        "start_criterion": 0.954648713412841,
        "solution_criterion": -2.0218067833370204,
    },
    "alpine1_good_start": {
        "criterion": alpine1,
        "start_x": np.full(10, 2),
        "solution_x": np.zeros(10),
        "start_criterion": 20.18594853651364,
        "solution_criterion": 0,
    },
    "alpine1_bad_start": {
        "criterion": alpine1,
        "start_x": np.full(10, 10),
        "solution_x": np.zeros(10),
        "start_criterion": 44.40211108893698,
        "solution_criterion": 0,
    },
    "alpine2_good_start": {
        "criterion": alpine2,
        "start_x": np.full(10, 9),
        "solution_x": np.full(10, 7.917),
        "start_criterion": -8.345137486473694,
        "solution_criterion": -30491.15748225926,
    },
    "alpine2_bad_start": {
        "criterion": alpine2,
        "start_x": np.ones(10),
        "solution_x": np.full(10, 7.917),
        "start_criterion": -0.177988299732403,
        "solution_criterion": -30491.15748225926,
    },
    "rosenbrock_good_start": {
        "criterion": rosenbrock,
        "start_x": np.array([-1.2, 1]),
        "solution_x": np.ones(2),
        "start_criterion": 24.2,
        "solution_criterion": 0,
    },
}

SCALAR_FUNCTION_TAGS = {
    "ackley": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "ackley2": {
        "continuous": False,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "ackley3": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "ackley4": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "adjiman": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "alpine1": {
        "continuous": False,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "alpine2": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "bartels": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "beale": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "bird": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "bohachevsky1": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "bohachevsky2": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "bohachevsky3": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "booth": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "branin": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "brent": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "brown": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "bukin6": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "colville": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "crossintray": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "dejong5": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "deckkersaarts": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "dixonprice": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "dropwave": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "easom": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "eggcrate": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "eggholder": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "exponential": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "forrester": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "goldsteinprice": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "gramacylee": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "griewank": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "happycat": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "himmelblau": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "holdertable": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "keane": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "langermann": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "leon": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "levy13": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "matyas": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "mccormick": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "michalewicz": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "periodic": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "permzerodbeta": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": True,
    },
    "permdbeta": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "powell": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "qing": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "quartic": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": True,
        "parametric": False,
    },
    "rastrigin": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "ridge": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": True,
    },
    "rosenbrock": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "rotatedhyperellipsoid": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "salomon": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "schaffel1": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schaffel2": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schaffel3": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schaffel4": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schwefel": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "schwefel2_20": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schwefel2_21": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schwefel2_22": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "schwefel2_23": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "shekel": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "shubert": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "shubert3": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "shubert4": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "sphere": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "styblinskitank": {
        "continuous": True,
        "convex": False,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "sumsquares": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "thevenot": {
        "continuous": True,
        "convex": True,
        "separable": True,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": True,
    },
    "threehumps": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "trid": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "wolfe": {
        "continuous": True,
        "convex": False,
        "separable": False,
        "differentiable": True,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "xinsheyang": {
        "continuous": False,
        "convex": False,
        "separable": True,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": True,
        "parametric": False,
    },
    "xinsheyang2": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": False,
        "mutimodal": True,
        "randomized_term": False,
        "parametric": False,
    },
    "xinsheyang3": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": True,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": True,
    },
    "xinsheyang4": {
        "continuous": True,
        "convex": True,
        "separable": False,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
    "zakharov": {
        "continuous": False,
        "convex": False,
        "separable": False,
        "differentiable": False,
        "mutimodal": False,
        "randomized_term": False,
        "parametric": False,
    },
}
