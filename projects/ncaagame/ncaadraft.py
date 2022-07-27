"""Randomly pick college teams."""

from random import randint, uniform

firstname: list[str] = ["John", "Brady", "Caleb", "Leroy", "DeAndre", "Demar", "Luka", "Armando", "George", "RJ", "Jalen", "DJ", "Derrick", "Erik", "Daniel", "Tom", "Michael", "Russell", "Chris", "Kevin", "Dwayne", "Kyrie", "Damian", "Karl", "Carmelo", "Steve", "Jack", "Alejandro", "Bill", "Hubert", "Mike", "Steph", "Jalen", "Miles", "Devin", "TJ", "AJ", "CJ", "Bud", "Giovanni", "Stefano", "Marco", "Jeremy", "Yao", "Mohamed", "Ibrahim", "Ahmed", "Cho", "Juan", "Carlos", "Luis", "Brook", "Kemba", "Tyler", "Ty", "Al", "Anthony", "Burton", "Cameron", "Cory", "Clark", "Hugo", "Cole", "Reggie", "Grayson", "DeMarcus", "Bruno", "Denis", "Mario", "Ben", "Shawn", "Raymond", "Frank", "Rechon", "Malik", "Jake", "Mo", "Dwight", "Draymond", "Aaron", "Trevor", "Charlie", "Gary", "Jimmy"]
lastname: list[str] = ["Jefferson", "Brady", "Brown", "Smith", "Williams", "DeRozan", "James", "Bacot", "Jordan", "Davis", "Lee", "Murray", "Allen", "Anthony", "Paul", "Irving", "Doncic", "Wade", "Jones", "Curry", "Johnson", "Durant", "Nash", "Thomas", "Ball", "Pierce", "Black", "White", "Villanueva", "Walton", "McCoy", "MacIntosh", "Austin", "Young", "Bridges", "Silva", "Morris", "Morrison", "Santos", "Romano", "Russo", "Bianco", "Lin", "Ming", "Ali", "Adebayo", "Mensah", "Chen", "Garcia", "Lopez", "Gonzalez", "Sanchez", "Adams", "Robinson", "Walker", "Harris", "Guster", "Lewis", "Payne", "Knight", "Green", "Jenkins", "Carter", "Miller", "Bush", "Cousins", "Jokic", "Morant", "Wilkins", "Chamberlain", "Love", "Jin", "Cosby", "Howard", "Gardner", "Fox", "Ward", "Hart", "Butler"]
colleges: list[str] = ["Gonzaga", "Georgia St", "Boise St", "Memphis", "Uconn", "New Mexico St", "Arkansas", "Vermont", "Alabama", "Notre Dame", "Texas Tech", "Montana St", "Michigan St", "Davidson", "Duke", "CSU Fullerton", "Baylor", "Norfolk St", "North Carolina", "Marquette", "Saint Mary's", "Indiana", "UCLA", "Texas", "Virginia Tech", "Purdue", "Yale", "Murray St", "San Francisco", "Kentucky", "Saint Peter's", "Arizona", "Wichita St", "Seton Hall", "TCU", "Houston", "Oregon", "Illinois", "Xavier", "Colorado St", "Michigan", "Tennessee", "Syracuse", "Ohio State", "Loyola Chicago", "Villanova", "Delaware", "Kansas", "Davidson", "San Diego St", "Creighton", "Iowa", "Richmond", "Providence", "S Dakota St", "LSU", "Iowa St", "Wisconsin", "Colgate", "USC", "Miami", "Auburn", "Louisville", "Boston College"]

i: int = randint(0, 63)
t: str = colleges[i]
print(t)
print(len(firstname))
print(len(lastname))
print(round(uniform(0.2, 1.0), 1))