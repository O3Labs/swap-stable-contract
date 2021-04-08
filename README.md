# Stable Swap Pool

## Steps to Generate usd pool contract

### Step 1

Open `contracts/pool-templates/base/pooldata.json` and fill the coins array.

For example:

``` json
{
    "lp_contract": "LPToken",
    "lp_constructor": {
        "symbol": "O3LP-USD",
        "name": "o3pool-usdt-usdc-dai"
    },
    "swap_constructor": {
        "_A": 200,
        "_fee": 4000000
    },
    "coins": [
        {
            "decimals": 6,
            "name": "USDT",
            "underlying_address": "0xCfEB869F69431e42cdB54A4F4f105C19C080A601"
        },
        {
            "decimals": 6,
            "name": "USDC",
            "underlying_address": "0xC89Ce4735882C9F0f0FE26686c53074E09B0D550"
        },
        {
            "decimals": 6,
            "name": "DAI",
            "underlying_address": "0x254dffcd3277C0b1660F6d42EFbB754edaBAbC2B"
        }
    ]
}
```

### Step 2

Back to project root path and run

``` shell
python generate_base.py usd
```

## Steps to deploy the contract

1. Open `scripts/deploy.py`.
1. Set the address for `DEPLOYER` and `POOL_OWNER`.
1. Run `pip install -r requirements.txt`.
1. Install `brownie` if not installed already: `pip install eth-brownie`.
1. Add fullnode rpc info for brownie:

    ```shell
    brownie networks add <category> <id> host=<host> chainid=<chainid>
    ```

    Example:

    ```shell
    brownie networks add test testing-server host=http://xxx.node:8545 chainid=123
    ```

1. Deploy usd pool contract and lp token contract to the network:

    ```shell
    brownie run deploy --network testing-server -I
    ```
