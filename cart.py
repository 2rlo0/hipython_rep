# 장바구니에 추가 및 장바구니 기능 선택
def cart_function():
    item = {
        'user_menu': cart['user_menu'],
        'user_size': cart['user_size'],
        'qty': cart['qty'],
        'price_per_item': size_price[cart['user_size']],
        'total_price': size_price[cart['user_size']] * cart['qty']
    }
    cart_list.append(item)

    print("\n🍦 장바구니에 추가되었습니다! 🍦")
    print_cart()
    print('-' * 50)

    while True:
        cho_mul = "\n1. 계속 쇼핑하기  2. 장바구니 보기 및 결제  3. 장바구니에서 상품 삭제  0. 종료\n선택: "
        choice = get_valid_number_input(cho_mul, 0, 3) ## 예외처리 (0~3)
        if choice == 1:
            menu_choice()
            return
        elif choice == 2:
            show_cart()
            return
        elif choice == 3:
            del_cart()
        elif choice == 0:
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            print('-' * 50)
            start()

# 장바구니 상품 삭제
def del_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        return
    print_cart()
    try:
        idx = int(input("삭제할 상품 번호를 입력하세요 (취소하려면 0 입력): "))
        if idx == 0:
            print("삭제를 취소했습니다.")
            return
        if 1 <= idx <= len(cart_list):
            removed = cart_list.pop(idx - 1)
            print(f"{removed['user_menu']} ({removed['user_size']}) x {removed['qty']}개가 장바구니에서 삭제되었습니다.")
        else:
            print("⛔ 유효한 번호를 입력하세요.")
    except ValueError:
        print("⛔ 숫자를 입력해주세요.")

# 장바구니 보기 및 결제
def show_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        print('-' * 50)
        start()
        return
    print_cart()
    print('-' * 50)

    while True:
        ask_mul = '1. 결제하기  2. 계속 쇼핑하기  0. 종료하기 '
        choice = get_valid_number_input(ask_mul, 0, 2) ## 예외처리 (0~3)
        if choice == 1:
            total = sum(item['total_price'] for item in cart_list)
            print(f"\n총 결제 금액: {total:,}원")

            answer = get_yes_or_no_input("결제하시겠습니까? (yes/no): ") #예외처리 (yes or no)
            if answer not in ['yes', 'no']:
                print("yes 또는 no만 입력해주세요.")
                continue
            elif answer == 'no':
                print("주문이 취소되었습니다.\n")
                return start()

            # 멤버십 적립 처리
            handle_membership()
            print("결제가 완료되었습니다. 감사합니다! 🍦\n")
            print("""⠀
            로딩중~~⠀⠀⠀
            。　 ඞ 。　 . •⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
    ⠀🍨⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀🍦
    ⠀⠀⠀⠀⠤⢀⠀⢸⠛⠋⠘⠛⠃⠙⢻⣿⣿⠀⠀⠀
    ⠀⠀⡌⠀⠀⠀⢣⢸⠀⠘⠀⠀⠘⠀⠀⢁⡹⠀⠀⠀     🍧
    ⠀⠀⠲⡖⠒⠒⡷⠀⡱⠤⣀⣁⣀⠤⠤⡈⠀⠀⠀⠀
    ⠀⠀⠀⠹⡄⡼⡀⣻⡜⠀⠀⠀⢀⠴⠦⢌⡆⠀⠀⠀🍫
    ⠀⠀⠀⠀⠙⠁⠈⠉⣷⣶⣶⣶⣾⣦⣤⠎⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠈⠓⠒⠊⠀⠀⠀⠀⠀
  결제 중입니다 😍
    """)

            time.sleep(3)
            print('=' * 50)


            print("결제가 완료되었습니다. 감사합니다! 🍦\n")
            print_receipt("I Miss You Cram!🍦", cart_list)
            cart_list.clear()
            start()
            return

        elif choice == 2:
            return menu_choice()
        elif choice == 0:
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            start()

# 장바구니 출력
def print_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        return
    print("\n🛒 현재 장바구니:")
    for i, item in enumerate(cart_list, 1):
        print(f"{i}. {item['user_menu']} ({item['user_size']}) x {item['qty']}개 - {item['total_price']:,}원")
    total = sum(item['total_price'] for item in cart_list)
    print(f"총 합계: {total:,}원")
    print('-' * 50)