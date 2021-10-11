package leetcode

func fib(n int, cache map[int]int) int {
    
	if n < 1 {
		return n
	}

	value, ok := cache[n]
	if ok {
		return value
	}

	cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
	return cache[n]
	
}