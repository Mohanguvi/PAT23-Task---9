# fibonacci series 
f = lambda x: x if x<=1 else f(x-1) + f(x-2)

# get the range of the fibonacci series
for i in range(1, 50):
    print(f(i)) # Display the results
