/*********************************************


https://www.programiz.com/dsa/graph-adjacency-list
https://thispointer.com/difference-between-vector-and-list-in-c/
Se usó STL (Standar Template Library) por facilidad

**********************************************/
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

class Graph {
  public:
  long int numNodes;
  list<int> *adjList;
  // BFS tree
  //list<int> *BSF_tree;
  // reversal
  list<int> *reversal;

  Graph(long int V);
  void addEdge(int src, int dest);
  // BFS tree
  void k_hops(int s, int k);     // s -> root

  // k-path to u
  void inv_path(int s, int k);  // s -> destiny

  // independent set
  void ind_set(int s, int k);  // s -> element; k -> number of elements
};

Graph::Graph(long int V) {
  numNodes = V;
  adjList = new list<int>[V];       // asignación de memoria para la adjList
  //BSF_tree = new list<int>[V];
  reversal = new list<int>[V];
}

void Graph::addEdge(int src, int dest) {
  adjList[src].push_front(dest);
}

void Graph::k_hops(int root, int k){
  // u -> source
  // v -> destiny
  // i -> layer counter
  int u, v, i = 0;
  // Nodos descubiertos
  int Discovered[numNodes];
  // listas de los nodos en layers y de los elementos adyacentes a un nodo
  list<int> L_curr, L_next, u_edges;

  ofstream edges_k_h_file;
  edges_k_h_file.open("edges_k_hops.csv");
  edges_k_h_file << "from,to\n";

  Discovered[root] = 1;
  // queue
  L_curr.push_back(root);
  // queue no vacío y el número de layers sea menor a los hops
  while(!L_curr.empty() && i < k){
    // popeamos el siguiente elemento del queue u
    u = L_curr.front();
    L_curr.pop_front();
    cout << u << endl;
    // tomamos la lista de adyacencia de u
    u_edges = adjList[u];
    // analizamos los nodos adyacentes a u
    while (!u_edges.empty()) {
      v = u_edges.front();
      u_edges.pop_front();

      if (Discovered[v] != 1){
        Discovered[v] = 1;
        L_next.push_back(v);
        // agregamos el nodo u,v a un file con los datos
        edges_k_h_file << u << "," << v << "\n";
        //cout << u << " " << L_next.back() << endl;
      }
    }

    // ver el almacenamiento para el siguiente layer
    cout << "LAYER" << " ";
    for (auto const &w : L_next){
      cout << w << " ";
    }
    cout << endl;

    // condición para pasar al siguiente layer, que el actual sea vacío
    if (L_curr.empty()){
      L_curr = L_next;
      L_next.clear();  // liberar el espacio
      i++;     // actualizar el nivel del layer
    }
  }
  edges_k_h_file.close();
}

void Graph::inv_path(int s, int k){
  // Inicialización de variables para el DFS
  list<int> Stack_n;   // stack de nodos
  list<int> longest_path;
  int n_depth = 0;   // número de profundidad
  int ext_node;    // nodo más al exterior
  bool Discovered[numNodes];
  bool add_node;   // true si se agrega un nodo al stack, false en cc
  Discovered[s] = true;

  // reversal del grafito
  for (int i = 0; i < numNodes; i++){
    for (auto const &w : adjList[i]){
      reversal[w].push_front(i);
    }
  }
  /* Si sirve el algoritmo anterior para reverso del grafito */
  int test_node = s;//60640;
  cout << "nodo de muestra:\t" << test_node <<endl;
  for (auto const &w : reversal[test_node]){
    cout << w << " ";
  }
  cout << endl;
  /*----------*/
  //return;
  //---------------------------- Implementación de DFS, así quedará en el STACK
  // anexar nodo inicial
  Stack_n.push_front(s);
  // hasta alcanzar la profundidad deseada, o hasta que no haya más nodos

  //for (int l = 0; l < 11; l++){
  while(n_depth < k && !Stack_n.empty()){
    // tomar ese elemento del stack, sin eliminarlo, y anexar un nodo adyacente no visitado antes
    // nodo más externo del stack
    ext_node = Stack_n.front();
    cout << "Tamanio Stack: "<< Stack_n.size()<< endl;
    add_node = false;
    // barrido sobre todos sus nodos adyacentes en reversal
    for (auto const &w : reversal[ext_node]){
      // si uno de sus nodos adyacentes no había sido descubierto, que lo anexe al stack
      if (Discovered[w] != true){
        Discovered[w] = true;
        Stack_n.push_front(w);
        n_depth++;
        add_node = true;
        cout << "*** UN NODO ANEXADO ***" << endl;
        cout << "profundidad: " << n_depth<< endl;
        break;
      }
    }
    // si para ese elemento tomado del stack no se agregó otro, entonces se elimina del stack y decrece la profundidad
    // n_depth = Stack_n.size()
    cout << "nodo anexado?? " << add_node << endl;
    if (!add_node){
      cout << "*** NINGUN NODO AGREGADO :c ***" << endl;
      // recupera el path más largo encontrado hasta ese momento
      if (longest_path.size() < Stack_n.size()){
        longest_path.clear();
        longest_path = Stack_n;
      }
      n_depth--;
      Stack_n.pop_front();
      add_node = false;
    }
  }


  ofstream inv_path_file;
  inv_path_file.open("nodes_inv_path.txt");
  // una vez terminado el ciclo hay dos opciones: stack vacío o con la respuesta
  // si el stack queda vacío, entonces tomamos longest_path
  if (Stack_n.empty()) {
    cout << "Longest Path: ";
    for (auto const &w : longest_path){
      cout << w << " -> ";
      inv_path_file << w << " ";
    }
  }
  else {
    cout << "Stack: ";
    for (auto const &w : Stack_n){
      cout << w << " -> ";
      inv_path_file << w << " ";
    }
  }
  inv_path_file.close();
  cout << endl;
}

/*
1 -
 -> USAR BFS
 -> analizar la independencia de cada layer "potencial"
    -> usar la matriz de adyacencia para cada layer potencial
       e ir descartando nodos hasta que quede una matriz vacía

 ------------------------- O -----------------

2 -
 -> USAR DFS
 -> analizar la independencia de cada nodo potencial
   -> ver si este nodo potencial no es nodo adyacente de algún
      nodo independiente o si un nodo adyacente al nodo potencial
      es independiente
 ---------------- WINNER--------
 1
 con el layer potencial ya tenemos una idea de la relacion entre los nodos

 en el caso de nodos potenciales, debemos de correr todo el grafito
*/

void Graph::ind_set(int root, int k){
  // u -> source
  // v -> destiny
  // i -> lindependent set elements number
  int u, v, i = 1;
  bool to_delete = false;
  // Nodos descubiertos
  int Discovered[numNodes];
  // listas de los nodos en layers y de los elementos adyacentes a un nodo
  // L_npot -> nodos no potenciales
  // L_pot -> nodos potenciales
  // L_ind -> nodos independientes
  list<int> L_curr, L_npot, L_pot, L_ind, u_edges;

  Discovered[root] = 1;

  L_ind.push_back(root);
  // queue
  L_curr.push_back(root);

  // archivo con todos los edges
  ofstream edges_graph_file;
  edges_graph_file.open("edges_graph.csv");
  edges_graph_file << "from,to\n";

  // siempre que no se haya alcanzado el número deseado de elementos
  // y que haya material de donde agarrar nuevos nodos
  // i.e. !L_curr.empty() o !L_npot.empty()
  while ((i < k)&& (!L_curr.empty() || !L_npot.empty())) {

    // corremos sobre todos los elementos para encontrar los vecinos

    while(!L_curr.empty()){
      // popeamos el siguiente elemento del queue u
      u = L_curr.front();
      L_curr.pop_front();
      cout << u << endl;
      // tomamos la lista de adyacencia de u
      u_edges = adjList[u];
      // analizamos los nodos adyacentes a u
      while (!u_edges.empty()) {
        v = u_edges.front();
        u_edges.pop_front();

        //agregado del edge
        edges_graph_file << u << "," << v <<"\n";

        if (Discovered[v] != 1){
          Discovered[v] = 1;
          L_npot.push_back(v);
        }
      }
    }



    while (!L_npot.empty()){
      // popeamos el siguiente elemento del queue u
      u = L_npot.front();
      L_npot.pop_front();
      //cout << u << endl;
      // tomamos la lista de adyacencia de u
      u_edges = adjList[u];
      // analizamos los nodos adyacentes a u
      while (!u_edges.empty()) {
        v = u_edges.front();
        u_edges.pop_front();

        //agregado del edge
        edges_graph_file << u << "," << v <<"\n";

        if (Discovered[v] != 1){
          Discovered[v] = 1;
          L_pot.push_back(v);
        }
      }
    }
    cout << "\n---   POTENCIALES   ---\n";
    while (!L_pot.empty()) {
    //for (auto const &u : L_pot){
      // ciclo se rompe si ya se ha alcanzado el número de elementos buscados
      if (i >= k ) break;

      u = L_pot.front();
      //L_pot.pop_front();

      u_edges = adjList[u];

      // análisis de independencia de los nodos en el layer
      // i.e. no haya edges en el layer potencial
      // en caso de haber, eliminamos un nodin y se pasa a los no potenciales
      while (!u_edges.empty()) {
        v = u_edges.front();
        u_edges.pop_front();

        //agregado del edge
        edges_graph_file << u << "," << v <<"\n";

        // barrido sobre los nodos potenciales para encontrar elementos que tengan elementos comúnes
        for (auto const &w : L_pot){
          cout << "pot_layer:\t" << v <<"\t" <<  w << endl;
          // si algún elemento adyacente coincide con un miembro de los potenciales
          if (w == v){
            // se debe eliminar algúno de los dos, en este caso eliminamos el u
            cout << u <<" DELETED****"<< endl;
            to_delete = true;
            //break;
          }
        }

        // barrido sobre los nodos potenciales para encontrar elementos que tengan elementos comúnes
        for (auto const &w : L_ind){
          cout << "pot_layer:\t" << v <<"\t" <<  w << endl;
          // si algún elemento adyacente coincide con un miembro de los potenciales
          if (w == v){
            // se debe eliminar algúno de los dos, en este caso eliminamos el u
            cout << u <<" DELETED****"<< endl;
            to_delete = true;
            //break;
          }
        }

      }
      cout <<"---- end"<< endl;
      L_pot.pop_front();

      // si hay algún edge que conecte a dos nodos del layer potencial
      // anexamos el u a los no potenciales y lo eliminamos de los potenciales
      if (to_delete){
        L_npot.push_back(u);
        // regresamos la variable a su valor original
        to_delete = false;
      }
      // si no se debe eliminar
      else {
        if (i < k) {
          L_curr.push_back(u);
          L_ind.push_back(u);
          cout << u << endl;
          // incrementa el número de nodos en el independent set
          i++;
        }
        // si se ha alcanzado la igualdad ya no tiene caso seguir
        // break rompe el ciclo u_edges.empty()
        else break;
      }
    }
    // liberación de la memoria, eliminación de los datos almacenados
    L_pot.clear();
  }

  // archivo con los nodos independientes
  ofstream ind_set_file;
  ind_set_file.open("ind_set.txt");

  cout << "------------   CONJUNTO INDEPENDIENTE  -----------" << endl;
  for (auto const &w : L_ind){
    cout << w << " ";
    ind_set_file << w << " ";
  }
  ind_set_file.close();

  edges_graph_file.close();
}

int main(int argc, char* argv[]){
  if (argc != 3) return -1;
  int node_u = atof(argv[1]);
  int int_k = atof(argv[2]);
  string n1, n2;
  int src, dest, max_edges = 0, tst_edges, node_mx_edges;
  Graph g(600000);

  ifstream test("TWITTER-Real-Graph-Partial.edges");
  while (test.good()){
    getline(test, n1, ','); // delimitador es un caracter
    getline(test, n2, '\n');
    if (n1 == "") break;   // n1 es un string
    src = stoi(n1);
    dest = stoi(n2);
    g.addEdge(src,dest);
    tst_edges = g.adjList[src].size();
    if (max_edges < tst_edges) {
      max_edges = tst_edges;
      node_mx_edges = src;
    }
  }
  cout << "**** NODE WITH HIGHEST GRADE:\t" << node_mx_edges << endl;
  test.close();

  g.k_hops(node_u, int_k);
  g.inv_path(node_u, int_k);
  g.ind_set(node_u, int_k);
  return 0;
}
