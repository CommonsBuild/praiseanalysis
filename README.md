# TE Commons

# Impact Hours / Token Distribution

Data set being analyzed: https://docs.google.com/spreadsheets/d/1qvmwwlUHnQWYc2JQRoE1Qo_IKx6a4CI9ehWIMvkiqFc/edit#gid=2142373003

(That's right, analyze! Get that weak "s" outta here)

The Praise system was an evolving process and had clear points of change that
have impact on the data set.

Round #0 = Historic data. This is the first round, it took praise from the
previous months that were relevant to the TEC and scored them.

Round #1 - #5 = **Centralized Tiered Praise**. Livia and Griff were the only
quantifiers and recieved the Mode praise amount    



### Data Science Research Topics for Praise Analysis:

0. Gini Index
1. UBIH
2. Distributions and Interventions
3. TRIBUTE TO THE ANCESTORS - Considering TE contributions prior to IH
4. Modulating the paid contributor discount rate
5. What is the price of governance? - Paid contributions X discounted IH
6. Grouping duplicated praise.
7. Categorizing Praise.(Twitter/Meetings/Coding/Research)
8. Are there imbalanced type distributions? 
9. How did the validators do?
10. Can we see clusters in the network such as working groups?
11. At what points are the outputs of the praise system aligned with the mission, vision, and values of the community, at what points are they not aligned?
12. What can we learn about the praise collecting process? How can it be improved for future commons deployments? 

### Analysis Results

0. Gini Index
Can we apply the Gini Index to the distribution? What does this look like?

1. UBIH
What does UBI look like applied to the data? Can we parameterize this?

"Universal Basic Impact Hours?" How does adding a fixed amount of IH to all
hatchers change the mean and the mode of the distribution before and after this
intervention? 

Visualize the distributions before and after and intervention such as UBI
 
Can we parameterize this by the amount of UBI that we apply?

How do we vote on these interventions? Using what we have got so far to
improve. Tokenlog it is. Run a DAO through github issues, continuously
self-modify the token distributions using data science and community sense
making.


2. Distributions and Interventions
What does applying interventions, filters, or transformations do to the to the
distribution? What other kind of interventions might be interesting?

3. TRIBUTE TO THE ANCESTORS 

Plot Contributions to TE Commons vs. contributions to Token Engineering
(discipline) in the past or in parallel - Archetype detection - (Manually)
Identify agents that are known to have been producing token engineering public
goods before the recording of impact hours started. Should we apply an NFT -
TEC OG - Multiplicative factor?

4. Modulating the paid contributor discount rate
What does it look like when we modulate the paid contributor discount rate from 0.15 to 1?

5. What is the price of governance?
Can we compare the total money paid to stewards against the total number of IH
that has been reduced from them? Can we compare this with TEC price outcomes?

Weigh the balance of discounts applied to Impact Hours Received for those who
are compensated from CSTK/TEC .

Perhaps consider an alternative future build where in which no one gets
discounts on their praise, and rather everyone gets a UBI. 

6. Grouping duplicated praise

7. Can we categorize the Praise?
Can we identify tweets from research? Can we identify coding from comms? What are the different
praise buckets? What does this look like and how is each bucket weighted? Does this reflect the
values of the community?

8. How many IH  are there Imbalanced type distributions (twitter/meetings, related to #1) - **WG IH Categories**

9. How did the Validators do?
How are the weightings? 

10. Can we see clusters in the network such as working groups?
11. At what points are the outputs of the praise system aligned with the mission, vision, and values of the community, at what points are they not aligned?

12. What can we learn about the praise collecting process? How can it be improved for future commons deployments? 


#### Notes from the Community

**Gravity(Juan)**:
1. Communications and transparency to avoid miscommunication
2. OK for people to gain IH, but not to take away
3. Very sensitive topic as it relates to wages and compensation

**Jeff**:
No proposed action through sake of analysis, but more infomation will give us a sense of how to align the system with our goals

**Griff:**
Every two weeks, impact hour quantification. We had a very interesting discussion of if we should divert from our current process given these insights and discussions. We decided not to divert as we havn't concluded results from this analysis yet (even though we can see some flaws now). It was hard.

**Tam:**
Adjusting a single praise session wouldn't adjust for the many months prior, and we are excited for this to be a community decision. 

Conjecture: The pool of funds allocated to builders is zero sum. i.e. any IH imbalance is taking voice from those with less IH to give to those with more IH.

Taking from Peter to pay Paul becomes a systemic issue when the majority of participants are Peter.


**Examples where using the raw IH data is dangerous:**
- Do we feel that it is fair that some TEC members who showed up for meetings for a few months, accumulated more IH than one of the creators of the TE field itself?
- Do we feel that it is fair that one of the primary driving members of the TEC has to spend $60,000 to have equivalent voice in this new economy as other members whose tasks were disproportionately rewarded by the praise process?
- Is it fair that contributors who have been building deep infrastructure for the TEC for years have 50-90% LESS VOICE in this economy than contributors who have been active in admin duties for the past 3-6 months?

**Source:**
https://docs.google.com/spreadsheets/d/1i6UaBb7n36HTZ6Ww2T6VrhjzW_7gIBTxHGM5wom27NE/edit?usp=sharing


## What are some ideas about how the analysis can be done?

**YGG desired data science approach**
-Praise data as a network
-Every person is a node, and there are edges
-Clustering: each WG is a cluster
-How the praise has transformed over time, a “drift” in the way praise was dished - put on time axis/multi-dimensionality

**Andrew**
Tends towards simplest possible solution so any changes/alterations don’t become a roadblock 

**Z**
-Sanity check
-Ignore who was giving/receiving - look at group by aggregate - irrespective of who received it
-How much was dished for what type of action - software dev/giving talks/sectors - what are the fractions of those buckets
-Is this what we were going for?
-What is it weighting towards at v
-If it is determined that some types of work are underrepresented / active and visible vs. deeper work unseen
-Intersubjective measurement - extent to which those reflections are doing what we intended
-Transparent policies to modify to improve purpose towards goal
-We have to make time to question the process/tool 
-Generated raw data - no perfectly objective data / “sensemaking” process of human input works from the process side - should be kept separately 
-The algorithmic processing is working differently - from the goals first 
-Algo should not be used as oracle, we should question if it is doing what we want
-Algos are in service of the sensemaking process - if it doesn’t feel right, we can do better - feedback loop - what did we intend, it doesn’t feel right, should or shouldn’t we do something - does the algo fail to express what we intended
-We can just document - make sure we question - algos in service of social process
-We govern algos rather than they gov us

**Griff**
-We adjust from the inside to try and adjust the distribution, this may have polluted the data
-We will start keeping that in a separate tab

Categories
Lightweight, fast, and high impact. Eyes on the prize, looking at allocating the builders pool of governance weight in the TEC. Keep this in mind as an implementable process that we can dig into soon.

    Categories the data

Number of praises Looking at drift - related to praise in calls (double praise)

Interesting to look at segmentations - As of now with raw data it does seem really skewed

    Always paid
    Sometimes paid
    Never paid

Distribution percentages - Distribution of how many people have what percentage. What are the distributions, what is the range between those distributions. If we remove the extremes and look at the mode.

Look for outliers first Multiple stages, look at the data before removing them. Then look at it after removing them. It's all an experiment, it's going to be messy, and we are going to learn at every step.

**High level categories TE Work**
- Should consider never paid / always paid / sometimes paid
- Many ways to slice the data
- Contrast approaches of big pic goal oriented top down vs. categories bottom up


Best Case Scenario - data scientist for a week who can lead would be ideal
* 4-8 hrs to focus
* Danilo/Shawn/Shinichi feedback and support
* Next Sunday again
* Hack session 5-6 ppl
* 2hr session



Looking at the praise data, it seems that a lot of small praises accumulate significantly more tokens than larger tasks with less frequent praise, even if they are quantified relatively much higher. This begs the question: do the results we see land within what we would call a fair or accurate distribution of tokens for work that was put into the efforts of the TEC?

Source:
TEC Forum Discussion
https://forum.tecommons.org/t/pre-hatch-impact-hours-distribution-analysis/376

Document Library
https://docs.google.com/document/d/1QiVfjtFDW1ahehdVXFV4Dauo5k_QM77FOUHS9CWmu7k/edit

Repo
https://github.com/CommonsBuild/praiseanalysis

Analysis by Octopus
https://colab.research.google.com/drive/1Lz2lrIkZbPLmgms5TrgUx8iO9sWDe3hN?usp=sharing

TEC Praise Data Sheet
https://docs.google.com/spreadsheets/d/1qvmwwlUHnQWYc2JQRoE1Qo_IKx6a4CI9ehWIMvkiqFc/edit#gid=1510055853

Processed Data
https://docs.google.com/spreadsheets/d/1K1CeAG-1E1UUk4P7lsM9MR_Fwvap8ch0WrZlPORESgQ/edit#gid=1975905774

Initial Analysis by Jeff
https://docs.google.com/spreadsheets/d/1i6UaBb7n36HTZ6Ww2T6VrhjzW_7gIBTxHGM5wom27NE/edit?usp=sharing

