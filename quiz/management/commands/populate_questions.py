from django.core.management.base import BaseCommand
from quiz.models import Question


class Command(BaseCommand):
    help = 'Populate the database with quiz questions'

    def handle(self, *args, **options):
        # Check if questions already exist
        if Question.objects.exists():
            self.stdout.write(self.style.WARNING('Questions already exist in the database. Skipping population.'))
            return

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
            # Science
            ["What is the chemical symbol for silver?", "Ag", "Au", "Si", "S", "Ag"],
            ["What part of the plant conducts photosynthesis?", "Root", "Stem", "Leaf", "Flower", "Leaf"],
            ["Which gas is most abundant in Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen", "Nitrogen"],
            ["What is H2O commonly known as?", "Hydrogen", "Oxygen", "Water", "Salt", "Water"],
            ["What force pulls objects toward Earth?", "Magnetism", "Friction", "Gravity", "Electricity", "Gravity"],
            # History
            ["Who was known as the Iron Man of India?", "Mahatma Gandhi", "Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel"],
            ["Who was the first Prime Minister of India?", "Rajendra Prasad", "Jawaharlal Nehru", "Indira Gandhi", "Lal Bahadur Shastri", "Jawaharlal Nehru"],
            ["Which war ended in 1945?", "World War I", "World War II", "Cold War", "Vietnam War", "World War II"],
            ["Who discovered America?", "Vasco da Gama", "Christopher Columbus", "Ferdinand Magellan", "James Cook", "Christopher Columbus"],
            ["The Taj Mahal was built by which Mughal emperor?", "Akbar", "Shah Jahan", "Aurangzeb", "Babur", "Shah Jahan"],
            # Geography
            ["Which is the smallest continent?", "Europe", "Australia", "Antarctica", "South America", "Australia"],
            ["Which country has the largest population?", "USA", "India", "China", "Russia", "India"],
            ["Which is the longest river in India?", "Ganga", "Yamuna", "Brahmaputra", "Godavari", "Ganga"],    
            ["Which is the highest mountain in the world?", "K2", "Kangchenjunga", "Everest", "Makalu", "Everest"],
            ["Which ocean lies between Africa and Australia?", "Atlantic", "Pacific", "Indian", "Arctic", "Indian"],
            # Sports
            ["How many players are there in a cricket team?", "9", "10", "11", "12", "11"],
            ["Who is known as the 'God of Cricket'?", "Virat Kohli", "Sachin Tendulkar", "MS Dhoni", "Ricky Ponting", "Sachin Tendulkar"],
            ["Which country hosts Wimbledon?", "USA", "Australia", "UK", "France", "UK"],
            ["In which sport is a shuttlecock used?", "Tennis", "Badminton", "Squash", "Table Tennis", "Badminton"],
            ["How many rings are there in the Olympic symbol?", "4", "5", "6", "7", "5"],
            # Current Affairs & GK
            ["Who is the CEO of Google (as of 2026)?", "Satya Nadella", "Sundar Pichai", "Elon Musk", "Tim Cook", "Sundar Pichai"],
            ["Which country launched the Chandrayaan missions?", "USA", "Russia", "India", "China", "India"],
            ["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Power Unit", "Central Processing Unit"],
            ["Which is the largest democracy in the world?", "USA", "India", "Brazil", "UK", "India"],
            ["What is the currency of Japan?", "Won", "Yuan", "Yen", "Dollar", "Yen"],
            # Miscellaneous
            ["Which bird is known for its colorful feathers?", "Crow", "Peacock", "Sparrow", "Eagle", "Peacock"],
            ["Which organ pumps blood in the human body?", "Lungs", "Brain", "Heart", "Liver", "Heart"],
            ["How many days are there in a leap year?", "365", "366", "364", "360", "366"],
            ["Which shape has three sides?", "Square", "Circle", "Triangle", "Rectangle", "Triangle"],
            ["Which is the largest land animal?", "Elephant", "Lion", "Giraffe", "Rhino", "Elephant"],
            # Additional Mixed Questions
            ["Which planet is closest to the Sun?", "Venus", "Earth", "Mercury", "Mars", "Mercury"],
            ["Which is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", "Tiger"],
            ["Which festival is known as the festival of lights?", "Holi", "Eid", "Diwali", "Christmas", "Diwali"],
            ["Which is the fastest land animal?", "Lion", "Cheetah", "Horse", "Tiger", "Cheetah"],
            ["Which gas is essential for breathing?", "Carbon dioxide", "Oxygen", "Nitrogen", "Helium", "Oxygen"],
            ["Which instrument is used to see distant objects?", "Microscope", "Telescope", "Periscope", "Binocular", "Telescope"],
            ["Which is the tallest animal?", "Elephant", "Giraffe", "Horse", "Camel", "Giraffe"],
            ["Which country is famous for pizza?", "France", "Italy", "USA", "Spain", "Italy"],
            ["Which language is primarily spoken in Brazil?", "Spanish", "Portuguese", "English", "French", "Portuguese"],
            ["Which is the largest planet in our solar system?", "Earth", "Jupiter", "Saturn", "Neptune", "Jupiter"],
            ["Which vitamin is good for eyesight?", "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin K", "Vitamin A"],
            ["Which is the boiling point of water?", "90°C", "100°C", "80°C", "120°C", "100°C"],
            ["Which animal is known as the king of the jungle?", "Tiger", "Lion", "Elephant", "Leopard", "Lion"],
            ["Which direction does the sun rise from?", "West", "North", "East", "South", "East"],
            ["Which is the largest bird?", "Eagle", "Ostrich", "Parrot", "Peacock", "Ostrich"],
            ["Which is the national flower of India?", "Rose", "Lotus", "Lily", "Sunflower", "Lotus"],
            ["Which is the smallest bone in the human body?", "Femur", "Stapes", "Tibia", "Skull", "Stapes"],
            ["Which planet is known for its rings?", "Mars", "Saturn", "Jupiter", "Venus", "Saturn"],
            ["Which metal is used to make wires?", "Copper", "Gold", "Iron", "Silver", "Copper"],
            ["Which is the hardest natural substance?", "Iron", "Gold", "Diamond", "Silver", "Diamond"],
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

        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(questions_data)} questions to the database!'))
