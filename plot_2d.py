import matplotlib.pyplot as plt

def plot_pressure(df):
    plt.plot(df["depth"], df["pressure"])
    plt.xlabel("Depth")
    plt.ylabel("Pressure")
    plt.title("Pressure vs Depth")
    plt.gca().invert_xaxis()
    plt.show()