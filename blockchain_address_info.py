import requests

ETHERSCAN_API_KEY = "YZ9RHBBWFNMTV81KJEHU3J2G89GPD2YEB7"                               
                                                                                       
def get_ethereum_balance(address: str) -> float:
    """Fetches the balance of an Ethereum address."""
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
                                                                                        
    if data['status'] == '1' and data['message'] == 'OK':
        return float(data.get("result", 0)) / 1e18                                      
    else:
        print("Failed to fetch balance.")
        return 0.0

                                                                                        
def get_ethereum_transactions(address: str) -> list:
    """Fetches the last 5 transactions of an Ethereum address."""
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
                                                                                        
    if data['status'] == '1' and data['message'] == 'OK':
        return data.get("result", [])[:5]                                                  
    else:
        print("Failed to fetch transactions.")
        return []


def display_transactions(transactions):
    print(f"{'Hash':<66} {'From':<42} {'To':<42} {'Value (ETH)':<20} {'Timestamp'}")
    print("-" * 150)  
    for tx in transactions:
        tx_hash = tx.get('hash', 'N/A')
        from_address = tx.get('from', 'N/A')
        to_address = tx.get('to', 'N/A')
        value = float(tx.get('value', 0)) / 1e18  
        timestamp = tx.get('timeStamp', 'N/A')
        print(f"{tx_hash:<66} {from_address:<42} {to_address:<42} {value:<20} {timestamp}")
    

def main():
    
    address = input("Enter Ethereum address: ")
    
    
    balance = get_ethereum_balance(address)
    print(f"Balance for {address}: {balance} ETH")
    
    
    transactions = get_ethereum_transactions(address)
    print(f"\nLast 5 Transactions for {address}:")
    
    
    if transactions:
        display_transactions(transactions)
    else:
        print("No transactions found for this address.")

if __name__ == "__main__":
    main()
