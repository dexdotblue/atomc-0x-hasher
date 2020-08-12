from web3 import Web3

EIP191_HEADER = '\x19\x01'
EIP712_ORDER_SCHEMA_HASH = '0x770501F88A26EDE5C04A20EF877969E961EB11FC13B78AAF414B633DA0D4F86F'
EIP712_DOMAIN_HASH = '0x8A86ABAAAA6F39CD45268DF47006089C9F4E0EECE818A502CC836ABBA54724AE'


def hash_order(makerAddress, takerAddress, feeRecipientAddress, senderAddress, makerAssetAmount, takerAssetAmount, makerFee, takerFee, expirationTimeSeconds, salt, makerAssetData, takerAssetData):
    order_hash_types = [
        'bytes32',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'uint256',
        'bytes',
        'bytes'
    ]
    order_hash_data = [
        Web3.toBytes(hexstr=EIP712_ORDER_SCHEMA_HASH),
        Web3.toInt(hexstr=makerAddress),
        Web3.toInt(hexstr=takerAddress),
        Web3.toInt(hexstr=feeRecipientAddress),
        Web3.toInt(hexstr=senderAddress),
        makerAssetAmount,
        takerAssetAmount,
        makerFee,
        takerFee,
        expirationTimeSeconds,
        salt,
        Web3.keccak(hexstr=makerAssetData),
        Web3.keccak(hexstr=takerAssetData)
    ]

    return Web3.toHex(Web3.solidityKeccak(
        ['string', 'bytes32', 'bytes32'],
        [
            EIP191_HEADER,
            Web3.toBytes(hexstr=EIP712_DOMAIN_HASH),
            Web3.solidityKeccak(order_hash_types, order_hash_data)
        ]
    ))
