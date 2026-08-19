/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> nodes;
        nodes[NULL] = NULL;
        Node* curr = head;
        while (curr) {
            Node* copy = new Node(curr->val);
            nodes[curr] = copy;
            curr = curr->next;
        }

        curr = head;
        Node* copy = new Node(0);
        Node* curr2 = copy;

        while (curr) {
            nodes[curr]->next = nodes[curr->next];
            nodes[curr]->random = nodes[curr->random];
            curr2->next = nodes[curr];
            curr = curr->next;
            curr2 = curr2->next;
        }

        return copy->next;
    }
};
