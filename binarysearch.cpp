bool isBST(struct node* root)
{
    static struct node *prev = NULL;
    
    // traverse the tree in inorder fashion and keep track of prev node
    if (root)
    {
        if (!isBST(root->left))
          return false;

        // Allows only distinct valued nodes 
        if (prev != NULL && root->data <= prev->data)
          return false;

        prev = root;

        return isBST(root->right);
    }

    return true;
}

int isBinary(struct node* head)
{
    struct node* prev = NULL;
    if (head != NULL)
    {
        if (!isBinary(head->left))
            return 0;
        if (prev != NULL && head->data <= prev->data)
            return 0;
        prev = head;

        return isBinary(head->right);
    }
}