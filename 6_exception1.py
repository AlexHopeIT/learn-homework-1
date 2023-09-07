"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_sey = input('Как дела? ')
        if user_sey == 'Хорошо':
            print('Пока!')
            break
        
        else: 
            user_sey != 'Хорошо'
            
    
if __name__ == "__main__":
    hello_user()
