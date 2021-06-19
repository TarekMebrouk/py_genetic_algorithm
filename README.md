<H1> Genetic algorithm </h1>
  <H6> University of Science and Technology USTHB </H6>
  <H6> IT department </H6>
  <H6> End-of-study project in license year (2020/2021) </H6>
  
<H3> Source of inspiration </H3>
<br>
Genetic algorithms are optimization algorithms based on techniques
derived from genetics and natural evolution: selection, crosses, mutations, etc.
Genetic algorithms already have a relatively old history since the first
John Holland's work on adaptive systems dates back to 1962 [9]. The work of
David Goldberg [10] largely contributed to popularize them.
<br>

<H3> Fonctionnement </H3>
<br>
Genetic algorithms iteratively modify a population of solutions into
applying genetic operators. Their operating principle is based on
the exploration of new solution spaces, from an initial population and as long as a
stop criterion is not verified, the algorithm will proceed to create new individuals at
from the current population.
According to a selection strategy chosen at the outset, a certain number of individuals from the
population is selected ("parent") then the recombination plan will allow obtaining
new individuals ("children") who inherit the good characteristics of the solutions
"Parent". The procedure is restarted after integrating the new individuals into the
initial population (using a special mutation process to diversify the solution to
subspaces not already visited). The genetic algorithm is then based on 3 functionalities
main:
<br>

- Selection: the genetic algorithm uses this strategy to choose individuals
of the population at each iteration (choice at random or of the best individuals) and
mix them randomly to create new individuals in order to improve
population.
There are several types of selection in this search:

 <H4> 1 - Selection by tournament. </H4> 
 <H4> 2 - Selection by roulette. </H4> 
 <H4> 3 - Selection by rank. </H4> 
 <H4> 4 - Selection by elitism. </H4> 

- Crossbreeding: represents the procedure of combining the individuals selected by
"selection", its principle is to combine 2 "parent" solutions to form
"Children" who inherit good characteristics from their parents.
There are several ways to combine 2 solutions of the treated problem, among these
methods :

<H4> 1 - Simple crossing. </H4> 
<H4> 2 - Multipoint crossing. </H4> 

- Mutation: this changes the characteristics of a solution allowing
to explore new areas of solutions (factor of diversification). This operator
plays the role of a "disruptive" element, it introduces "noise" into the
population (the type of modification or the "noise" depends directly on the problem
processed (data structure of the processed solutions)).
Among the variants of genetic algorithms, we can cite the following two:
<br>
- The population replacement version:

From an initial population P (containing "n" solutions | P | = n), we construct a
second population P * in parallel. The general principle is to go through the three
important steps (selection, crossing, mutation) several times and at each iteration we
constructs two "children", we insert them in the population P * until | P * | = | P | then
we switch between P and P * and we start the process again with the new population P
until the stop criterion is satisfied.
In this algorithm the crossing and mutation procedures are done under a
probability condition.

<br>
- The incremental replacement version:
The principle consists in creating new individuals (by selection, crossing and
mutation), something that is done under a condition (probability). After building a
new individual "child", one replaces a "parent" in the population P by the new
solution found.
For the choice of the "parent" to replace, we can choose the worst (the value of the
"fitness" objective function of the chosen parent is the worst in the population
previous), or use the binary tournament technique or another technique that
depends on the problem being treated. We repeat the process several times until satisfaction of the stop criterion.
<br>

<H3> Intensification / diversification aspect </H3>
<br>
For both versions of the genetic algorithm, the intensification aspect is represented by
the operator of selection and crossing because the two processes favor the best
solutions (the selection chooses the two best parents of the current population and the
crossing creates new individuals "children" who take advantage of the good characteristics
parents). Mutation makes it possible to modify the characteristics of a solution
(disturbance), it thus ensures the change from the search space to subspaces
not already explored. So this process undoubtedly represents the main factor of the
diversification.
<br>

<H3> Advantages and disadvantages : </H3>
Genetic algorithms have a strong potential of practical applications (used in
multiple areas) and provide excellent performance. This type of mechanism could
seem magical, the difficulties are invisible but very real. The first of them
consists of choosing the various parameters: percentage of crossing, percentage of
mutation and population size, but the most important issue remains the coding of
data. Using this procedure is often computationally expensive. 


