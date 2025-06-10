# 멤버십 적립 함수
def handle_membership():
    global last_membership
    while True:
            member = input("멤버십을 적립하시겠습니까? (yes/no): ").strip().lower()
            if member not in ['yes', 'no']:
                print("yes 또는 no만 입력해주세요.")
                continue

            if member == 'no':
                print("멤버십 적립을 건너뜁니다.\n")
                last_membership = False
                break

            print("멤버십 적립을 선택하셨습니다.")

            while True:
                member_ship = input("전화 번호를 11자리를 입력하세요: ").strip()
                last_membership = member_ship

                # 유효성 검사(11자리 여부, 숫자 여부)
                if len(member_ship) != 11 or not member_ship.isdigit():
                    print("전화번호가 올바르지 않습니다. 11자리 숫자만 입력해주세요.")
                    continue

                # 포인트 적립
                if member_ship in membership_dict:
                    # 기존 회원: 1포인트 추가
                    membership_dict[member_ship] += 1
                    print(f"기존 ({member_ship}) 번호로 포인트를 적립했습니다. 적립 포인트: {membership_dict[member_ship]} Point\n")
                else:
                    # 신규 회원: 포인트 1점으로 초기화
                    membership_dict[member_ship] = 1
                    print(f"새로운 ({member_ship}) 번호로 멤버십이 생성되었습니다. 적립 포인트: {membership_dict[member_ship]} Point\n")

                return