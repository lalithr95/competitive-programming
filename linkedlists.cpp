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

int Solution::lPalin(ListNode* A) {
	stack	<int> s;
	ListNode *temp = A;
	while(temp!=NULL) {
		s.push(temp->val);
		temp = temp->next;
	}
	temp = A;
	while(temp!=NULL) {
		if(s.top() !=  temp->val) {
			return 0;
		}
		s.pop();
		temp = temp->next;
	}
	return 1;
}

int main() {
	return 0;
}