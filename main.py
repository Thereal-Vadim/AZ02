import pandas as pd
import numpy as np

data = {
    'Имя': ['Иван', 'Мария', 'Петр', 'Анна', 'Алексей',
            'Елена', 'Дмитрий', 'Ольга', 'Сергей', 'Наталья'],
    'Математика': [4, 5, 3, 5, 4,
                   3, 5, 4, 3, 5],
    'Русский язык': [5, 4, 4, 5, 3,
                     4, 4, 5, 4, 5],
    'Физика': [3, 5, 4, 4, 5,
               3, 4, 3, 5, 4],
    'История': [4, 5, 3, 5, 4,
                4, 5, 3, 4, 5],
    'Английский': [5, 4, 4, 3, 5,
                   4, 3, 5, 4, 4]
}

df = pd.DataFrame(data)

print("Первые строки DataFrame:")
print(df.head())

print("\nСредние оценки по предметам:")
print(df.mean(numeric_only=True))

print("\nМедианные оценки по предметам:")
print(df.median(numeric_only=True))

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nДля математики:")
print(f"Q1: {Q1_math}")
print(f"Q3: {Q3_math}")
print(f"IQR: {IQR_math}")

print("\nСтандартное отклонение по предметам:")
print(df.std(numeric_only=True))