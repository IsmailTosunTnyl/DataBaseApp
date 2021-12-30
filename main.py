from dotenv import dotenv_values
from database import Database
import os


def print_database(object):
    os.system('cls')
    print(f"Executed query is '{object[2]}'")
    header = ""
    for title in object[1]:
        header += "|     " + title + "    |"
    print(header)
    for row in object[0]:
        s = ""
        for column in row:
            s += "|  " + str(column).strip() + " |"
        print(s)
    input("\n Devam Etmek için 'ENTER' basın")


def menu(db):
    main_menu = "1.Kayıtlı Sorugular\n" \
                "2.Özel Sorgu\n" \
                "0.Çıkış"


    while True:

        try:
            print(main_menu)
            input_variable = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
            os.system('cls')
            match input_variable:

                case 1:
                    for q in range(1, len(db.predefined_queries) + 1):
                        print(f"{q}. {db.predefined_queries[q - 1]}")

                    input_variable = int(input("\n istediğiniz sorgunun numarasını giriniz: "))

                    print_database(db.execute_query(db.predefined_queries[input_variable - 1]))
                case 2:
                    query = str(input(
                        "Yapmak istediğiniz sorguyu tek parça halinde postgreSQL yazım kurallarına uygun şekilde yazın\n"))
                    print_database(db.execute_query(query))
                case 0:
                    return
                case _:
                    os.system('cls')
                    print("Hatalı Tuşlama Yaptınız")
                    input("\n Devam Etmek için 'ENTER' basın")
        except :
            os.system('cls')
            print("Hatalı Tuşlama Yaptınız")
            db = Database(dotenv_values()["url"])
            input("\n Devam Etmek için 'ENTER' basın")


if __name__ == '__main__':
    db = Database(dotenv_values()["url"])
    menu(db)
