# topology-github
This repository provides supplementary material, in particular the analysis scripts for the research article *A Topology of Groups: What GitHub Can Tell Us about Online Collaboration*.

To reproduce the analyses completely one has to set up the [ghtorrent](https://ghtorrent.org/) database.  \
Gousios, G. (2013). The GHTorrent dataset and tool suite. *Proceedings of the 10th Working Conference on Mining Software*.

We worked with a dump from 2018-06-01. For the most part, the mysql database is sufficient to reproduce the analyses, but for the analysis of issue comments one also needs the mongodb database. You can download the databases [here](https://ghtorrent.org/downloads.html).

*requirements.txt* - python packages and their versions necessary to run the scripts.
Create a new python environment with pyhton 3.7 (`conda create --name env-name` or `python3 -m venv env-name` ) \
Activate environment (either `source activate env-name` or `source env-name/bin/activate`).
Then install the package list with `pip install -r requirements.txt`.


*scrape_pr_graphs_from_ghtorrent.py* - Script to read pull request data from the ghtorrent database and contruct graphs from it.

*pr*eprocessing_pull_request_graphs.ipynb* - Script to preprocess graph structures and calculate feature vectors based on structural properties of the graph.

*clustering.ipynb* - Script to find a group typology of github projects based on the structural features of pull request interaction graphs.

*analysis.ipynb* - Analysis of group types.

*collect_issue_comments_from_db.ipynb* - Script to collect issue comments from the database.

*issue_comments_preprocessing.ipynb* - Preprocessing of issue comments.

*make_nlp_plots_for_typology_paper.ipynb* - Create plots of the log-odds ratios of word frequencies in the issue comments of different project types.

*train_svm_classifier.ipynb* - Training of a support vector machine classifier to recognize graph structures from the group typology.

*analysis_projects_1yearlater.ipynb* - Analysis of group types after one year.











