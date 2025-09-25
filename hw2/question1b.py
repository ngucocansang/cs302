def fib_fast_doubling(n: int) -> int:
    """Compute the nth Fibonacci number using the fast doubling method."""
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    
    def _fd(k:int):
        if k ==0:
            return (1, 1)
        (a,b) = _fd(k >>1)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k & 1:
            return (d, c + d)
        else:
            return (c, d)
        
    return _fd(n)[0]

if __name__ == "__main__":
    for n in [0,1,2,3,4,5,10,20,30,40,50]:
        print(f"F({n}) = {fib_fast_doubling(n)}")