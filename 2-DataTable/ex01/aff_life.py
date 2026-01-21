from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        return
    
    country = "Switzerland"
    country_data = df[df["country"] == country]
    years = country_data.columns[1:]
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel("Life Expectancy")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
