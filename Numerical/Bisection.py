import pandas as pd

def bisection (f, x0, x1, e):
    step = 1
    condition = True
    df = pd.DataFrame(data={'x': [x0], 'f(x)': [f(x0)]})
    while condition:
        x2 = (x0 + x1 )/2
        print(f'Step: {step}, x2 = {x2: 0.16f} and f(x2) = {f(x2):0.16f}')

        if f(x0)*f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        df.loc[step] = {'x': x0, 'f(x)': f(x0)}
        step = step +1
        condition = abs(f(x2)) > 0
    
    print(f'\nRequired Root is: {x2: 0.16f}')
    return df

if __name__ == "__main__":
    import math

    def f(x): return math.cos(x) - x
    df = bisection(f=f, x0=0, x1=math.pi / 4, e=1.0e-16)
    print(df.style.format({'x': '{:.16f}', 'f(x)': '{:.16f}'}).to_latex())