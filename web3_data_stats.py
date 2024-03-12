from web3 import Web3

# 连接到Web3节点
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your_infura_project_id'))

def get_transaction_count():
    # 获取最新区块号
    latest_block_number = w3.eth.block_number
    # 获取最新区块
    latest_block = w3.eth.get_block(latest_block_number)
    # 获取最新区块的交易数量
    transaction_count = len(latest_block.transactions)
    return transaction_count

def get_account_count():
    # 获取当前网络上的所有账户
    accounts = w3.eth.accounts
    # 计算账户数量
    account_count = len(accounts)
    return account_count

def get_contract_deployments():
    # 获取最新区块号
    latest_block_number = w3.eth.block_number
    contract_deployments = 0
    # 遍历最新区块，统计合约部署情况
    for i in range(latest_block_number - 100, latest_block_number + 1):
        block = w3.eth.get_block(i)
        for transaction in block.transactions:
            # 判断交易是否为合约创建交易
            receipt = w3.eth.get_transaction_receipt(transaction.hex())
            if receipt and receipt.contract_address:
                contract_deployments += 1
    return contract_deployments

def main():
    # 获取交易数量
    transaction_count = get_transaction_count()
    print("交易数量:", transaction_count)

    # 获取账户数量
    account_count = get_account_count()
    print("账户数量:", account_count)

    # 获取合约部署数量
    contract_deployments = get_contract_deployments()
    print("合约部署数量:", contract_deployments)

if __name__ == "__main__":
    main()
