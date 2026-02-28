import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizproject.settings')
django.setup()

from quiz.models import Question

questions_data = [
    # Science & Tech
    ["What is the chemical symbol for gold?", "Au", "Ag", "Go", "Gd", "Au"],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", "Mars"],
    ["What gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen", "Carbon dioxide"],
    ["What is the speed of light?", "3 × 10⁸ m/s", "3 × 10⁶ m/s", "3 × 10⁵ km/h", "3 × 10⁷ km/s", "3 × 10⁸ m/s"],
    ["Which vitamin is produced when sunlight falls on the skin?", "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "Vitamin D"],
    # History
    ["Who was the first President of the United States?", "Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams", "George Washington"],
    ["In which year did India gain independence?", "1945", "1947", "1950", "1939", "1947"],
    ["Who invented the telephone?", "Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "James Watt", "Alexander Graham Bell"],
    ["The Great Wall of China was primarily built to protect against which group?", "Mongols", "Huns", "Romans", "Persians", "Mongols"],
    ["Who discovered penicillin?", "Louis Pasteur", "Alexander Fleming", "Marie Curie", "Gregor Mendel", "Alexander Fleming"],
    # Geography
    ["What is the largest ocean on Earth?", "Atlantic", "Pacific", "Indian", "Arctic", "Pacific"],
    ["Mount Everest is located in which country?", "India", "Nepal", "China", "Bhutan", "Nepal"],
    ["Which river is the longest in the world?", "Nile", "Amazon", "Yangtze", "Mississippi", "Nile"],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "Canberra"],
    ["Which desert is the largest in the world?", "Sahara", "Gobi", "Kalahari", "Thar", "Sahara"],
    # Sports
    ["How many players are there in a football (soccer) team?", "9", "10", "11", "12", "11"],
    ["Who holds the record for the most Olympic gold medals?", "Usain Bolt", "Michael Phelps", "Carl Lewis", "Mark Spitz", "Michael Phelps"],
    ["In which sport is the term 'love' used?", "Cricket", "Tennis", "Football", "Badminton", "Tennis"],
    ["Which country won the FIFA World Cup in 2018?", "Brazil", "Germany", "France", "Argentina", "France"],
    ["The Tour de France is associated with which sport?", "Swimming", "Cycling", "Running", "Football", "Cycling"],
    # Current Affairs & GK
    ["Who is the CEO of Tesla (as of 2026)?", "Jeff Bezos", "Elon Musk", "Tim Cook", "Sundar Pichai", "Elon Musk"],
    ["Which country hosted the 2022 FIFA World Cup?", "Qatar", "UAE", "Russia", "USA", "Qatar"],
    ["The internet was first introduced in which decade?", "1960s", "1970s", "1980s", "1990s", "1970s"],
    ["What is the capital city of Canada?", "Toronto", "Ottawa", "Vancouver", "Montreal", "Ottawa"],
    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", "William Shakespeare"],
    # Miscellaneous
    ["Which animal is known as the 'Ship of the Desert'?", "Horse", "Camel", "Elephant", "Donkey", "Camel"],
    ["Which metal is liquid at room temperature?", "Mercury", "Iron", "Lead", "Gold", "Mercury"],
    ["How many continents are there on Earth?", "5", "6", "7", "8", "7"],
    ["What is the smallest prime number?", "0", "1", "2", "3", "2"],
    ["Which instrument measures atmospheric pressure?", "Thermometer", "Barometer", "Hygrometer", "Anemometer", "Barometer"],
]

for q in questions_data:
    Question.objects.get_or_create(
        question_text=q[0],
        option1=q[1],
        option2=q[2],
        option3=q[3],
        option4=q[4],
        correct_answer=q[5]
    )

print("Successfully added 30 questions to the database!")