#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//struct for word node with pointers to leftmost and rightmost characters
struct WordNode {
	char word[50];
	struct WordNode *left;
	struct WordNode *right;
};

//create new struct for word
struct WordNode *saveWord(struct WordNode *root, char *word) {
	if (root == NULL) {
		struct WordNode *newNode = malloc(sizeof(struct WordNode));
		strcpy(newNode->word, word);
		newNode->left = newNode->right = NULL;
		return newNode;
	}

	if (strcmp(word, root->word) < 0)
		root->left = saveWord(root->left, word);
	else if (strcmp(word, root->word) > 0)
		root->right = saveWord(root->right, word);

	return root;
}

//is the word in the dictionary?
struct WordNode *findWord(struct WordNode *root, char *word) {
	if (root == NULL)
		return NULL;
	if (strcmp(word, root->word) == 0)
		return root;
	else if (strcmp(word, root->word) < 0)
		return findWord(root->left, word);
	else
		return findWord(root->right, word);
}

int main() {
	struct WordNode *root = NULL;
	char input[50];

	printf("> Loading dictionary...\n");

	char *dictionary[] = {"apple", "banana", "hello", "world", "tree", "restaurant", "porcupine", "paraphernalia", "vacuum", "bologna", "liaison", "pharaoh", "pneumonia"};
	int dictSize = 13;

	for (int i = 0; i < dictSize; i++) {
		root = saveWord(root, dictionary[i]);
	}

	printf("> Loaded %d words: apple, banana, hello, world, tree, restaurant, porcupine, paraphernalia, vacuum, bologna, liaison, pharoah, pneumonia\n", dictSize);

	while (1) {
		printf("\n> Enter a word to check (or 'quit' to exit): ");
		scanf("%49s", input);
		
		if (strcmp(input, "quit") == 0) {
			printf("> Goodbye!\n");
			break;
		}

		if (findWord(root, input))
			printf("> \"%s\" is spelled correctly\n", input);
		else
			printf("> \"%s\" is NOT in the dictionary\n", input);
	}

	return 0;
}
