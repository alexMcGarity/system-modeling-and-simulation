from pylab import *
def xeq1(r):
    return sqrt(r)
def xeq2(r):
    return -sqrt(r)

domain = linspace(0, 10)
plot(domain, xeq1(domain), linewidth = 3)
plot(domain, xeq2(domain), linewidth = 3)
plot([0], [0])
axis([-10, 10, -5, 5])
xlabel("r")
ylabel("x_eq")
show()