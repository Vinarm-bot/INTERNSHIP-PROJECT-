# AI Recommendation System

recommendations = {
    "coding": [
        "Python Programming",
        "Java Programming",
        "Web Development",
        "Data Structures"
    ],
    "music": [
        "Spotify",
        "YouTube Music",
        "Guitar Lessons",
        "Piano Course"
    ],
    "movies": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "3 Idiots"
    ],
    "sports": [
        "Football",
        "Cricket",
        "Badminton",
        "Chess"
    ],
    "books": [
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich"
    ],
    "fitness": [
        "Morning Yoga",
        "Home Workout",
        "Running",
        "Healthy Diet Plan"
    ]
}

print("===== AI Recommendation System =====")
print("Available Interests:")
print("Coding, Music, Movies, Sports, Books, Fitness\n")

interest = input("Enter your interest: ").lower()

if interest in recommendations:
    print("\nRecommended for you:")
    for item in recommendations[interest]:
        print("-", item)
else:
    print("\nSorry! No recommendations found for this interest.")