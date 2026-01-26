from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot life expectancy vs income for all countries in a given year."""

    life = load("life_expectancy_years.csv")
    if life is None:
        return

    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if income is None:
        return

    year = "1900"

    life_expectancy = []
    income_data = []

    for country in life["country"]:
        if year in life.columns and year in income.columns:
            life_val = life[life["country"] == country][year].values
            income_val = income[income["country"] == country][year].values

            if len(life_val) > 0 and len(income_val) > 0:
                try:
                    life_exp = float(life_val[0])
                    inc = float(income_val[0])

                    life_expectancy.append(life_exp)
                    income_data.append(inc)
                except (ValueError, TypeError):
                    continue

    plt.scatter(income_data, life_expectancy, alpha=0.7)

    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale('log')

    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
