[![Python 3.8](https://github.com/softwaresaved/international-survey-{{year}}/actions/workflows/python-package.yml/badge.svg)](https://github.com/softwaresaved/international-survey-{{year}}/actions/workflows/python-package.yml)

# RSE International Survey {{year}}

This repository is used to analyse the RSE international survey data for the
survey conducted by the Software Sustainability Institute in {{year}}.

## Setup

To reproduce the results on your machine, first clone the repository and setup
the Python virtual environment:
```bash
git clone https://github.com/softwaresaved/international-survey-{{year}}
cd international-survey-{{year}}
python -m venv venv  # use python3 if your default python is still Python 2
source venv/bin/activate
python -m pip install -r requirements.txt
```

There is very little configuration required. The following instructions are to set
environment variables on macOS and Linux. If you are on Windows, use the documentation linked [here](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/set_1).

```bash
export RSE_SURVEY_YEAR=2018  # optional, only needed if the repository name doesn't end with year
export RSE_SURVEY_YEAR_PREV=2017  # optional, only needed if you want to override the repo setting in YEAR_PREV
export RSE_SURVEY_FIGURE_TYPE=svg  # optional, set to pdf or png to generate figures in that format
export RSE_SURVEY_FIGURE_DPI=300  # optional, set dpi for png or pdf output formats
export RSE_SURVEY_BASEURL=international-survey-zoo/  # optional, change if not the same as repo, trailing / required
```

To reproduce the results:

```bash
python run.py
```

This should create a `cache/processed_data.csv` and generate all the sections.

You can also (re-)generate the report per section. If you don't have
`cache/processed_data.csv`, then you need to initialise first (`python run.py
init`). This step is not needed when `run.py` is invoked without any parameters,
as the default invocation does the initialization. Then generate the section

```bash
python run.py <section>
```
For convenience, section names can be specified using hyphens or underscores.

Country reports should be generated _after_ the section specific reports:
```bash
python run.py country
```

* The section reports utilise the [templates](templates) corresponding to each section; the country report template is at [lib/templates/country_report.md](lib/templates/country_report.md).
  The template file uses the [Mustache](https://mustache.github.io) templating language via the [chevron](https://pypi.org/project/chevron/) module.
* Two types of reports are generated: section reports and country reports. Section reports are useful for comparing countries for a particular section of the survey,
such as demographics or job satisfaction. Country reports give an overview of a country across the different sections of the survey.
* Section reports are generated in [_section](_section)
* Country reports are generated in [_country](_country)
* Each table in the report has a corresponding CSV in [csv](csv)
* Each figure in the report has a corresponding SVG in [fig](fig)
* The source data used for the analysis is at [data](data)

## Software survey website

* We use [Jekyll](https://jekyllrb.com) and [Github Pages](https://pages.github.com) to build the website hosted at https://softwaresaved.github.io/international-survey-{{year}}.
* Stylesheets for the site are at [_sass](_sass)
* Configuration of the site is at [_config.yml](_config.yml)
* The hosted site can be viewed locally by using the command `bundle exec jekyll serve` in the docs folder and following the localhost URL. If this is the first time setting up Jekyll on your computer, ensure that you have Ruby and Bundle installed (`gem install bundler`).

## Creating a survey for the next year

- Use https://github.com/softwaresaved/international-survey-template as a template for the new repository, which should be named international-survey-YEAR
- Update the [COUNTRIES](COUNTRIES) file
- Add a YEAR_PREV file to the repository root if you want to compare to a survey year that
  is not immediately preceding the survey year.
- Create the merged data file with the present and previous survey data
  and place it at `data/public_merged.csv`
- Update section files as required in the [survey](survey) folder.
- *If* adding a new section, add it to the common library at https://github.com/softwaresaved/international-survey-lib
- You can also customize the templates for only this year by putting a .md file in a `templates` subfolder
- Set configuration (`RSE_SURVEY_*`, see above) if required
- Generate the survey report! This may give errors depending upon how much divergence there is from the previous year's survey
- You can view the report locally if you have Ruby installed, just run this: `bundle exec jekyll serve`
- Add the generated report to git: `git add _country _section data csv fig`
- Configure GitHub Pages to serve files from the main branch
- The site should be available now at https://softwaresaved.github.io/international-survey-{{year}}
- Update copyright (`footer_content:` in [_config.yml](_config.yml)), author information and steps to reproduce in the [README](README.md).
- Check licenses and attributions
- Remember to make any changes that you might need to this template repository for future years

## Composition of the survey

{{ composition }}

## Contributors

{{ contributors }}

## Licence 

This repository contains code and public data. We have different licence for each
* The code is released under [BSD 3-Clause License](LICENSE).
* The data stored in this repository is under the [CC BY 2.5 SCOTLAND](LICENSE_FOR_DATA).

The repository is also archived on zenodo: {{ doi }}
If you want to cite this work and need a citation in a specific format, you can use the citation service on the zenodo.

## Citations
> {{ citation }}

## Funders
The Software Sustainability Institute is supported by EPSRC grant EP/H043160/1 and EPSRC/ESRC/BBSRC grant EP/N006410/1, with additional project funding from Jisc and NERC. Collaboration between the universities of Edinburgh, Manchester, Oxford and Southampton.
