
#making a dictionary of shows for content based filtering
shows = {
    'Breaking Bad': {'Genres': ['crime', 'drama', 'thriller']},
    'Game of Thrones': {'Genres': ['action', 'adventure', 'drama', 'fantasy']},
    'Stranger Things': {'Genres': ['drama', 'fantasy', 'horror', 'mystery', 'sci-fi', 'thriller']},
    'The Office': {'Genres': ['comedy', 'drama']},
    'Friends': {'Genres': ['comedy', 'romance']},
    'The Crown': {'Genres': ['biography', 'drama', 'history']},
    'Black Mirror': {'Genres': ['drama', 'sci-fi', 'thriller']},
    'The Mandalorian': {'Genres': ['action', 'adventure', 'fantasy', 'sci-fi']},
    'The Witcher': {'Genres': ['action', 'adventure', 'drama', 'fantasy', 'mystery']},
    'Money Heist': {'Genres': ['action', 'crime', 'drama', 'mystery', 'thriller']},
    'Naruto': {'Genres': ['action', 'adventure', 'fantasy', 'anime']},
    'Attack on Titan': {'Genres': ['action', 'drama', 'fantasy', 'horror', 'anime']},
    'One Piece': {'Genres': ['action', 'adventure', 'comedy', 'drama', 'fantasy', 'anime']},
    'Death Note': {'Genres': ['mystery', 'psychological', 'supernatural', 'thriller', 'anime']},
    'My Hero Academia': {'Genres': ['action', 'adventure', 'comedy', 'super power', 'anime']},
    'Fullmetal Alchemist: Brotherhood': {'Genres': ['action', 'adventure', 'drama', 'fantasy', 'magic', 'anime']},
    'Demon Slayer: Kimetsu no Yaiba': {'Genres': ['action', 'demons', 'supernatural', 'historical', 'anime']},
    'Dragon Ball Z': {'Genres': ['action', 'adventure', 'fantasy', 'martial arts', 'super power', 'anime']},
    'Hunter x Hunter': {'Genres': ['action', 'adventure', 'fantasy', 'anime']},
    'Sword Art Online': {'Genres': ['action', 'adventure', 'fantasy', 'romance', 'anime']}
}
# User's preferred genre
while True:
    user_preference = input('Enter the Genre of TV Shows you like (or "exit" to quit): ').lower()

    if user_preference == 'exit':
        break
# Find shows with similar genres to user's preference
    recommended_shows = []

    for show, data in shows.items():
        if user_preference in data['Genres']:
            recommended_shows.append(show)

# Display recommended shows
    if recommended_shows:
        print(f"Recommended TV shows of {user_preference} Genre:")
        for show in recommended_shows:
            print(show)
    else:
        print(f"No recommendations found for the genre: {user_preference}")