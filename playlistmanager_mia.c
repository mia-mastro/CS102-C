#include <stdio.h>
#include <string.h>

#define MAX_SONGS 100

struct Song {
	char title[MAX_SONGS];
	char artist[MAX_SONGS];
	int duration;
};

struct Song playlist[MAX_SONGS];
int totalSongs = 0;
int currentlyPlaying = 0;

int durationMin(int seconds) {
	return seconds / 60;
}

int durationSec(int seconds) {
	return seconds % 60;
}

void addSong(char *pTitle, char *pArtist, int pDuration) {
	if (totalSongs >= MAX_SONGS) {
		printf("Playlist is full!\n");
		return;
	}
	strcpy(playlist[totalSongs].title, pTitle);
	strcpy(playlist[totalSongs].artist, pArtist);
	playlist[totalSongs].duration = pDuration;
	totalSongs++;
}

void removeSong(char *pTitle) {
	if (totalSongs == 0) {
		printf("Playlist is empty!\n");
		return;
	for (int i = 0; i < totalSongs; i++) {
		if (strcmp(playlist[i].title, pTitle) == 0) {
			for (int j = i; j < totalSongs - 1; j++) {
				playlist[j] = playlist[j + 1];
			}
			totalSongs--;
			if (currentlyPlaying >= totalSongs) {
				currentlyPlaying = totalSongs - 1;
			}
			if (currentlyPlaying < 0) {
				currentlyPlaying = 0;
			}
			return;
			}
		}
	printf("Song not found!\n");
	}
}

void nextSong() {
	if (totalSongs == 0) {
		printf("Playlist is empty!\n");
		return;
	}
	if (currentlyPlaying < totalSongs - 1) {
		currentlyPlaying++;
	} else {
		currentlyPlaying = 0;
	}
}

void previousSong() {
	if (totalSongs == 0) {
		printf("Playlist is empty!\n");
		return;
	}
	if (currentlyPlaying > 0) {
		currentlyPlaying--;
	} else {
		currentlyPlaying = totalSongs - 1;
	}
}

void currentPrint() {
	if (totalSongs == 0) {
		printf("Playlist is empty!\n");
		return;
	}
	struct Song s = playlist[currentlyPlaying];
	printf("Now playing: \"%s\" by %s (%d:%02d)\n", s.title, s.artist, durationMin(s.duration), durationSec(s.duration));
}

void listPrint() {
	if (totalSongs == 0) {
		printf("Playlist is empty!\n");
		return;
	}
	printf("\n-----PLAYLIST-----\n");
	for (int i = 0; i < totalSongs; i++) {
		if (i == currentlyPlaying) {
			printf("[->] %d. \"%s\" by %s (%d:%02d)\n", i + 1, playlist[i].title, playlist[i].artist, durationMin(playlist[i].duration), durationSec(playlist[i].duration));
		} else {
			printf("%d. \"%s\" by %s (%d:%02d)\n", i + 1, playlist[i].title, playlist[i].artist, durationMin(playlist[i].duration), durationSec(playlist[i].duration));
		}
	}
	printf("-----------------\n");
}

int main() {
	char command[50];
	char title[100];
	char artist[100];
	int duration;

	printf("~~~ Playlist Manager ~~~\n");
	printf("Commands: add, remove, next, prev, current, list, quit\n");

	while (1) {
		printf("\n> ");
		scanf("%s", command);

		if (strcmp(command, "add") == 0) {
			printf("Enter song title: ");
			scanf(" %[^\n]", title);
			printf("Enter artist name: ");
			scanf(" %[^\n]", artist);
			printf("Enter duration (in seconds): ");
			scanf("%d", &duration);
			addSong(title, artist, duration);
			printf("Added: \"%s\" by %s (%d:%02d)\n", title, artist, durationMin(duration), durationSec(duration));
		} else if (strcmp(command, "remove") == 0) {
			printf("Enter song title: ");
			scanf(" %[^\n]", title);
			removeSong(title);
			printf("Removed: \"%s\" by %s (%d:%02d)\n", title, artist, durationMin(duration), durationSec(duration));
		} else if (strcmp(command, "next") == 0) {
			nextSong();
			currentPrint();
		} else if (strcmp(command, "prev") == 0) {
			previousSong();
			currentPrint();
		} else if (strcmp(command, "current") == 0) {
			currentPrint();
		} else if (strcmp(command, "list") == 0) {
			listPrint();
		} else if (strcmp(command, "quit") == 0) {
			printf("Thanks for using the playlist manager!\n");
			break;
		} else {
			printf("Unrecognized command entered\n");
		}
	}
	return 0;
}

