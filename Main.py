import psycopg2
def StartGame(Num):



    # Создание таблицы для основной информации по всей игре, заполнение происходит на старте, далее таблица не меняется
    cur.execute(f'''
            	CREATE TABLE IF NOT EXISTS Table{Num} (
                	id SERIAL PRIMARY KEY,
                	Round INTEGER NOT NULL,
                	Inflation INTEGER NOT NULL,
                	Key_Rate INTEGER NOT NULL,
                	The_cost_of_improving_Geometric_Progressions INTEGER NOT NULL,
                	The_cost_of_buying_a_franchise_from_a_bank INTEGER NOT NULL,
                	The_performance_of_the_new_franchise_in_the_Cards INTEGER NOT NULL,
                	Loan_rate_at_the_bank INTEGER NOT NULL,
                	Deposit_to_the_bank INTEGER NOT NULL,
                	The_price_of_buying_Bread_by_the_bank INTEGER NOT NULL,
                	The_price_of_buying_milk_from_a_bank INTEGER NOT NULL,
                    The_price_of_buying_salt_from_the_bank  INTEGER NOT NULL,
                    The_price_of_buying_wheat_from_the_bank  INTEGER NOT NULL,
                    The_price_of_buying_workers_from_the_bank  INTEGER NOT NULL,
                    The_price_of_buying_technologies_from_the_bank  INTEGER NOT NULL,
                    The_sale_price_of_milk_to_the_bank INTEGER NOT NULL,
                    The_sale_price_of_salt_to_the_bank INTEGER NOT NULL,
                    The_sale_price_of_wheat_to_the_bank INTEGER NOT NULL,
                    The_sale_price_of_workers_to_the_bank INTEGER NOT NULL,
                    The_sale_price_of_technologies_to_the_bank INTEGER NOT NULL
                    );
        	''')
    cur.execute(
        f"INSERT INTO Table{Num} (Round, Inflation, Key_Rate, The_cost_of_improving_Geometric_Progressions, The_cost_of_buying_a_franchise_from_a_bank, The_performance_of_the_new_franchise_in_the_Cards, Loan_rate_at_the_bank, Deposit_to_the_bank, The_price_of_buying_Bread_by_the_bank, The_price_of_buying_milk_from_a_bank, The_price_of_buying_salt_from_the_bank, The_price_of_buying_wheat_from_the_bank, The_price_of_buying_workers_from_the_bank, The_price_of_buying_technologies_from_the_bank, The_sale_price_of_milk_to_the_bank, The_sale_price_of_salt_to_the_bank, The_sale_price_of_wheat_to_the_bank, The_sale_price_of_workers_to_the_bank, The_sale_price_of_technologies_to_the_bank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (1, 15, 17, 1200, 1400, 6, 19, 16, 1200, 110, 110, 110, 110, 110, 90, 90, 90, 90, 90))
    cur.execute(
        f"INSERT INTO Table{Num} (Round, Inflation, Key_Rate, The_cost_of_improving_Geometric_Progressions, The_cost_of_buying_a_franchise_from_a_bank, The_performance_of_the_new_franchise_in_the_Cards, Loan_rate_at_the_bank, Deposit_to_the_bank, The_price_of_buying_Bread_by_the_bank, The_price_of_buying_milk_from_a_bank, The_price_of_buying_salt_from_the_bank, The_price_of_buying_wheat_from_the_bank, The_price_of_buying_workers_from_the_bank, The_price_of_buying_technologies_from_the_bank, The_sale_price_of_milk_to_the_bank, The_sale_price_of_salt_to_the_bank, The_sale_price_of_wheat_to_the_bank, The_sale_price_of_workers_to_the_bank, The_sale_price_of_technologies_to_the_bank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (2, 10, 11, 1200, 1400, 6, 13, 10, 1380, 128, 128, 128, 128, 128, 102, 102, 102, 102, 102))
    cur.execute(
        f"INSERT INTO Table{Num} (Round, Inflation, Key_Rate, The_cost_of_improving_Geometric_Progressions, The_cost_of_buying_a_franchise_from_a_bank, The_performance_of_the_new_franchise_in_the_Cards, Loan_rate_at_the_bank, Deposit_to_the_bank, The_price_of_buying_Bread_by_the_bank, The_price_of_buying_milk_from_a_bank, The_price_of_buying_salt_from_the_bank, The_price_of_buying_wheat_from_the_bank, The_price_of_buying_workers_from_the_bank, The_price_of_buying_technologies_from_the_bank, The_sale_price_of_milk_to_the_bank, The_sale_price_of_salt_to_the_bank, The_sale_price_of_wheat_to_the_bank, The_sale_price_of_workers_to_the_bank, The_sale_price_of_technologies_to_the_bank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (3, 5, 10, 1200, 1400, 6, 12, 9, 1518, 142, 142, 142, 142, 142, 110, 110, 110, 110, 110))
    cur.execute(
        f"INSERT INTO Table{Num} (Round, Inflation, Key_Rate, The_cost_of_improving_Geometric_Progressions, The_cost_of_buying_a_franchise_from_a_bank, The_performance_of_the_new_franchise_in_the_Cards, Loan_rate_at_the_bank, Deposit_to_the_bank, The_price_of_buying_Bread_by_the_bank, The_price_of_buying_milk_from_a_bank, The_price_of_buying_salt_from_the_bank, The_price_of_buying_wheat_from_the_bank, The_price_of_buying_workers_from_the_bank, The_price_of_buying_technologies_from_the_bank, The_sale_price_of_milk_to_the_bank, The_sale_price_of_salt_to_the_bank, The_sale_price_of_wheat_to_the_bank, The_sale_price_of_workers_to_the_bank, The_sale_price_of_technologies_to_the_bank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (4, 2, 8, 1200, 1400, 6, 10, 7, 1594, 151, 151, 151, 151, 151, 114, 114, 114, 114, 114))
    # Создание таблицы для основной информации по команде, все команды в одном месте, иноформация самая актуальная в конце бахзы данных
    cur.execute(f'''
            	CREATE TABLE IF NOT EXISTS Game{Num} (
                	id SERIAL PRIMARY KEY,
                	TeamNumber INTEGER NOT NULL,
                	TeamName VARCHAR(50) NOT NULL,
                	Round INTEGER NOT NULL, 
                	BankAccount INTEGER NOT NULL,
                	Сontribution INTEGER NOT NULL,
                	Сredit INTEGER NOT NULL,
                	MaxCredit INTEGER NOT NULL,
                	Production_Of_Milk INTEGER,
                	Production_Of_Wheat INTEGER,
                	Production_Of_Worker INTEGER,
                	Production_Of_Salt INTEGER,
                	Production_Of_Technologies INTEGER,
                	Count_Of_Milk INTEGER,
                    Count_Of_Wheat INTEGER,
                    Count_Of_Worker INTEGER,
                    Count_Of_Salt INTEGER,
                    Count_Of_Technologies INTEGER
                    );
        	''')

def NextRound(Num):
    cur.execute(f"SELECT Round FROM game{Num};")
    Round = int(cur.fetchone()[0])
    cur.execute(f"UPDATE game{Num} SET Round = {Round+1};")
    cur.execute(f"UPDATE game{Num} SET count_of_milk = count_of_milk + production_of_milk, count_of_wheat = count_of_wheat + production_of_wheat, count_of_worker = count_of_worker + production_of_worker, count_of_salt = count_of_salt + production_of_salt, count_of_technologies = count_of_technologies + production_of_technologies;")
    cur.execute(f"SELECT Round FROM game{Num};")
    Num = int(cur.fetchone()[0])
    print(f"Текущий раунд: {Num}")
def EndGame(Num):
    cur.execute(f"Select * FROM Game{Num}")
    colnames = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    print(colnames)
    print(rows)
    # Вставка данных
    cur.execute("UPDATE data SET game_id = %s WHERE game_id = %s;", (Num+1, Num))
    cur.close()
    conn.close()



class Command:
    number_of_command = 1
    start_count_of_production = 10
    start_money_of_command = 1000
    start_other_production = 0
    start_count_of_cards = 0


    improvement_indicator_of_production_of_wheat= 1
    improvement_indicator_of_production_of_eggs = 1

    def __init__(self, name_of_command, name_of_production):
        self.name_of_command = name_of_command
        self.name_of_production = name_of_production
        self.number_of_command = Command.number_of_command


        cur.execute("SELECT * FROM Data;")
        Num = int(cur.fetchone()[0])

        match self.name_of_production:  # Определение производства команды, присвоение начального значения в зависимости от этого
            case "Молочное":
                cur.execute(
                    f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Production_Of_Wheat, Production_Of_Worker, Production_Of_Salt, Production_Of_Technologies, Count_Of_Milk, Count_Of_Wheat, Count_Of_Worker, Count_Of_Salt, Count_Of_Technologies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (self.number_of_command, self.name_of_command, 0, Command.start_money_of_command, 0, 0, 600, Command.start_count_of_production, Command.start_other_production, Command.start_other_production, Command.start_other_production, Command.start_other_production, Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards))
            case "Пшеничное":
                cur.execute(
                    f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Production_Of_Wheat, Production_Of_Worker, Production_Of_Salt, Production_Of_Technologies, Count_Of_Milk, Count_Of_Wheat, Count_Of_Worker, Count_Of_Salt, Count_Of_Technologies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (self.number_of_command, self.name_of_command, 0, Command.start_money_of_command, 0, 0, 600, Command.start_other_production, Command.start_count_of_production, Command.start_other_production,
                     Command.start_other_production, Command.start_other_production, Command.start_count_of_cards,
                     Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards,
                     Command.start_count_of_cards))
            case "Рабочее":
                cur.execute(
                    f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Production_Of_Wheat, Production_Of_Worker, Production_Of_Salt, Production_Of_Technologies, Count_Of_Milk, Count_Of_Wheat, Count_Of_Worker, Count_Of_Salt, Count_Of_Technologies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (self.number_of_command, self.name_of_command, 0, Command.start_money_of_command, 0, 0, 600,
                     Command.start_other_production, Command.start_other_production, Command.start_count_of_production,
                     Command.start_other_production, Command.start_other_production, Command.start_count_of_cards,
                     Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards,
                     Command.start_count_of_cards))
            case "Солевое":
                cur.execute(
                    f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Production_Of_Wheat, Production_Of_Worker, Production_Of_Salt, Production_Of_Technologies, Count_Of_Milk, Count_Of_Wheat, Count_Of_Worker, Count_Of_Salt, Count_Of_Technologies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (self.number_of_command, self.name_of_command, 0, Command.start_money_of_command, 0, 0, 600,
                     Command.start_other_production, Command.start_other_production,Command.start_other_production,
                     Command.start_count_of_production, Command.start_other_production, Command.start_count_of_cards,
                     Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards,
                     Command.start_count_of_cards))
            case "Технологическое":
                cur.execute(
                    f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Production_Of_Wheat, Production_Of_Worker, Production_Of_Salt, Production_Of_Technologies, Count_Of_Milk, Count_Of_Wheat, Count_Of_Worker, Count_Of_Salt, Count_Of_Technologies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (self.number_of_command, self.name_of_command, 0, Command.start_money_of_command, 0, 0, 600,
                     Command.start_other_production, Command.start_other_production,Command.start_other_production,
                     Command.start_other_production, Command.start_count_of_production, Command.start_count_of_cards,
                     Command.start_count_of_cards, Command.start_count_of_cards, Command.start_count_of_cards,
                     Command.start_count_of_cards))
            case _:
                print("hyi")
        print(f'Команда: {self.name_of_command}, имеет: {Command.start_money_of_command} - денег, производство: {self.name_of_production}, {self.number_of_command}')
        Command.number_of_command += 1
    def Test (self, Num):
        cur.execute(f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Count_Of_Milk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",(1, "Team1", 0, 1000, 0, 0, 1000, 0, 0))
        cur.execute(f"INSERT INTO Game{Num} (TeamNumber, TeamName, Round, BankAccount, Сontribution, Сredit, MaxCredit, Production_Of_Milk, Count_Of_Milk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",(1, "Team1", 0, 1000, 0, 0, 1000, 0, 0))
        print(f"Select * FROM Game{Num}")
        cur.execute(f"Select * FROM Game{Num}")
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        print(colnames)
        print(rows)
    def buy_cart(self, Num):
        # Добавить вывод нового количества карт на балансе
        type_of_card = input("Введите тип карточки которую хотите купить (молоко, пшеница, работник, соль, технологии): ")

        match type_of_card:
            case "молоко":
                type_of_cards = "the_price_of_buying_milk_from_a_bank"
            case "соль":
                type_of_cards = "the_price_of_buying_salt_from_a_bank"
            case "пшеница":
                type_of_cards = "the_price_of_buying_wheat_from_a_bank"
            case "работник":
                type_of_cards = "the_price_of_buying_workers_from_a_bank"
            case "технологии":
                type_of_cards = "the_price_of_buying_technologies_from_a_bank"

        cur.execute(f"SELECT game{Num}.bankaccount, table{Num}.{type_of_cards} FROM game{Num} INNER JOIN table{Num} ON table{Num}.round = game{Num}.round where game{Num}.teamnumber = {self.number_of_command};")
        rows = cur.fetchall()
        bankaccount = rows[0][0]
        price = rows[0][1]
        match type_of_card:
            case "молоко":
                type_of_cards = "count_of_milk"
            case "соль":
                type_of_cards = "count_of_salt"
            case "пшеница":
                type_of_cards = "count_of_wheat"
            case "работник":
                type_of_cards = "count_of_workers"
            case "технологии":
                type_of_cards = "count_of_technologies"
        print(f"На вашем аккаунте {bankaccount}, вы можете купить  {bankaccount//price} карточек за {price}")
        count = int(input("Сколько карточек вы хотите купить: "))
        while count * price > bankaccount:
            print("Недостаточно денег")
            count = int(input("Сколько карточек вы хотите купить: "))
        cur.execute(f"UPDATE game{Num} SET bankaccount = bankaccount - {price} * {count}, {type_of_cards} = {type_of_cards} + {count} WHERE game{Num}.teamnumber = {self.number_of_command};")

    def sell_cart(self, Num):

        type_of_card = input("Введите тип карточки которую хотите продать (молоко, пшеница, работник, соль, технологии): ")
        match type_of_card:
            case "молоко":
                type_of_cards = "count_of_milk"
            case "соль":
                type_of_cards = "count_of_salt"
            case "пшеница":
                type_of_cards = "count_of_wheat"
            case "работник":
                type_of_cards = "count_of_workers"
            case "технологии":
                type_of_cards = "count_of_technologies"
        match type_of_card:
            case "молоко":
                price_of_cardse = "the_sale_price_of_milk_to_the_bank"
            case "соль":
                price_of_cardse = "the_sale_price_of_salt_to_the_bank"
            case "пшеница":
                price_of_cardse = "the_sale_price_of_wheat_to_the_bank"
            case "работник":
                price_of_cardse = "the_sale_price_of_workers_to_the_bank"
            case "технологии":
                price_of_cardse = "the_sale_price_of_technologies_to_the_bank"

        cur.execute(f"SELECT game{Num}.{type_of_cards}, table{Num}.{price_of_cardse} FROM game{Num} INNER JOIN table{Num} ON table{Num}.round = game{Num}.round where game{Num}.teamnumber = {self.number_of_command};")
        rows = cur.fetchall()
        count = rows[0][0]
        price = rows[0][1]
        print(count, price)
        print(f"На вашем аккаунте {count} карточек типа: {type_of_card}, вы можете продать их за  {price*count}, где цена одной карточки: {price}")
        count_sell = int(input("Сколько карточек вы хотите продать: "))
        while count_sell > count:
            print("Недостаточно карточек")
            count_sell = int(input("Сколько карточек вы хотите продать: "))
        cur.execute(f"UPDATE game{Num} SET bankaccount = bankaccount + {price} * {count_sell}, {type_of_cards} = {type_of_cards} - {count_sell} WHERE game{Num}.teamnumber = {self.number_of_command};")




    # def send_to_the_team(self, other,  name_of_command_send, type_of_send, quanity):#производит передачу ресурсов от команды которая вызвала с командой которая приниает предложение
    # 	match other.number_of_command:
    # 		case 0:
    # 			first_command.proverka(self.type_of_send, )
    # 		case 1:
    # 			print()
    # 		case _:

    # 			print("hyi a ne perevod")
    # 	def proverka(self, other, type, q):
    # 		match type:
    # 			case "Яица":
    # 				other.quanity_eggs+=q
    # 				self.quanity_eggs-=q
    # 			case "Пшеница":
    # 				ther.quanity_wheat_flour+=q
    # 				self.quanity_wheat_flour-=q
    # def send_to_the_team(self, other, type_of_send, quanity=0, mony=0):
    #     if other.mony_of_command < mony:
    #         print(f'Сделка не состоялась т.к. у команды {other.name_of_command} недостаточно: {mony}')
    #     match type_of_send:
    #         case "Яица":
    #             if self.quanity_eggs < quanity:
    #                 print(
    #                     f'Сделка не состоялась т.к. у вас недостаточно: {type_of_send}, максимальное количество для передачи: {self.quanity_eggs}')
    #                 return
    #         case "Пшеница":
    #             if self.quanity_eggs < quanity:
    #                 print(
    #                     f'Сделка не состоялась т.к. у вас недостаточно: {type_of_send}, максимальное количество для передачи: {self.quanity_wheat_flour}')
    #                 return
    #     approval = input(
    #         f"согласны ли вы на обмен {type_of_send} - типа товара в размере: {quanity} с командой: {other.name_of_command}?\n")
    #
    #     if approval == "Да":
    #         match type_of_send:
    #             case "Яица":
    #                 other.quanity_eggs += quanity
    #                 self.quanity_eggs -= quanity
    #                 self.mony_of_command += mony
    #                 other.mony_of_command -= mony
    #                 print("Сделка слстоялась")
    #
    #             case "Пшеница":
    #                 other.quanity_wheat_flour += quanity
    #                 self.quanity_wheat_flour -= quanity
    #                 self.mony_of_command += mony
    #                 other.mony_of_command -= mony
    #                 print("Сделка слстоялась")
    #     else:
    #         print("Сделка не состоялась")



# Подключение к базе данных postgres
conn = psycopg2.connect(
dbname="postgres",
user="postgres",
password="1234",
host="localhost",
port="5432"
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT * FROM Data;")

Num: int = int(cur.fetchone()[0])

a= input()
while a != "endgame":
    match a:
        case "start":
            print("Начало игры выводиться основная информация по командам: ")
            StartGame(Num)
            first_command = Command("Мука", "Молочное")
            second_command = Command("Пшеница", "Пшеничное")
            third_command = Command("Работники", "Рабочее")
            fourth_command = Command("Соль", "Солевое")
            fifth_command = Command("Технологии", "Технологическое")
            print('')
            print(f"Игра успешно начата номер игры = {Num}")
        case "next round":
            print("Следующий раунд")
            NextRound(Num)
        case "by card":
            a = int(input("Введите номер команды: "))
            match a:
                case 1:
                    first_command.buy_cart(Num)
                case 2:
                    print("sdfsfdsfd")
                    second_command.buy_cart(Num)
                case 3:
                    third_command.buy_cart(Num)
                case 4:
                    fourth_command.buy_cart(Num)
                case 5:
                    fifth_command.buy_cart(Num)
        case "sell card":
            a = int(input("Введите номер команды: "))
            match a:
                case 1:
                    first_command.sell_cart(Num)
                case 2:
                    print("sdfsfdsfd")
                    second_command.sell_cart(Num)
                case 3:
                    third_command.sell_cart(Num)
                case 4:
                    fourth_command.sell_cart(Num)
                case 5:
                    fifth_command.sell_cart(Num)
        case "end":
            EndGame(Num)
        case "end game":
            break
        case _:
            print("hi")
    a = input()
# second_command = Command("Яица", "Яичное")
# second_command.receiving_of_eggs()
# first_command.send_to_the_team(second_command, "Яица", 12, 100)
# second_command.send_to_the_team(first_command, "Яица", 3, 100)
# # first_command.match_production(first_command.name_of_production)
# print(first_command.production_of_wheat_flour)
# print("hi")
# executor.start_polling(dp, skip_updates=True)




# EndGame()

