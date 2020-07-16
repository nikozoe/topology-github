# topology-github
This repository provides supplementary material, in particular the analysis scripts for the research article *A Topology of Groups: What GitHub Can Tell Us about Online Collaboration*.

To reproduce the analyses completely one has to set up the [ghtorrent](https://ghtorrent.org/) database. 
Gousios, G. (2013). The GHTorrent dataset and tool suite. *Proceedings of the 10th Working Conference on Mining Software*.

We worked with a dump from 2018-06-01. For the most part, the mysql database is sufficient to reproduce the analyses, but for the analysis of issue comments one also needs the mongodb database. You can download the databases [here](https://ghtorrent.org/downloads.html).
