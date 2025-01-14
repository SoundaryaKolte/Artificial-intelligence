#include <iostream>
using namespace std;

#define V 5  // Number of vertices in the graph

// Function to find the vertex with the minimum key value that is not yet included in MST
int minKey(int key[], bool inMST[]) {
    int min = 1000000;  // A large value to represent "infinity"
    int min_index;

    // Find the vertex with the smallest key value that is not yet in MST
    for (int v = 0; v < V; v++) {
        if (!inMST[v] && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

// Function to implement Prim's MST algorithm
void primMST(int graph[V][V]) {
    int parent[V];   // Array to store the constructed MST
    int key[V];      // Key values used to pick the minimum weight edge
    bool inMST[V];   // To track vertices already included in MST

    // Initialize all keys as a large number (representing infinity)
    for (int i = 0; i < V; i++) {
        key[i] = 1000000;  // Set initial key value as a large number
        inMST[i] = false;  // Initially, no vertex is included in MST
    }

    // Make key[0] 0 so that the first vertex is picked as the starting point
    key[0] = 0;
    parent[0] = -1;  // Starting vertex has no parent

    // The MST will have V vertices
    for (int count = 0; count < V - 1; count++) {
        // Pick the vertex with the minimum key value from the set of vertices not yet included in MST
        int u = minKey(key, inMST);

        // Add the picked vertex to the MST
        inMST[u] = true;

        // Update the key and parent indices of the adjacent vertices
        for (int v = 0; v < V; v++) {
            // Only update the key if the edge exists, and v is not in MST
            if (graph[u][v] != 0 && !inMST[v] && graph[u][v] < key[v]) {
                key[v] = graph[u][v];
                parent[v] = u;
            }
        }
    }

    // Print the constructed MST
    cout << "Edge \tWeight\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << "\t" << graph[i][parent[i]] << "\n";
    }
}

// Main function to test the above implementation
int main() {
    // Example graph (Adjacency Matrix Representation)
    int graph[V][V] = { 
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    primMST(graph);

    return 0;
}


/*output:Edge 	Weight
0 - 1	2
1 - 2	3
0 - 3	6
1 - 4	5
*/
