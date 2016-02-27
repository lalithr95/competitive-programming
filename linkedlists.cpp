#include <iostream>
#include <algorithm>
using namespace std;

ListNode* reverse(ListNode *A) {
	if (A == NULL) {
		return NULL;
	}
	else {
		ListNode *temp, *prev, *next;
		temp = A;
		prev = NULL;
		while(temp!=NULL) {
			next = temp->next;
			temp->next = prev;
			prev = temp;
			temp = next;
		}
		A = prev;
		return A;
	}
}

int main() {
	return 0;
}