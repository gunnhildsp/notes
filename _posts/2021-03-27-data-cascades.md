---
title: "Data excellence as a first-class citizen of AI"
description: "Data quality issues are prevalent and invisible, but avoidable if we design for and incentivize data excellence."
layout: post
toc: true
categories: [data-quality]
---
A recent blog post from Vicki Boykis drew me in as it revolves around the topic of implicit knowledge: [The ghosts in the data](https://veekaybee.github.io/2021/03/26/data-ghosts/). Implicit knowledge hits us from many differents perspectives nowadays, from automating implicit knowledge through AI, discovering and sharing implicit knowledge in distributed or hybrid workplaces, when enabling beginner coders to develop and maintain applications, and when documenting everything from software applications to model experiments. As all pythonistas know: [Explicit is better than implicit](https://www.python.org/dev/peps/pep-0020/). 

The blog post pointed me to the paper [“Everyone wants to do the model work, not the data work”: Data Cascades in High-Stakes AI](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/0d556e45afc54afeb2eb6b51a9bc1827b9961ff4.pdf). Vicki Boykis refers to this as one of the first formal sources citing explicitly the previously implicit knowledge that data quality matters for ML model performance. *Data cascades* is defined as *compounding events causing negative, downstream effects from data issues, resulting in technical debt over time*. The paper is based on a qualitative study of practices among 53 AI practitioners working in *high stakes* domain, which they define as *domains that have safety impacts on living beings*, such as climate change and maternal health. 

Data workers play a critical role in creating and maintaining AI systems, and their work has downstream impact. 

## Garbage in, garbage out 
Data quality is crucial to ML model performance. Andrew Ng provided a few examples of the importance of data quality in his recent webinar [A chat with Andrew on MLOps: From model-centric to data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo). However, this field is quite immature, demonstrated by the fact that the webinar, and deeplearning.ai courses in general, lack introductions to concrete tools and rigorous processes to lean data-centric.

Data cleaning usually involves integrity constraints, type inference, schema matching, outlier detection and more. Several tools have been created to streamline this process, such as [Great expectations](https://greatexpectations.io/), [Tensorflow data validation](https://www.tensorflow.org/tfx/guide/tfdv) and [Deequ](https://pydeequ.readthedocs.io/en/latest/README.html). An important trait here is to catch the bugs through data validation, not through model performance deterioration: the data quality work will suffer when it is seen as a by-product of model performance monitoring.

Data validation and cleaning focuses on one part of the data lifecycle, but especially in high stakes environment, the birth and afterlife of data needs attion as well, i.e. the data creation, collection process and downstream life of data. We should view data as a dynamic entity with possibility for drifts and skews, requiring follow-up. A further complicating factor is that data quality work is cross-functional in nature: dataset definition and labelling accuracy often depend on subject matter expertice.

## Data cascades are hard to spot, and require non-conventional AI practices
According to the paper, data cascades are **opaque**, meaning that 
Practitioners were not equipped to identify upstream or downstream issues. They lacked tools and metrics to detect and measure the effects on systems. As a proxy, model performance metrics were used, which test the whole system, not the datasets. 

The study also found that **"conventional" AI practices are insufficient**: Applying "conventional" AI practices in high stakes domains triggers data cascades. Some examples provided are moving fast, hyperparameter tuning to improve model performance instead of data quality work. 

## Undervaluation of data work manifests in ML metrics, ML prestige and education programs
The paper describes several factors in the ML ecosystem that contribute to data cascades, among the the **incentives and currency in AI**, and the **lack of data education**. 

Model improvements can be easily tracked and rewarded through model performance metrics. Data improvements are not monitored in the same way. In addition, model development and architectures holds a prestige in the community, whereas data work is neglected. ImageNet, the database of labelled images which has been crucial for computer vision, initially received little recognition as ML work. Fei-Fei Li, the AI researcher who lead the project, struggled to receive funding in the beginning, with rejections commenting that it was [shameful that a Princeton professor would research the topic](https://qz.com/1034972/the-data-that-changed-the-direction-of-ai-research-and-possibly-the-world/). The undervaluation of data work is not only among practitioners: The study found that there was little buy-in along decision makers and funders for working on data quality improvement. 

Lack of focus on data in education programs left practitioners at a loss when faced with the realities of data in the wild: "In real life we never see clean data," one of the subjects said. In spite of this, training and education provides little guidance on how to collect, clean and document datasets, let alone handle live data. The study included both US practitioners, mostly from AI specialisations in graduate programs, and Indian, West African and East African practitioners, who were mostly self-taught after completing CS degrees. Data engineering was under-emphasized in both routes.

## Categories of data cascades
The paper provides detailed descriptions of the four most prevalent categories of data cascades, including many disheartening citations from the practitioners. 
* **Physical-world brittleness** was the most common, and is caused by changes in the world we are modelling, such as hardware drifts, changes in environment, human behaviour or legislation. Mitigations to physical-world brittleness cascades included:
  * **Monitoring data sources** (often at an example level)
  * **Introducing noise in the training dataset** to overcome the disparage between pristine training data and messy live data
  * **Investing in data literacy** for system operators and field partners as also introduced in a few cases
* **Inadequate domain expertise**: When AI practitioners were tasked with defining ground truth, identifying the necessary feature set and interpreting data, data cascades were triggered. These errors were **very costly**, often only discovered after model deployment. Consequences ranged from requiring additional data collection, addition of new data sources to entire data collection pipelines needed to be reworked. The study gives two important subclasses of inadequate domain expertise: Subjectivity in ground truth, leading to ambiguous labels, and defining and collecting representative data. Mitigations included:
  * **End-to-end domain expertise involvement**, not only in early stages or trouble shooting situations, as many projects do, but deep involvement. 
  * **Defining representative datasets** particular to the domain and problem definition at hand is also crucial
* **Concflicting reward systems**: Conventional AI practices viewing data collection as a non-technical task to be outsourced to field partners, caused problems in high stakes domains. Common problems were field partners missing incentives for data quality and having conflicting tasks. In addition, field partners often had poor data literacy, and didn't understand the impact of the data collection process. Mitigating measures included
  * **Data literacy training**, however, this was very rarely provided. When training was given, data quality was reported to improve. One practitioner reported providing real time feedback on data quality indicators to field partners, as a training. 
  * **Partnerships with field partners**, lead by top level management, could have improved the incentive and task conflicts, but most practitioners reported that top level management did not prioritize this.
* **Poor cross-organisational documentation**: Conventional AI practice of neglecting data documentation is especially damaging in domains where the volume of data is low. [Documentation practices have been suggested](https://arxiv.org/pdf/1803.09010.pdf), but are not widely implemented. These cascades were often discovered through chance through manual review. Many practitioners also complained of lack of standards when entering data, and issues with vendor documentation for data collecting equiment. Mitigating these issues involved clear procedures and meticulous attention: 
  * Data collection plans
  * Data strategy handbooks
  * Design documents
  * File conventions

## The problem can be avoided
Step-wise and early interventions in the development process enables practicioners to avoid data cascades, according to the investigation. However, this was rare, due to undervaluation of data work and partner dependencies. Katie Bauer recently published a related thread on how the concept **shifting left**, used about information security work in the book [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339), applies to data science and data practices: 

{% twitter https://twitter.com/imightbemary/status/1371857703077736454?s=20 %}

In addition to the mitigating actions individuals can take, we need to shift our reactive processes, viewing data as "grunt work", to a proactive focus on data excellence. The paper suggests three improvement areas for education, conferences and organisations to begin to move the needle on the prestige of data work, and summarized the practices of the high-performing teams.

### What should you change tomorrow? Incorporate best software practices adapted to data
Data cascades surface the need for several feedback channels at different stages in the AI lifecycle. The teams with the fewest data cascades showed some common practices: 
- step-wise feedback loops throughout the development iterations
- frequenct model runs
- close collaboration with domain experts and field partners
- maintained clear data documentation
- regular monitoring of incoming data

These practices mirror software development practices adapted to data. This reduces uncertainty and data cascades building up.

### Research is required to go from goodness-of-fit to goodness-of-data
Today, the community is overly reliant on goodness-of-fit metrics. This leads to creating models that fit well to training data, but ignoring the issue of whether the data fits the real world phenomenon we are modelling. In addition, the metrics are only available at a later stage in development, but course correction for data sources should start as early as possible. This could prevent data cascades, and ensure data can be used for several applications. Measuring goodness-of-data will also allow improvements. That being said, [metrics](https://arxiv.org/ftp/arxiv/papers/2002/2002.08512.pdf) [are](https://lineardigressions.com/episodes/2019/12/22/data-scientists-beware-of-simple-metrics) [always](https://arxiv.org/pdf/1909.12475.pdf) [problematic](https://gunnhildsp.github.io/notes/metrics/data-science/2020/03/07/metrics.html), and as of now, research on goodness-of-data metrics is immature.

### Organisations and conferences should incentivise data excellence
Scientific and purposeful processes outlined in human centered computing contrast the reality of the AI practitioners, who tended to view data as *operations*, far from the glamour of model work. Conferences should be part of the necessary culture change, accepting and highlighting data exellence. Organisations should reward data collection, pipeline maintenance, data documentation etc. in promotions and peer reviews. Data work is currently lopsided, with domain experts and field partners doing one-off inconvenient jobs. Data exellence emphasizes partnerships and deep involvement of domain experts, sharing credit for work should only be natural. 

### AI education should provide real world data literacy training
The practical data skill gap induced by pristine practice dataset in education is substancial. Training on data collection, curation and inter-disciplinary collaboration can help prepare future practitioners. There is a large body of work from human centered computing and data ethics to draw on. 

## Additions to the reading list
The paper cites a lot of interesting work. I noted in particular the following papers:
* Practitioners have shown to collaborate much less around datasets, relative to collaboration around code: [How do data science workers collaborate? Roles, workflows and tools](https://arxiv.org/pdf/2001.06684.pdf) by Amy X Zhang, Michael Muller, and Dakuo Wang.
* Melanie Feinberg describes data as a design material and our role as designers of data, not it's appropriators: [A design perspective on data](https://ils.unc.edu/~mfeinber/Feinberg%202017c.pdf) by Melanie Feinberg.
* Muller et al. extend and outline five approaches of data scientists to perform analyses: [How data science work-ers work with data: Discovery, capture, curation, design, creation](http://library.usc.edu.ph/ACM/CHI2019/1proc/paper126.pdf), by Muller, Lange, Wang, Piorkowski, Tsay, Liao, Dugan and Erickson. 
