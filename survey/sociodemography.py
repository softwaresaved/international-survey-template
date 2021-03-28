# Sociodemography
import sys
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.analysis import count_diff, plot_cat_comparison
from lib.report import (
    slugify,
    make_report,
    read_cache,
    table_country,
    figure_country,
    COUNTRIES_WITH_WORLD,
)

age = ["socio3. Please select your age"]

age_order = [
    "18 to 24 years",
    "25 to 34 years",
    "35 to 44 years",
    "45 to 54 years",
    "55 to 64 years",
    "Age 65 or older",
    "Prefer not to say",
]

gender = ["socio2. Please select your gender"]

ethn_us = ["socio5us. Do you consider yourself Hispanic or Latino"]

disability = [
    "disa1. Do you have a condition that is defined as a disability by your country?"
]


@make_report(__file__)
def run(survey_year, data="data/public_merged.csv"):
    df = read_cache("processed_data")
    ethnicity = [x for x in df.columns if x[:7] == "socio5."]
    countries = []
    for country in COUNTRIES_WITH_WORLD:
        print(country)
        countries.append({"country": country})
        for category, columns, order_index in [
            ("Age", age, age_order),
            ("Gender", gender, False),
        ]:
            results = count_diff(
                df, columns, country, category, survey_year, order_index=order_index
            )
            countries[-1].update(table_country(country, slugify(category), results))
            plot_cat_comparison(
                results, country=country, category=category, order_index=order_index
            )
            countries[-1].update(figure_country(country, slugify(category), plt))
        if country in ["United Kingdom", "United States"]:
            ethnicity_data = count_diff(
                df, ethnicity, country, category, survey_year, multi_choice=True
            )
            countries[-1].update(table_country(country, "ethnicity", ethnicity_data))
            plot_cat_comparison(results, country=country, category=category)
            countries[-1].update(figure_country(country, "ethnicity", plt))
        if country == "United Kingdom":
            disability_data = count_diff(
                df,
                disability,
                country,
                "Officially recognised disability",
                survey_year,
                y_n=True,
            )
            plot_cat_comparison(disability_data, country=country, category=category)
            countries[-1].update(figure_country(country, "disability", plt))
        if country == "United States":
            hispanic_latino_data = count_diff(
                df, ethn_us, country, category, survey_year, y_n=True
            )
            countries[-1].update(
                table_country(country, "hispanic-or-latino", hispanic_latino_data)
            )
            plot_cat_comparison(
                hispanic_latino_data, country=country, category=category
            )
            countries[-1].update(figure_country(country, "hispanic-or-latino", plt))
    return {"countries": countries}


if __name__ == "__main__":
    run()
