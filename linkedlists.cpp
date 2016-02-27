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


ListNode* Solution::deleteDuplicates(ListNode* A) {
	ListNode *temp,*prev;
	unordered_map<int, int> m;
	temp = A;
	prev = NULL;
	while(temp!=NULL) {
		if(m.find(temp->val) != m.end()) {
			m[temp->val]++;
		}
		else {
			m[temp->val] = 1;
		}
		temp = temp->next;
	}
	ListNode *head = NULL;
	ListNode *temp2;
	temp = A;
	while(temp!=NULL) {
		if(m[temp->val] == 1) {
			if(head == NULL) {
				temp2 = (ListNode *)malloc(1*sizeof(ListNode));
				temp2->val = temp->val;
				temp2->next = NULL;
				head = temp2;
			}
			else {
				temp2->next = (ListNode *)malloc(1*sizeof(ListNode));
				temp2->next->val = temp->val;
				temp2 = temp2->next;
				temp2->next = NULL;
			}
		}
		temp = temp->next;
	}
	return head;
}


int main() {
	return 0;
}