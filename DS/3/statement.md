xyz has a city of his own. where every house is connected to other houses by roads. he wants to turn one of the houses into city center such that the summation of distances from city center other houses is as small as possible. formally, if house i is the city center then &#8721;d(i,j) for every j != i is minimum where d(i,j) is the minimum time required to go from i to j. 

**Input:**

first line of the input will contain an integer t, the number of testcases. first line of each testcase will contain N and E, number of houses and number of roads followed by E lines of the format a b w 
denoting that there is a road between house a and house b of weight w.  

**Constraints:**

    N <= 10<sup>3</sup>
    E <= 10<sup>3</sup>
    w <= 10<sup>6</sup>


**Output:**

print one integer, the number of the house that xyz should turn into a city center.