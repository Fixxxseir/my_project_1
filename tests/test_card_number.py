from src.masks import get_mask_card_number

user_card_number = input()
masked_number = get_mask_card_number(user_card_number)
print(masked_number)

