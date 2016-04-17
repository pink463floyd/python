A--B--C
\  \
 D--E--F
A'--B'--C'
\   \
 D'--E'--F'
Node
|- int64_t value
|- Collection<Node*> neighbors
given node N in graph G, return N and the veties directly connected to N






typedef struct node{
  UINT64 value;
  struct node *p;
} NODE;
typedef struct node{
  UINT64 value;
  //struct node *p;
   struct node[X];
   int count;
} NODE;
NODE *foo(NODE *b)
 NODE *tmp;
 NODE *tmp2 = NULL;
 NODE *tmp3 = malloc(sizeof(NODE);
 for (int i=0; i<b->count;i++)
 {
    tmp = malloc(sizeof(NODE));
    tmp->value = b->value;
    tmp->count = 0;
    tmp2 = tmp;
 }
   
foo(Graph G, node n)
{
  return each far vertex that is connected to N.
}
B -> A, C, E; create B' (and populate B'.neighbors.addall(A', C', E'))
A -> B, D; create A'
D -> A, E; create D'
E -> B, D, F; create E'
F -> E; create F'
C -> B; create C'
return B'
B' -> A', C', E'
A' -> B', D'
Node B;
Node* B_prime = copy(&B);
assert_equal(B_prime->neighbors, [A_prime, C_prime, E_prime])
typedef struct node{
  UINT64 value;
  //struct node *p;
   struct node[X];
   int count;
} NODE;
int visited[X];
int processed[X];
NODE *copy(NODE *p)
{
//Init visited and processed to zero
p_prime = malloc(sizeof(NODE));
for (i=0;i<p->count;i++)
{
  visited[p->value] = 1;
  add_queue(p->node[count]);
  bind contents of p->node with p’
  p_prime->node[i].value = p->node[value];
}
if queue not empty
  x = dequeue
  copy(x);
  processed[x->value] = 1;
}
B' -> A', C', E'
A -> B, D; create A'
Hi Liz:
I won’t be able to work on this until later tonight, but I have a version that is close. Tonight I will do some desk checking on it, but wanted to capture my current work. Thanks for the extension!
#define MAX 1024 //Assume this number is big enough.  I would never be this casual in ‘production’
NODE *copy_node(NODE *p)
{
  NODE *p_prime = malloc(sizeof(NODE));
  p_prime->count = 0;
  p_prime->value = p->value;
}
NODE *establish_edge(NODE *a, NODE *b)
{
  a->node[a->count] = b;
  a->count++;
}
NODE *copy(NODE *p)
{
  NODE *visited[MAX];
  NODE *prime_table[MAX]; //Pointers to the deep copies
  queue q = init_queue();
  NODE *p_prime_root = NULL;
  NODE *prime = NULL;
  for (int init_count = 0;init_count<MAX; init_count++) {
    visited[init_count] = 0;
  }
  add_queue(q,p); //FIFO queue
  while (queue_not_empty(q))
  {
     NODE *p2 = read_queue(q);
     if (visited[p2->value] != 0) {
         visited[p2->value] = 1;
         prime = copy_node(p2);
     else
         prime = prime_table[p2->value];
     if (p_prime_root == NULL) {
         p_prime_root = prime);
     }
     for (int i=0;i<p2->count;i++) {
        if (visited[p2->node[i].value] == 0) {
            add_queue(q, p2->node[i]);
            x = copy_node(p2->node[i]);
            prime_table[p2->node[i].value] = x;
            visited[p2->node[i].value] = 1;
        } else {
            x = visited[p2->node[i].value];
        }
        
        establish_edge(prime, x);
     }
  }
  return p_prime_root;
}
Hi Liz: 9:41 pm Friday night. This was fun, thanks for taking the time to meet with me today. My final submission is below. From the one above fixed a few small logic errors and cleaned up one of the variable names. Take care. Scott
#define MAX 1024 //Assume this number is big enough
NODE *copy_node(NODE *p)
{
  NODE *p_prime = malloc(sizeof(NODE));
  p_prime->count = 0;
  p_prime->value = p->value;
  return p_prime;
}
NODE *establish_edge(NODE *a, NODE *b)
{
  a->node[a->count] = b;
  a->count++;
}
NODE *copy(NODE *p)
{
  NODE *visited[MAX];
  NODE *prime_table[MAX]; //Pointers to the deep copies
  queue *q = init_queue(); //FIFO Queue
  NODE *p_prime_root = NULL;
  NODE *prime = NULL;
  NODE *far_end; //Vertex at other end of edge
  for (int init_count = 0;init_count<MAX; init_count++) {
    visited[init_count] = (NODE *)0;
    prime_table[init_count] = (NODE *)0;
  }
  add_queue(q,p); //FIFO queue
  while (queue_not_empty(q))
  {
     NODE *p2 = read_queue(q);
     if (visited[p2->value] == 0) {
         visited[p2->value] = 1;
         prime = copy_node(p2);
         prime_table[p2->value] = prime;
     } else {
         prime = prime_table[p2->value];
     }
     if (p_prime_root == NULL) {
         p_prime_root = prime);
     }
     for (int i=0;i<p2->count;i++) {
        if (visited[p2->node[i].value] == 0) {
            add_queue(q, p2->node[i]);
            far_end = copy_node(p2->node[i]);
            prime_table[p2->node[i].value] = far_end;
            visited[p2->node[i].value] = 1;
        } else {
            far_end = prime_table[p2->node[i].value];
        }
        
        establish_edge(prime, far_end);
     }
  }
  return p_prime_root;
}
