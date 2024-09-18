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

    // Worst Fit memory allocation
    bool allocate(int processSize) {
        if (!head) return false;  // No free blocks available
        
        Node* current = head;
        Node* worst_block = nullptr;

        // Traverse the free list to find the worst fit block (largest block)
        while (current) {
            if (current->size >= processSize) {
                // If worst_block is null or current block is a larger fit
                if (!worst_block || current->size > worst_block->size) {
                    worst_block = current;
                }
            }
            current = current->next;
        }

        // If a worst fit block is found
        if (worst_block) {
            worst_block->size -= processSize;

            // Remove the block if fully allocated
            if (worst_block->size == 0) {
                removeBlock(worst_block);
            }

            return true;  // Allocation successful
        }

        return false;  // Allocation failed (no suitable block found)
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

    cout << "Enter number of free memory blocks: ";
    cin >> num_blocks;

    cout << "Enter value of each free memory block: " << endl;
    for (int i = 0; i < num_blocks; i++) {
        cin >> x;
        freeList.addBlock(x);
    }

    // Allocate memory for a process
    int processSize;

    cout << "Enter the process size: ";
    cin >> processSize;

    cout << endl << "Initial Free List: " << endl;
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
