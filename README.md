# code-2ndJune-SunnySourav

Here is how to run the code:
<br>
1.Create directory named assesment using command:   mkdir assesment 
<br>
2.Navigate to the directory using the command : cd assesment
<br>
3.Clone the project using command : git clone https://github.com/itssunny322/code-2ndJune-SunnySourav.git
<br>
4.Navigate to the directory where requrements.txt
<br>
5.Create virtual environment using the command:
    ->  python3 -m venv env
<br>
6.Activate virtual environment using the command :
    -> source env/bin/activate
<br>
7.Create database using the command :
    -> mysql -u root -p 
    -> enter password
    -> create database bmi;
<br>
8.Navigate to the directory where manage.py is present

9.Run the server using the command:
    -> python manage.py runserver
    
    
    
    
 Extra:

Logic is in bmiapp/views.py
<br>
 
 Input as mentioned in PDF:
 
 [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]

Output as asked :

[
    {
        "Gender": "Male",
        "HeightCm": 171,
        "WeightKg": 96,
        "bmi": 32.83061454806607,
        "bmiCategory": "Moderately obese",
        "bmiHealthRisk": "Medium risk"
    },
    {
        "Gender": "Male",
        "HeightCm": 161,
        "WeightKg": 85,
        "bmi": 32.79194475521777,
        "bmiCategory": "Moderately obese",
        "bmiHealthRisk": "Medium risk"
    },
    {
        "Gender": "Male",
        "HeightCm": 180,
        "WeightKg": 77,
        "bmi": 23.76543209876543,
        "bmiCategory": "Normal weight",
        "bmiHealthRisk": "Low risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 166,
        "WeightKg": 62,
        "bmi": 22.49963710262738,
        "bmiCategory": "Normal weight",
        "bmiHealthRisk": "Low risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 150,
        "WeightKg": 70,
        "bmi": 31.11111111111111,
        "bmiCategory": "Moderately obese",
        "bmiHealthRisk": "Medium risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 167,
        "WeightKg": 82,
        "bmi": 29.402273297715947,
        "bmiCategory": "Overweight",
        "bmiHealthRisk": "Enhanced risk"
    },
    {
        "overweight_count": 1
    }
]



 
    
    
