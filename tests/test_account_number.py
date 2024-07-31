from src.masks import get_mask_account

user_account_number = input()
masked_account_number = get_mask_account(user_account_number)
print(masked_account_number)
