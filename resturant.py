import os
import datetime as dt




os.system('cls')
menu = ['pizza:10','burger:5','hotdog:3','soda:1']
recipte = []#لیست غذا های انتخاب شده
quantity_list = []# لیست مقدار انتخاب شده
total_price_list =[]# لیست قیمت خرید کل
def price(food):
	'''this function calculates the price of the item in the menu'''
	for item in menu:
		if food == item.split(':')[0]:
			food_price = item.split(':')[1]
			return int(food_price)
def is_in_menu(food):
	'''this function returns true if the selected item is in the menu'''
	count = 0
	while count != len(menu):
		for item in menu:
			if food == item.split(':')[0]:
				return True
		count += 1
def is_in_recipte(food):
	'''this function returns true if the selected food is already selected '''
	count = 0
	while count != len(recipte):
		for item in recipte:
			if food == item:
				return True
			count += 1		
time1 = dt.datetime.now().second
# شروع برنامه
while True:
	print('==== welcome to K.S.P (karim sag paz) resturant ====')
	print('menu')
	print('_'*25)
	for item in menu:
		print(item.split(':')[0] + ' ' +item.split(':')[1] + '$')
		print('_'*25)
	select = input('please choose your food : ')
	if is_in_menu(select.lower()):
		recipte.append(select)
		quantity = input('please tell us how many food you want : ')
		if quantity.isdigit():
			quantity_list.append(quantity)
			total_price_list.append(int(price(select))*int(quantity))
			continue_order = input('do you want to order another food ? (yes/no) ')
			#قسمت آخر برنامه
			if continue_order.lower() == 'no':
				total_price = sum(total_price_list)
				#شرط مینیمم قیمت خرید
				if total_price >= 50 :
					time2 = dt.datetime.now().second
					os.system('cls')
					print('  ===== recipte =====')
					print('thank you for your order')
					print('='*25)
					print('foods')
					print(*recipte)
					print('='*25)
					print('quantity')
					print(*quantity_list)
					print('='*25)
					print('waiting time : '+str(time2-time1)+' seconds')
					print('='*25)
					print('tax')
					print(str(total_price*9/100)+'$')
					print('='*25)
					print('total price')
					# قیمت کل با احتساب مالیات
					print(str(total_price+9/100*total_price)+'$')
					print('='*25)
					print('enjoy your meal')
					print('='*25)
					break
				else:
					print('your item added to your list\nbut you must buy at least 50$ of food')
					print(f'you need to buy {50-total_price}$ of more food')
			elif continue_order.lower() == 'yes':
				pass
			else:
				print('sorry I do not understand what you are saying')
		else:
			print('please enter a digit as quantity')
	else:
		print('please choose your food from the menu')
	os.system('cls')