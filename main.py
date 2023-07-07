import json

def lambda_handler(event, context):
    
    textbooks = {
        "Mathematics": ["$1.99", "12"],
        "English": ["$2.99", "16"],
        "French": ["$1.44", "34"]
    }
    
    textbook_name = event.get("textbookName")
    no_of_books = event.get("no")
    moneyForPurchase = event.get("purchaseMoney")
    
    quantity_in_stock = textbooks.get(textbook_name)[1] 
    
    if int(no_of_books) > int(quantity_in_stock):
        return {
            "message": f"Sorry, we do not have that much in stock, there are only {quantity_in_stock} available at this time"
        }
    
    price_of_books = float(textbooks.get(textbook_name)[0].strip()[1:5]) * int(no_of_books)
    print(price_of_books)
    
    
    if price_of_books > moneyForPurchase:
        short = price_of_books - moneyForPurchase
        return {
            "message": f"Sorry, insufficient funds, you are ${round(short, 2)} short",
        }
    
    balance = moneyForPurchase - price_of_books
    return {
        "receipt": {
                "TextBook": textbook_name,
                "Quantity": no_of_books,
                "Balance": f"${round(balance, 2)}"
            } 
        }
