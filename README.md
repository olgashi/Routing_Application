# Routing_Application

 DATA STRUCTURES AND ALGORITHMS II - C950 9 June, 2020
Olga Shiryaeva
Problem statement (from requirements page):
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.
Solution overview:
Basic greedy algorithm (located in core_algorithm.py) was used for determining a distance between two addresses. A path between any two addresses is stored in a graph data structure.
Since we know that we have at least one path for any two addresses, it is reasonable to say the average time ‘look up’ for a single path is O(1). Lookup for all packages is O(n), where n is a total number of packages. The resulting total distance travelled for all trucks/deliveries is 70.10 miles. When developing the solution Python version 3.8 was used.
Data Structures used
Graph data structure is used to maintain and access information about shipping destinations along with distances between them. Each vertex in the graph represents a single location. Graph has a list

 of all edges along with edges connected to them (list of key value pairs, where key is a given edge and value is a list of all vertices connected to it).
Additionally, there is a list on the graph data structure, that contains information about distances between all edges, and is represented by key value pairs where key is a set of two locations and value is the distance between them. In this solution there is only one connecting edge for any two vertices (two if we count both directions).
Hash Table data structure is used to represent package data. When populating table with package objects, the solution hashes the package id (​hash(key) % length of the table, where key is the packageid)​ ofaspecificpackageandmapsittoaPackageobjectcontainingallprovideddetailsfor that object. ‘Maps’, means that it associates a hashed key value of the package with the package object itself. Since each package has a unique id, there are no collisions. Each Package object is an instance of a Package class and it contains all required information for that specific package.
Hash Table data structure data can be manipulated and accessed via insert, search and remove methods, each having O(1) run time complexity.
Core Algorithm Overview
● Manually separate packages into 3 piles (taking into account any restrictions such as special notes and package delivery deadlines), one is designated for the first truck and two are designated for the second truck (two separate trips). Third truck is not used.
● The first truck starts making deliveries and leaves HUB at 8:00 am, the second truck goes out at 9:05 am. Once the second truck is finished, it comes back to the HUB to get the remaining packages and delivers those as well.

 ● Repeat for all three piles until all packages are delivered:
○ For each package on a given truck at each trip:
■ Look up an address pair which represents a key, in that key the first element is the current location and second is a shipping address of the package. Look up is performed in a list of key-value pairs where key is a pair and the value is the distance between the two locations.
Look up has run time complexity of O(1).
■ If the pair exists, then add corresponding distance to the running total; update package status and actual delivery time.
Loading and parsing package and location data
Location data and package data is loaded from csv files dynamically. There are two separate methods that load data into a corresponding data structure, read_packages_csv_file and read_locations_csv_file (both located in utils/input_data_utils.py).
In case the solution has to be scaled (either number of packages or number of locations), no additional modifications to the code are needed, it will support any number of packages or locations. The only requirement is that csv files, that contain location and package data, are kept in the same format.
Space-time complexity
Comments describing space-time complexity are distributed throughout the solution.
Adaptability to a changing market and to scalability

 The solution is easily adaptable to changing markets and to scalability. Loading data can be done with no additional changes to the code. The only thing, I think would need additional changes if scaling is needed, is sorting the packages. In case of scaling, sorting will need to be rewritten, so it is done dynamically.
Maintainability
Overall, code was written with maintainability in mind. The program is organized into separate modules for clarity and easy updates.
Data​ structure to store the package data
Each package and its corresponding details are stored in a Hash Table data structure. We know that each package is unique and there are no collisions, so a single lookup (search) is done with an average-case runtime of O(1).
Populating a Hash Table with packages takes O(n), where n is the number of packages. Main advantage of keeping package data in a Hash Table is the speed of the lookup (O(1))
Interface for the insert and look-up functions to view the status of any package at any time
Interface is provided and ran via main.py. Once main.py is run, the delivery simulation is performed and
the user is able to lookup the status of the package at any time during the day of the delivery (using data generated by the simulation).
Additionally, there is a functionality that lets the user see the total distance all trucks traveled and information for a specific package, including actual delivery time and status.

 Screenshots to show package status of ​all packages at a time between 8:35 a.m. and 9:25 a.m., 9:35 a.m. and 10:25 a.m., 12:03 p.m. and 1:12 p.m.
Once the program is started, the user sees several options for commands they can use: id, time, distance, clear, exit.
 Below are the screenshots with statuses for all packages at different times throughout the day.

 
 
 
 
 
 
 
 
 An example of using ‘distance’ command to look up total distance for all trips.

  An example of running the ‘id’ command that lets the user view details about a specific package by providing its id.

  Details for each package, including package id, address, actual delivery time and delivery deadline

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  Justification of the ​choice of core algorithm
Core algorithm of the solution has two main advantages: ● Ease of implementation

 Once the package data is added to a hash table and location data is set up as a graph data structure, the algorithm for determining the distance between two points is a simple key-value lookup that takes constant time. For all packages its run time complexity is O(n).
● Speed
Although it is relatively fast (O(n), where n is a number of packages) and easy to implement, it requires that at least one path between any two points exists in the list of paths/routes. Otherwise, the algorithm will not work. Additionally, populating a graph with routes (edges) for all given locations has run time complexity of O(n^2) and can be added to total run time complexity since it is an essential part of the core algorithm.
Two other algorithms that could be used and would have met the criteria and requirements:
● Nearest neighbor algorithm
● Dijkstra's algorithm
Nearest neighbor algorithm overview:
It uses graph data structure. Worst case runtime is O(n^2), worst case space complexity is O(n^2). Pseudocode:
1. Initialize all vertices as unvisited, where each vertex is a shipping destination.
2. Choose “HUB” as the current vertex ​u​, mark current vertex as visited, ​v represents unvisited
vertex.
3. Determine the shortest edge/path connecting ​u and ​v. ​Look up the distance value for that edge and add to the running total, mark package as delivered and update its delivery time.

 4. Set ​v​ to be the current vertex ​u​ and then mark ​v​ as visited.
5. If all the vertices/shipping destinations are visited (all packages are delivered), end the
program. Else, go to step 3.
This algorithm outputs a sequence of the visited vertices (shipping destinations).
The main difference between the algorithm that was used in the solution and ‘Nearest neighbors’ is that ‘Nearest neighbors’ does not do sorting of the packages (solution uses manual sorting). Instead it is provided with a list of destinations and a starting point. It ‘sorts’ by determining the optimal path for deliveries. The drawback of ‘Nearest neighbors’ in this case is that there may be more than one path from one point to the next and it could potentially choose a less optimal path due to the fact that it is a ‘greedy’ algorithm. When in the solution, there is only one path for any two points (two if you count both directions).
Dijkstra's algorithm overview:
It works with both directed and undirected graphs, all edges have to have non negative weights (distances). Worst case run time complexity is O(|E| + V log|V|), where E is the number of edges and V is the number of vertices.
Pseudocode:
1. Initialize distance to current vertex (location/address) to zero
2. Set all other weights/distances to infinity
3. Set the set of visited vertices (locations/addresses) as empty
4. Set queue Q to contain all vertices
5. While the Q is not empty
6. Select the vertex u that has shortest distance

 7. Add u to the list of visited vertices
8. Relax all vertices adjacent to u
The Dijkstra algorithm will choose the most optimal path to the final destination. Even though it is also a ‘greedy’ algorithm, it will produce an optimal path.
The main difference between the Dijkstra and the solution is that the solution does not actually create a path, but simply picks an existing path from a list of paths for each of the destinations. It will fail to deliver a package if the edge connecting current location and that package’s shipping destination is not in the list of connected edges. Whereas Dijkstra will still find a path because it will look for a path through other vertices.
What you would do differently if you did this project again
I would build an additional ‘sorting’ algorithm, instead of manually sorting the packages and distributing them between truck loads.
Justification of data structure choice
Graph data structure is used to store data about shipping destinations along with distances between them. Each location is represented by a vertex and each vertex is connected to every other vertex by one edge. There is a list on the graph data structure, that contains information about distances between all edges, and is represented by key value pairs where key is a set of two locations and value is the distance between them. The solution has one connecting edge for any two vertices (two if we count both directions). Using graph data structure allows for easy look up of any connecting

 edge and a way to know which vertices any given vertex is connected to (especially imported if the solution will need to be updated in the future to accommodate a different core algorithm).
Hash Table data structure is used to represent package data. It hashes the package id of a specific package and associates a hashed key value of the package with the package object itself. Since each package has a unique id, there are no collisions. It allows for easy search, insert or delete, each having O(1) run time complexity.
No changes to the code needed if more than 40 packages are to be delivered. The only requirement is that at least 1 path for any two locations exists.
Two other data structures that can meet the same criteria and requirements:
Packages can be stored in a queue, which can be represented as a Linked-list data structure. The main drawback is that lookup of a package will take O(n) time in the worst case scenario (n is number of packages), whereas with a hash table it takes O(1).
In order for this solution to be optimal, we need to determine the optimal destination as we are building the queue, so that the order of packages in a queue would represent the path from HUB to the last package’s shipping address.
Packages can also be stored in a basic list or array. The main disadvantage is that lookup takes O(n) in the worst case scenario.
Sources Used
T. Cormen,”Introduction to Algorithms”, third edition, MIT Press
“​C950: Data Structures and Algorithms II”, ZyBooks course material

 “Hash table runtime complexity (insert, search and delete)” question/answer, stackoverflow.com https://stackoverflow.com/questions/9214353/hash-table-runtime-complexity-insert-search-and-delet e#9214594
Heuristics for the Traveling Salesman Problem, Christian Nilsson Link ̈oping University http://160592857366.free.fr/joe/ebooks/ShareData/Heuristics%20for%20the%20Traveling%20Sales man%20Problem%20By%20Christian%20Nillson.pdf
Nearest neighbour algorithm, Wikipedia, ​https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
     
