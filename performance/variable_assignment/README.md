# variable assignment
# method
On each trial, we run the code with the loop 100000 times each with and without garbage collection.
# code
## inside
total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i

## outside
i = 0
total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i

# results
|  Trial  |   inside (gc)   |   outside (gc)   |   inside (w/o gc)   |   outside (w/o gc)   |
|:-------:|:---------------:|:----------------:|:-------------------:|:--------------------:|
| 1       |     36.4853     |     40.2039      |       35.9772       |       37.3973        |
| 2       |     38.2650     |     36.6842      |       64.9883       |       78.7694        |
| 3       |     51.0261     |     51.9533      |       48.2219       |       50.7608        |
| 4       |     50.1293     |     48.8253      |       51.0740       |       41.4610        |
| 5       |     39.9235     |     41.1098      |       40.8048       |       38.2779        |
| 6       |     45.3781     |     39.8215      |       41.0781       |       40.3324        |
| 7       |     42.1352     |     42.4717      |       45.8082       |       44.3277        |
| 8       |     45.7612     |     40.2000      |       40.2900       |       44.3383        |
| 9       |     43.9968     |     44.7974      |       46.9256       |       50.4430        |
| 10      |     40.7364     |     40.0896      |       42.2261       |       44.1519        |
| *Sum*   |   *433.8369*    |   *426.1567‬*     |     *457.3942*      |     *470.2597*       |
| **Average** | **43.3837** |   **42.6157**    |     **45.7394**     |     **47.0260**      |

# conclusions
There is an almost insignificant benefit to instantiating the variable outside of the 

# future work
Does python optimize away loops.