%pylab inline

a = randn(40)

# define astats
def astats(arr):
    print('min, max, mean = %f, %f, %f' % (min(arr), max(arr), mean(arr)))

astats(a)
