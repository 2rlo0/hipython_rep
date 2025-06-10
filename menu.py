# 메뉴 선택
def menu_choice():
    while True:
        print("\n📋 메뉴판\n")
        for index, name in enumerate(menu_list):
            print(f'{index + 1}. {name}')

        menu_mul = f"\n원하시는 메뉴를 선택해주세요. (1~{len(menu_list)}, 0:처음으로): "
        menu_index = get_valid_number_input(menu_mul, 0, len(menu_list))  # 예외처리

        if menu_index is None:
            continue  # None일 경우 아무 처리 없이 다시 메뉴 선택

        if menu_index == 0:
            print('\n보고싶을거예요😭\n')
            print('-' * 50)
            start()
            return

        if 1 <= menu_index <= len(menu_list):
            cart['user_menu'] = menu_list[menu_index - 1]
            print('-' * 50)
            size_count()
            return


# 수량 선택
def size_count():
    while True:
        print("\n🍨 사이즈 및 가격\n")
        for i, (size, price) in enumerate(size_price.items()):
            print(f'{i + 1}. 사이즈: {size}, 가격: {price:,}원')
        size_mul = f"\n원하시는 사이즈를 선택해주세요. (1~{len(size_price)}, 0:뒤로가기): "
        size_index = get_valid_number_input(size_mul, 0,3 )## 예외처리 (0~3)

        if size_index is None:
            print("⛔입력 오류⛔ 사이즈 다시 선택하세요.")

        elif size_index == 0:
            print('\n⬅️ 뒤로 돌아갑니다')
            print('-' * 50)
            menu_choice()
            return
        elif 1 <= size_index <= len(size_price):
            cart['user_size'] = size_list[size_index - 1]
            break
    while True:
        qty_mul = "🤟 원하시는 개수를 적어주세요. (0:뒤로가기) \n 10개 이하만 가능!: "
        qty = get_valid_number_input(qty_mul, 0, 10) ## 예외처리 (0~10) 성공
        if qty == None:
            continue
        if qty == 0:
            print('\n⬅️ 사이즈 선택으로 돌아갑니다')
            print('-' * 50)
            size_count()
            return
        if qty > 0:
            cart['qty'] = qty
            break
    print('-' * 50)
    cart_function()