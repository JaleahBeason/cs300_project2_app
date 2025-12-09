
from db import get_connection

def add_shop():
    print("\n--- Add Shop ---")
    try:
        shop_id = int(input("Shop ID (int): "))
        mall_id = int(input("Mall ID (int): "))
        retailer_id = int(input("Retailer ID (int): "))
        shop_name = input("Shop Name: ")
        floor_space = int(input("Floor Space (sq ft): "))
        rent_amount = float(input("Rent Amount: "))
        percent_sales = float(input("Percent of Sales (e.g. 7.5): "))
    except ValueError:
        print("Invalid number entered. Try again.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        sql = """
            INSERT INTO Shop
            (Shop_ID, Mall_ID, Retailer_ID, Shop_Name, Floor_Space, Rent_Amount, Percent_Sales)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (shop_id, mall_id, retailer_id, shop_name,
                          floor_space, rent_amount, percent_sales))
        conn.commit()
        print("Shop added successfully.")
    except Exception as e:
        print("Error adding shop:", e)
    finally:
        cur.close()
        conn.close()


def delete_shop():
    print("\n--- Delete Shop ---")
    try:
        shop_id = int(input("Shop ID to delete: "))
    except ValueError:
        print("Invalid Shop ID.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Shop WHERE Shop_ID = %s"
        cur.execute(sql, (shop_id,))
        conn.commit()
        if cur.rowcount == 0:
            print("No shop with that ID.")
        else:
            print("Shop deleted.")
    except Exception as e:
        print("Error deleting shop:", e)
    finally:
        cur.close()
        conn.close()


def update_shop_rent():
    print("\n--- Update Shop Rent ---")
    try:
        shop_id = int(input("Shop ID to update: "))
        new_rent = float(input("New rent amount: "))
    except ValueError:
        print("Invalid number.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        sql = "UPDATE Shop SET Rent_Amount = %s WHERE Shop_ID = %s"
        cur.execute(sql, (new_rent, shop_id))
        conn.commit()
        if cur.rowcount == 0:
            print("No shop with that ID.")
        else:
            print("Rent updated.")
    except Exception as e:
        print("Error updating rent:", e)
    finally:
        cur.close()
        conn.close()


def sp_get_shop_total_income():
    print("\n--- GetShopTotalIncome (SP) ---")
    try:
        shop_id = int(input("Shop ID: "))
    except ValueError:
        print("Invalid Shop ID.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        # second parameter is OUT, so we pass a placeholder (0)
        args = [shop_id, 0.0]
        result_args = cur.callproc("GetShopTotalIncome", args)
        total_income = result_args[1]
        print(f"Total income for shop {shop_id}: {total_income}")
    except Exception as e:
        print("Error calling GetShopTotalIncome:", e)
    finally:
        cur.close()
        conn.close()


def sp_get_shops_in_mall():
    print("\n--- GetShopsInMall (SP) ---")
    try:
        mall_id = int(input("Mall ID: "))
    except ValueError:
        print("Invalid Mall ID.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.callproc("GetShopsInMall", [mall_id])
        # stored_results() gives us the SELECT result set(s)
        for result in cur.stored_results():
            rows = result.fetchall()
            if not rows:
                print("No shops found for that mall.")
            else:
                print("Shop_ID | Shop_Name | Retailer_Name | Floor_Space | Rent_Amount | Percent_Sales")
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error calling GetShopsInMall:", e)
    finally:
        cur.close()
        conn.close()


def sp_add_maintenance_event():
    print("\n--- AddMaintenanceEvent (SP) ---")
    try:
        shop_id = int(input("Shop ID: "))
        date_str = input("Event date (YYYY-MM-DD): ")
        cost = float(input("Cost: "))
        mtype = input("Type ('Scheduled' or 'Unscheduled'): ")
    except ValueError:
        print("Invalid input.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.callproc("AddMaintenanceEvent", [shop_id, date_str, cost, mtype])
        conn.commit()
        print("Maintenance event added.")
    except Exception as e:
        print("Error calling AddMaintenanceEvent:", e)
    finally:
        cur.close()
        conn.close()


def sp_get_mall_income_summary():
    print("\n--- GetMallIncomeSummary (SP) ---")
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.callproc("GetMallIncomeSummary")
        for result in cur.stored_results():
            rows = result.fetchall()
            print("Mall_ID | Mall_Name | Mall_Total_Income")
            for row in rows:
                print(row)
    except Exception as e:
        print("Error calling GetMallIncomeSummary:", e)
    finally:
        cur.close()
        conn.close()


def sp_get_average_discount_for_mall():
    print("\n--- GetAverageDiscountForMall (SP) ---")
    try:
        mall_id = int(input("Mall ID: "))
    except ValueError:
        print("Invalid Mall ID.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        args = [mall_id, 0.0]
        result_args = cur.callproc("GetAverageDiscountForMall", args)
        avg_disc = result_args[1]
        print(f"Average retailer discount for mall {mall_id}: {avg_disc}")
    except Exception as e:
        print("Error calling GetAverageDiscountForMall:", e)
    finally:
        cur.close()
        conn.close()


\
def main_menu():
    while True:
        print("\n===== CS300 Project 2 – Mall DB App =====")
        print("1. Add Shop")
        print("2. Delete Shop")
        print("3. Update Shop Rent")
        print("4. Get Shop Total Income (SP)")
        print("5. Get Shops in Mall (SP)")
        print("6. Add Maintenance Event (SP)")
        print("7. Get Mall Income Summary (SP)")
        print("8. Get Average Discount for Mall (SP)")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_shop()
        elif choice == "2":
            delete_shop()
        elif choice == "3":
            update_shop_rent()
        elif choice == "4":
            sp_get_shop_total_income()
        elif choice == "5":
            sp_get_shops_in_mall()
        elif choice == "6":
            sp_add_maintenance_event()
        elif choice == "7":
            sp_get_mall_income_summary()
        elif choice == "8":
            sp_get_average_discount_for_mall()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
