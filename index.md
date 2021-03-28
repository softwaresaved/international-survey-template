---
layout: home
title: Home
---
# RSE International Survey

The Research Software Engineering (RSE) International Survey is a survey conducted
by the [Software Sustainability Institute](https://www.software.ac.uk) that comprises 8 countries
and covers all aspects of the practice of research software engineering.

We ran the **first survey in 2016**, which provided an insight into the
demographics, job satisfaction, and practices of research software engineers
(RSEs). To support and broaden this work, the institute will conduct the survey
at regular intervals, and extend the geographical coverage, which will
facilitate inter-country comparison. The results of the surveys, the anonymised
version of which is under a open license, will act as a a valuable resource to
understand and improve the working conditions for RSEs.

In **2017** we also surveyed Canadian RSEs and we added four further countries,
Germany, Netherlands, South Africa and USA. Our thanks to our partners: Scott
Henwood (Canada), Stephan Janosch and Martin Hammitzsch (Germany), Ben van
Werkhoven and Tom Bakker (Netherlands), Anelda van der Walt (South Africa) and
Daniel Katz and Sandra Gesing (USA).

In **2018** we have worked differently and created a survey for all countries
(rather than one survey for each one).

This site covers the **{{year}}** survey.

## Composition of the survey

The [base questions](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/{{year}}/questions.csv) for the survey were tailored to meet the requirements of each country. They covered ten subjects:
   1. **Demographics**: traditional social and economic questions, such as gender, age, salary and education.
   1. **Coding**: how much code do RSEs write, how often, and for whom.
   1. **Employment**: questions about where RSEs work and in which disciplines.
   1. **Current contract**: understanding stability of employment by questioning the type of employment contract RSEs receive.
   1. **Previous employment**: understanding routes into the profession the reasons for choosing it.
   1. **Collaboration and training**: who RSEs work with, how many people they work with, and the training they conduct.
   1. **Publications**: do RSEs contribute to publications and are they acknowledged?
   1. **Sustainability and tools**: testing, bus factor, technical handover. Also which tools they are using
   1. **Job satisfaction**: what do RSEs think about their job and their career?
   1. **Network**: how do RSEs meet and gain representation?
These subjects are not necessarily  investigated under this order, neither published with that order. 

## Contributors

Here is a list of contributors for the {{year}} version of the survey (alphabetic order). They are also mentioned in the [.zenodo.json](https://github.com/softwaresaved/international-survey/blob/master/.zenodo.json) to be automatically added to the DOI.

{{ contributors }}

## Licence 

This repository contains code and public data. We have different licence for each
* The code is released under [BSD 3-Clause License](https://github.com/softwaresaved/international-survey-{{year}}/blob/main/LICENSE).
* The data stored in this repository is under the [CC BY 2.5 SCOTLAND](https://github.com/softwaresaved/international-survey-{{year}}/blob/main/LICENSE_FOR_DATA).

The repository is also archived on zenodo: {{doi}}
If you want to cite this work and need a citation in a specific format, you can use the citation service on the zenodo.

## Reproducibility

To reproduce the results on your machine, first clone the repository and setup
the Python virtual environment:
```bash
git clone https://github.com/softwaresaved/international-survey-{{year}}
cd international-survey-{{year}}
python -m venv venv  # use python3 if your default python is still Python 2
source venv/bin/activate
python -m pip install -r requirements.txt
```


To reproduce the results:

```bash
python run.py
```

This should create a `cache/processed_data.csv` and generate all the sections.

To generate the country reports (only _after_ generating the section reports):
```bash
python run.py country
```

## Citations
The citation for the {{year}} version is:
> {{Authors}}. ({{cite-year}}, {{cite-month}} {{cite-day}}). softwaresaved/international-survey-{{year}}: Public release for {{year}} results (Version {{version). Zenodo. {{doi}}

## Funders
The Software Sustainability Institute is supported by EPSRC grant EP/H043160/1 and EPSRC/ESRC/BBSRC grant EP/N006410/1, with additional project funding from Jisc and NERC. Collaboration between the universities of Edinburgh, Manchester, Oxford and Southampton.
