# Music Playlist Manager
# Using Doubly Linked List


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None


class MusicPlaylist:

    def __init__(self):
        self.head = None
        self.current = None

    # Add a song
    def add_song(self, title, artist):
        new_song = Song(title, artist)

        if self.head is None:
            self.head = new_song
            self.current = new_song
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_song
            new_song.prev = temp

        print("\nSong added successfully!")

    # Display playlist
    def display_playlist(self):

        if self.head is None:
            print("\nPlaylist is empty.")
            return

        temp = self.head

        print("\n====== YOUR PLAYLIST ======")

        while temp is not None:

            if temp == self.current:
                print(f"▶ {temp.title} - {temp.artist}")
            else:
                print(f"  {temp.title} - {temp.artist}")

            temp = temp.next

    # Play current song
    def play_current(self):

        if self.current is None:
            print("\nPlaylist is empty.")
        else:
            print(
                f"\nNow Playing: "
                f"{self.current.title} - {self.current.artist}"
            )

    # Next song
    def next_song(self):

        if self.current is None:
            print("\nPlaylist is empty.")

        elif self.current.next is None:
            print("\nThere is no next song.")

        else:
            self.current = self.current.next
            self.play_current()

    # Previous song
    def previous_song(self):

        if self.current is None:
            print("\nPlaylist is empty.")

        elif self.current.prev is None:
            print("\nThere is no previous song.")

        else:
            self.current = self.current.prev
            self.play_current()

    # Search song
    def search_song(self, title):

        temp = self.head

        while temp is not None:

            if temp.title.lower() == title.lower():

                print("\nSong Found!")
                print("Title :", temp.title)
                print("Artist:", temp.artist)

                return

            temp = temp.next

        print("\nSong not found.")

    # Delete song
    def delete_song(self, title):

        temp = self.head

        while temp is not None:

            if temp.title.lower() == title.lower():

                if temp.prev is None:
                    self.head = temp.next
                else:
                    temp.prev.next = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                if self.current == temp:

                    if temp.next is not None:
                        self.current = temp.next
                    else:
                        self.current = temp.prev

                print("\nSong deleted successfully!")
                return

            temp = temp.next

        print("\nSong not found.")


# =================================
# MAIN PROGRAM
# =================================

playlist = MusicPlaylist()

while True:

    print("\n==============================")
    print("      MUSIC PLAYLIST")
    print("==============================")

    print("1. Add Song")
    print("2. Display Playlist")
    print("3. Play Current Song")
    print("4. Next Song")
    print("5. Previous Song")
    print("6. Search Song")
    print("7. Delete Song")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        title = input("Enter song title: ")
        artist = input("Enter artist name: ")

        playlist.add_song(title, artist)

    elif choice == "2":

        playlist.display_playlist()

    elif choice == "3":

        playlist.play_current()

    elif choice == "4":

        playlist.next_song()

    elif choice == "5":

        playlist.previous_song()

    elif choice == "6":

        title = input("Enter song title to search: ")
        playlist.search_song(title)

    elif choice == "7":

        title = input("Enter song title to delete: ")
        playlist.delete_song(title)

    elif choice == "8":

        print("\nThank you for using Music Playlist Manager!")
        break

    else:

        print("\nInvalid choice! Please try again.")
