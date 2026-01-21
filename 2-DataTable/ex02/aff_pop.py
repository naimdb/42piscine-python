from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("population_total.csv")
    if df is None:
        return
    
    campus = "Switzerland"
    target = "France"

    campus_data = df[df["country"] == campus]
    target_data = df[df["country"] == target]

    years = campus_data.columns[1:]
    
    population = campus_data.values[0][1:]
    target_population = target_data.values[0][1:]

    plt.plot(years, population)
    plt.plot(years, target_population)
    plt.title(f"Population Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel("Population")
    plt.tight_layout()
    plt.legend([campus, target])
    plt.show()


if __name__ == "__main__":
    main()
