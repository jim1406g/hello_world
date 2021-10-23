def make_album(author, title, tracks_count=None):
    album = {'author': author, "title": title}
    if tracks_count:
        album['track_count'] = tracks_count
    return album


albums = []

while True:
    album = {}
    print(f"\nВведите данные музыкального альбома (q - выход)")

    author = input("Автор альбома: ")
    if author == 'q':
        break

    title = input("Название альбома: ")
    if title == 'q':
        break

    tracks_count = input("Количество треков (опционально): ")
    if tracks_count == 'q':
        break
    elif tracks_count:
        album = make_album(author, title, tracks_count)
    else:
        album = make_album(author, title)

    albums.append(album)

for album in albums:
    print(album)
