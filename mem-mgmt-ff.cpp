#include <iostream>
using namespace std;

// Node structure for the doubly linked list
struct Node {
    int size;           // Size of the free memory block
    Node* prev;         // Pointer to the previous node
    Node* next;         // Pointer to the next node

    Node(int s) : size(s), prev(nullptr), next(nullptr) {}
};

// Doubly linked list for free memory blocks
class FreeList {
private:
    Node* head;

public:
    FreeList() : head(nullptr) {}

    // Function to add a block to the free list
    void addBlock(int size) {
        Node* newNode = new Node(size);
        if (!head) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next) {
                temp = temp->next;
            }
            temp->next = newNode;
            newNode->prev = temp;
        }
    }

    // First Fit memory allocation
    bool allocate(int processSize) {
        Node* current = head;
        
        // Traverse the free list
        while (current) {
            if (current->size >= processSize) {
                // Allocate memory
                current->size -= processSize;

                // Remove the block if fully allocated
                if (current->size == 0) {
                    removeBlock(current);
                }
                
                return true; // Allocation successful
            }
            current = current->next;
        }

        return false; // Allocation failed (no suitable block found)
    }

    // Remove block from the list
    void removeBlock(Node* block) {
        if (!block) return;
        
        if (block == head) {
            head = block->next;
            if (head) head->prev = nullptr;
        } else {
            if (block->prev) block->prev->next = block->next;
            if (block->next) block->next->prev = block->prev;
        }
        
        delete block;
    }

    // Display the current state of the free list
    void display() {
        Node* temp = head;
        while (temp) {
            cout << "Block size: " << temp->size << endl;
            temp = temp->next;
        }
    }
};

int main() {
    FreeList freeList;

    // Adding free memory blocks to the list
    int num_blocks;
    int x;

    cout<<"Enter number of free memory blocks: ";
    cin>>num_blocks;

    cout<<"Enter value of each free memory block: "<<endl;
    for(int i=0;i<num_blocks;i++){
        cin>>x;
        freeList.addBlock(x);
    }
    // Allocate memory for a process
    int processSize;

    cout<<"Enter the process size: ";
    cin>>processSize;

    cout << endl<< "Initial Free List: " << endl;
    freeList.display();

    if (freeList.allocate(processSize)) {
        cout << "\nProcess of size " << processSize << " allocated successfully." << endl;
    } else {
        cout << "\nFailed to allocate memory for process of size " << processSize << "." << endl;
    }

    cout << "\nFree List after allocation:" << endl;
    freeList.display();

    return 0;
}
