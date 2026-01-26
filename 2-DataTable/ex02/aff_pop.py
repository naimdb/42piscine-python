from load_csv import load
import matplotlib.pyplot as plt


def parse_pop(value):
    """Convert population string (e.g., '1.75M') to float in millions."""
    if 'M' in value:
        return float(value.replace('M', ''))
    elif 'k' in value:
        return float(value.replace('k', '')) / 1000
    else:
        return float(value) / 1e6


def main():
    """Plot population projections for two countries."""

    df = load("population_total.csv")
    if df is None:
        return

    campus = "Switzerland"
    target = "France"

    campus_data = df[df["country"] == campus]
    target_data = df[df["country"] == target]

    years = campus_data.columns[1:]
    years = [int(year) for year in years]

    population = [parse_pop(x) for x in campus_data.values[0][1:]]
    target_population = [parse_pop(x) for x in target_data.values[0][1:]]

    limit_index = years.index(2050)
    years = years[:limit_index]
    population = population[:limit_index]
    target_population = target_population[:limit_index]

    plt.plot(years, population, label=campus)
    plt.plot(years, target_population, label=target)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    
    plt.xticks(years[::40])
    
    y_max_value = max(max(target_population), max(population))
    y_max = int((y_max_value // 20 + 1) * 20)
    y_ticks = range(0, y_max + 20, 20)
    plt.yticks(y_ticks, [f'{y}M' for y in y_ticks])

    plt.tight_layout()
    plt.legend([campus, target])
    plt.show()


if __name__ == "__main__":
    main()