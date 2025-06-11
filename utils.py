# 유틸리티 함수
# yes or no
def get_yes_or_no_input(msg):
    while True:
        user_input = input('>>>' + msg + " (yes/no): ").strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("⚠️'yes' 또는 'no'만 입력할 수 있어요.")

#숫자검증
def get_valid_number_input(msg, min_no=0, max_no=5):
    try:
        number = int(input('>>>' + msg).strip())
        if number < min_no:
            print(f'⚠️ {min_no} 이상 숫자를 입력하세요.')
            return None
        elif number > max_no:
            print(f'⚠️ {max_no} 이하 숫자를 입력하세요.')
            return None
        else:
            return number
    except ValueError:
        print('⚠️ 숫자로 입력하세요.')
        return None