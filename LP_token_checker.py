import json
from web3 import Web3
import requests
import re
import time
from tabulate import tabulate

tick = time.time()

matic_APIKey = "INSERT_POLYGONSCAN_API_KEY"
matic_rpc = "https://matic-mainnet.chainstacklabs.com"
matic_scanner_url = "https://api.polygonscan.com/api?"

polygon = {"network": "polygon", "apikey": matic_APIKey, "rpc": matic_rpc, "scanner": matic_scanner_url}

bsc_APIKey = "INSERT_BSCSCAN_API_KEY"
bsc_rpc = "https://bsc-dataseed.binance.org/"
# bsc_rpc = "https://bsc.mytokenpocket.vip"
# bsc_rpc = "https://binance.ankr.com:8545"
# bsc_rpc = "https://bsc.getblock.io/mainnet/"
bsc_scanner_url = "https://api.bscscan.com/api?"

bsc = {"network": "bsc", "apikey": bsc_APIKey, "rpc": bsc_rpc, "scanner": bsc_scanner_url}

# list of Masterchefs

# dictionary template = {"network":"polygon", "name": "", "masterchef": "", "timelock":""}

farm_slowpoke = {"network": "polygon", "name": "slowpoke", "masterchef": "0x6CF9D94F71907102558d0A5E9BC48206540Be40d","timelock": "0xbCe0CBaC6844e6B0A9892d8BE66A162B97536727"}
farm_polycuban = {"network": "polygon", "name": "polycuban", "masterchef": "0xFcB50bA9D50ec0a3705a554f0b5E76d3909b2Df9","timelock": ""}
farm_polycubanv2 = {"network": "polygon", "name": "polycuban", "masterchef": "0x66886e787c9aE72b7418234C871e872a67FC357f","timelock": ""}
farm_polyvertex = {"network": "polygon", "name": "polyvertex","masterchef": "0x8bE82Ab9B6179bE6EB88431E3E4E0fd93b9E607C","timelock": "0x8eC313CFbc877a9E0559c8e80763a9a058C28C69"}
farm_polycat = {"network": "polygon", "name": "polycat", "masterchef": "0x8CFD1B9B7478E7B0422916B72d1DB6A9D513D734","timelock": "0xf5a824B077Cc0aaF50Cf83a9E82714b89B684925"}
farm_zodiac = {"network": "polygon", "name": "12ZodiacFinance","masterchef": "0xd30418ebfffd5c9fe1b548e347661177a316cc20", "timelock": ""}
farm_polysnow = {"network": "polygon", "name": "polysnow", "masterchef": "0xFf42AE1A338585316267345E6234fc7E6de15D34", "timelock": "0x1e2691ba284639E9185C7d305c2c40ad270d6f25"}
farm_polyyield = {"network": "polygon", "name": "polyyield", "masterchef": "0x9eaacd7d41fdde61314eeeb61326c06402b9bfe3", "timelock": ""}
farm_gemstone = {"network": "polygon", "name": "gemstone", "masterchef": "0x9BFD897e3eabFfA738a8F1c4d0B397C07E97E42D","timelock": ""}
farm_adamant = {"network": "polygon", "name": "adamant", "masterchef": "0x7aa078eb0Ebf3C6775572f493f3435aCBC9aB706","timelock": ""}
farm_honest = {"network": "polygon", "name": "honest", "masterchef": "0xf43261d712cCa4aE55b34B77d9157e773254D1dF","timelock": ""}
farm_polyorca = {"network": "polygon", "name": "polyorca", "masterchef": "0x38aAA663e004De27AB2592Dd30247E605a101f9c", "timelock": ""}
farm_polyeevee = {"network": "polygon", "name": "polyeevee", "masterchef": "0x55642E8Df0153010Df8415f0D2e6e4679A1D5d88","timelock": ""}
farm_polyroll = {"network": "polygon", "name": "polyroll", "masterchef": "0x3C58EA8D37f4fc6882F678f822E383Df39260937","timelock": ""}
farm_polygamer = {"network":"polygon", "name": "polygamer", "masterchef": "0x49C472315BADa5612b5EfB0a1152e59461E0dBfE","timelock":""}
farm_polyyeld = {"network":"polygon", "name": "polyyeld", "masterchef": "0x2DC11B394BD0f1CC6AC0a269cfe3CC0b333601B4","timelock":"0xF034c02662bD8a09affc4979816C8f723386b4dc"}
farm_sweets = {"network":"polygon", "name": "sweets.farm", "masterchef": "0x1823886920374e9Aa33eb8BFfD98C7B0595b5c42","timelock":""}
farm_polypulsar = {"network":"polygon", "name": "polypulsar", "masterchef": "0x217cF04C783818E5b15Ae0723b22Ee2415Ab5fe3", "timelock":""}
farm_gravity = {"network":"polygon", "name": "gravity", "masterchef": "0xf9FBfA8Fd7568D39E1b2091379499B48EA2F4c72", "timelock":""}
farm_beets = {"network":"polygon", "name": "beets", "masterchef": "0x569610567F5262b6A9bfdf6B04793A407d8E97c7", "timelock":""}
farm_dinosaur = {"network":"polygon", "name": "dinosaur", "masterchef": "0xA12005edA0eb0f83462D39A8452b3b976f926a76", "timelock":""}
farm_polyweed = {"network":"polygon", "name": "polyweed", "masterchef": "0x703418a72FC982ec157b6388E6e9f2C9E09d96D3", "timelock":""}
farm_romefi = {"network":"polygon", "name": "rome finance", "masterchef": "0x21e3346eef563f24088cd49d5bb4f6df87d7aca2", "timelock":""}
farm_spacedefiA = {"network":"polygon", "name": "Space Defi A", "masterchef": "0x8AfFf0191249E5563a063C758C0a2a189a9cB35C", "timelock":""}
farm_cubex = {"network":"polygon", "name": "cubex", "masterchef": "0xB5b591fd4CAd5c85cfFb2C361a12Df108475c27D", "timelock":""}
farm_polysheep = {"network":"polygon", "name": "polysheep", "masterchef": "0x50D4592f2C562258aC6648478595160cD0Cca2aB", "timelock":""}
farm_polyzeus = {"network":"polygon", "name": "polyzeus", "masterchef": "0x9DD398dfD94d40699eCb020864e3501d8a978C71", "timelock":""}
farm_carousel = {"network":"polygon", "name": "carousel", "masterchef": "0xFa00505AC5ef3b2bb37e421D9146c167d4c3C741", "timelock":""}
farm_foxfarming = {"network":"polygon", "name": "fox farming", "masterchef": "0x1AeC80c827F2d35d8EEF2D8D3977516271b05B2e", "timelock":""}
farm_apecomm = {"network":"polygon", "name": "ape.community", "masterchef": "0xb85A840A8b19C02C5F3188C3018f78918dB18761", "timelock":""}
farm_polybrew = {"network":"polygon", "name": "polybrew", "masterchef": "0xadAC1BC3E5E68593eD09B8A103fdC98F5f67384D", "timelock":""}
farm_polypup = {"network":"polygon", "name": "polypup", "masterchef": "0xCc7E7c9FC775D25176e9Bfc5A400EdAc212aa81C", "timelock":""}
farm_polygrass = {"network":"polygon", "name": "polygrass", "masterchef": "0x8E576c1Ee1955EDDC1C365f1Aa710209Af9286aC", "timelock":""}
farm_polymax = {"network":"polygon", "name": "polymax", "masterchef": "0x772A9845F165Ba97dd3e19f766AE25f4d0DBAf96", "timelock":""}
farm_polypupbone = {"network":"polygon", "name": "polypup bone", "masterchef": "0x9DcB2D5e7b5212fAF98e4a152827fd76bD55f68b", "timelock":""}
farm_polyruby = {"network":"polygon", "name": "polyruby", "masterchef": "0x0678F7cCbe68441bDcB09C460e14a4a2b833079B", "timelock":""}
farm_helios = {"network":"polygon", "name": "helios.cash", "masterchef": "0x702638277cf7464fD815d73322BC6b4d7C6CF3B1", "timelock":""}
farm_rediant = {"network":"polygon", "name": "rediant", "masterchef": "0x5979959483b4aAFa6a94Ba8dA6Aa406C31D06cb6", "timelock":""}
farm_augury = {"network":"polygon", "name": "augury", "masterchef": "0x6ad70613d14c34aa69E1604af91c39e0591a132e", "timelock":""}
farm_polyracoon = {"network":"polygon", "name": "polyracoon", "masterchef": "0xf840FCe89f15ADfF63cdae750Bce8B1408c205C7", "timelock":""}
farm_polybutterfly = {"network":"polygon", "name": "polybutterfly", "masterchef": "0x50C6eC50a89a946C5886Aeb54a22fe732558F7D1", "timelock":""}
farm_helios = {"network":"polygon", "name": "helios cash", "masterchef": "0x702638277cf7464fD815d73322BC6b4d7C6CF3B1", "timelock":""}
farm_bullrun = {"network":"polygon", "name": "bullrun finance", "masterchef": "0x10712a6d1B8C0de4c5172A3004A8AeE20569c670", "timelock":""}
farm_pndamatic = {"network":"polygon", "name": "panda matic", "masterchef": "0xdFF5Ae6213B65ad7355c72d19C3C1a3D8c2C78Fd", "timelock":""}
farm_polydiamond = {"network":"polygon", "name": "polydiamond", "masterchef": "0x8881BdA61814bD8875aF7E1f861277B8B845a6d7", "timelock":""}
farm_pepefarm = {"network":"polygon", "name": "pepefarm", "masterchef": "0xFB5F7a67217d2c0de0cB89F589df54Fb8452F8C1", "timelock":""}
farm_boneswap = {"network":"polygon", "name": "boneswap", "masterchef": "0x0d17c30afbd4d29eef3639c7b1f009fd6c9f1f72", "timelock":""}
farm_vampirefarming = {"network":"polygon", "name": "vampire farming", "masterchef": "0xce60111975c933efd5ae522d1b6cca86a5cba12b", "timelock":""}
farm_vixa = {"network":"polygon", "name": "vixa", "masterchef": "0x2db9C526Fb5C9531BFbC324558659ff03f928341", "timelock":""}
farm_euroballz = {"network":"polygon", "name": "euro ballz", "masterchef": "0x8fd027d88bd83c2dd6eea36a99ed349bc96d5cb4", "timelock":""}
farm_indiaswap = {"network":"polygon", "name": "india swap", "masterchef": "0x47Fe222FD26c39234f9295132444532Ba0881CC6", "timelock":""}
farm_polytopia = {"network":"polygon", "name": "polytopia", "masterchef": "0xd2Fb5e6DF8B468Ae57E7fefD942C44F275a56710", "timelock":""}
farm_polycloud = {"network":"polygon", "name": "polycloud", "masterchef": "90d7219bfe2dedca9ef5bdf599141f2c6eb36248", "timelock":""}
farm_jetswap_p = {"network":"polygon", "name": "jetswap polygon", "masterchef": "0x4e22399070ad5ad7f7beb7d3a7b543e8ecbf1d85", "timelock":""}
farm_polygarden = {"network":"polygon", "name": "polygarden", "masterchef": "0x0fAbd04f68Ff13a72eb1542201a211eE70feBA5F", "timelock":""}
farm_polygarden_rug = {"network":"polygon", "name": "polygarden (rugged)", "masterchef": "0x2C37983e0C763894Cf40846aF6F483B70474CA0f", "timelock":""}
farm_polytoken = {"network":"polygon", "name": "polytoken", "masterchef": "9c7afe8e0a0d945bf91d71a655c4a7d15c48e58e", "timelock":""}
farm_polygorilla = {"network":"polygon", "name": "polygorilla", "masterchef": "0xf0168d40aAFaa078DeB86B321941CE35AE5661E9", "timelock":""}
farm_polycrystal = {"network":"polygon", "name": "polycrystal", "masterchef": "0xeBCC84D2A73f0c9E23066089C6C24F4629Ef1e6d", "timelock":""}
farm_polycrystal_USDC = {"network":"polygon", "name": "polycrystal USDC staking pool", "masterchef": "0x4E9e19B2943c74A2A6f801Be0421eD3c563b83E9", "timelock":""}
farm_spiderman = {"network":"polygon", "name": "spiderman", "masterchef": "0xa7439172de1343a2f640c36ecfb576706283504b", "timelock":""}
farm_polynabi = {"network":"polygon", "name": "polynabi", "masterchef": "0xdfb723f35fb51d801e664821d079790365747c47", "timelock":""}






# dictionary template = {"network":"polygon", "name": "", "masterchef": "", "timelock":""}

farm_popit = {"network": "bsc", "name": "popit", "masterchef": "0xa356097644cB4e0bCF939aCE69A719849521Cd8B","timelock": ""}
farm_stablemagnet = {"network": "bsc", "name": "stablemagnet","masterchef": "0xf6E62b59DbD8C8395321F886bd06eCf04f57C088", "timelock": ""}
farm_robinhood = {"network": "bsc", "name": "robinhood", "masterchef": "0xd4DC714a68638ffc5EC24441FE37e9dDa677467a","timelock": ""}
farm_privacyswap = {"network": "bsc", "name": "privacyswap", "masterchef": "0xD8151Da76095264929ab7cB680457c18014D2f9d","timelock": "0xa78515e2eD5ee06738DDD6d014c29a75aF13Cb36"}
farm_privacyswapv2 = {"network":"bsc", "name": "privacyswap V2", "masterchef": "0x75dDFFF9810eE13AC45d49D6606B2fBFE9B90FB0", "timelock":""}
farm_lightningdragon = {"network":"bsc", "name": "lightning dragon", "masterchef": "0xC66445ca849c21B4Fc245CB8536578b79623F794", "timelock":""}
farm_churro = {"network":"bsc", "name": "churro", "masterchef": "0x6930701D7278B1665F9Fc2d0820F2C713C123e9C", "timelock":""}
farm_moneytime = {"network":"bsc", "name": "moneytime", "masterchef": "0x7d3c7d762035Bc75789a941f50a81bab8638c856", "timelock":""}
farm_jaguarevo = {"network":"bsc", "name": "jaguar evolution", "masterchef": "0xe11BdE767Edb8dE456833c8a0a5AA95F12929218", "timelock":""}
farm_frozencake = {"network":"bsc", "name": "frozencake", "masterchef": "0x02bFCe87315191E061595F5D5d34B69CD4b9239B", "timelock":""}
farm_rediant_bsc = {"network":"bsc", "name": "rediant", "masterchef": "0x5979959483b4aAFa6a94Ba8dA6Aa406C31D06cb6", "timelock":""}
farm_nekocat = {"network":"bsc", "name": "nekocat", "masterchef": "0x77F7518e4dA5240EcCC7e5a673e5FF3759eaD795", "timelock":""}
farm_venom = {"network":"bsc", "name": "venom", "masterchef": "0x92B4fD4eACb2893c03e62e3b8A480421a912f9DD", "timelock":""}
farm_backtothedefi = {"network":"bsc", "name": "back to the defi", "masterchef": "0x8ACdD83803242c16e50828D1b97E266c6B513d17", "timelock":""}
farm_torcash = {"network":"bsc", "name": "torcash", "masterchef": "0xfe8fac74Da035323Fb702B99230e7E29F31fA64D", "timelock":""}
farm_atar = {"network":"bsc", "name": "atar", "masterchef": "0xC4aC498C22351cF6E26261b3B7428de8dAe3f654", "timelock":""}
farm_trident = {"network":"bsc", "name": "trident", "masterchef": "0x4cf32518b713eC6D2e67AFeAC945c5013acBbC4E", "timelock":""}
farm_pantherswap = {"network":"bsc", "name": "pantherswap", "masterchef": "0x058451C62B96c594aD984370eDA8B6FD7197bbd4", "timelock":""}
farm_lungtoo = {"network":"bsc", "name": "lungtoo", "masterchef": "0xa9dC1c94899C37cCC070d818607032e4E735D5fA", "timelock":""}
farm_lungtoov2 = {"network":"bsc", "name": "lungtoov2", "masterchef": "0xe203d9b564Fd0ebcA9747203aeD496aFB9C87c3F", "timelock":""}
farm_lavacake = {"network":"bsc", "name": "lavacake", "masterchef": "0xfbfae2D489Bb649C7f33d9812b2Dcf17E9bb279C", "timelock":""}
farm_kittycoin = {"network":"bsc", "name": "kittycoin", "masterchef": "0xF8Cee793C00e56f8e9f1517daB77831444529192", "timelock":""}
farm_dexterlab = {"network":"bsc", "name": "dexter lab", "masterchef": "0xE02D0FBd638a4584Fe22F3f982088C26A336560B", "timelock":""}
farm_cowswap = {"network":"bsc", "name": "cowswap", "masterchef": "0x9f9704E70483692127f47564a1b5a377aD2c189c", "timelock":""}
farm_beeswap = {"network":"bsc", "name": "beeswap", "masterchef": "0xc5a10bfadc3c4efb317f4cf01a4af9fc83db755f", "timelock":""}
farm_trees = {"network":"bsc", "name": "trees", "masterchef": "0x5e93da2f630d88b2da0d33c84bd215c61a6e344e", "timelock":""}
farm_puswap = {"network":"bsc", "name": "puswap", "masterchef": "0xa9fe1666a06b63851f5e342741e16df08e0bf261", "timelock":""}
farm_triton = {"network":"bsc", "name": "triton", "masterchef": "0xF8927D7911168B222237A5050f28C8c95e201eC8", "timelock":""}
farm_sabretooth = {"network":"bsc", "name": "sabretooth", "masterchef": "0x0febb4523520ea2e0593014E5634Ad7345ac2C1e", "timelock":""}
farm_whiteteethswap = {"network":"bsc", "name": "whiteteeth swap", "masterchef": "0x9c3c77a2f788e0201fb0cbce025f4efd76d9ba05", "timelock":""}
farm_newb = {"network":"bsc", "name": "newb", "masterchef": "0x6eC9f515F0c8803f8b2D49dE61d794eDf2A0119d", "timelock":""}
farm_goldfarm = {"network":"bsc", "name": "gold farm", "masterchef": "0x2DD77Fa9903c23b359470f17d69A8e25bC9Ec032", "timelock":""}
farm_rasta = {"network":"bsc", "name": "rasta", "masterchef": "0xec89Be665c851FfBAe2a8Ded03080F3E64116539", "timelock":""}
farm_thefinalfinance = {"network":"bsc", "name": "the final finance", "masterchef": "0xf495c5f39598B49762DcF1A76adA628059Bbc9aa", "timelock":""}
farm_fungi = {"network":"bsc", "name": "fungi finance", "masterchef": "0x894E508f808a7a4B380FF6b8078FeD716c47721C", "timelock":""}







# dictionary template = {"network":"bsc", "name": "", "masterchef": "", "timelock":""}

# Input target farm
target_farm = farm_polynabi

# ============ Autonomous script starts here ==============

mode = eval(target_farm["network"])

web3 = Web3(Web3.HTTPProvider(mode["rpc"]))
url = mode["scanner"]
getAPI = "&apikey=" + mode["apikey"]

record_name = target_farm["name"]
record_MC = target_farm["masterchef"]
record_TL = target_farm["timelock"]
record_network = target_farm["network"]

print("Farm name is:", record_name, "on", record_network)

MC_address = web3.toChecksumAddress(record_MC)
print("Checking masterchef address:", MC_address)

#makeAPI

MC_API_URL= url + "&module=contract" + "&action=getabi" + "&address=" + MC_address + getAPI
MC_ABI = requests.get(MC_API_URL).json()["result"]
MC_ABI_result = json.loads(MC_ABI)
MC_contract = web3.eth.contract(address=MC_address, abi=MC_ABI)

MC_contract_type = str.split(MC_ABI_result[0]["inputs"][0]["internalType"])[0]
MC_contract_name = str.split(MC_ABI_result[0]["inputs"][0]["internalType"])[-1]
print("Address is type:", MC_contract_type, ". Name of address is", MC_contract_name)


MC_owner_address = MC_contract.functions.owner().call()
print("Masterchef owner address:", MC_owner_address)

owner_valid = True
try:
    MC_owner_API_URL = url + "&module=contract" + "&action=getabi" + "&address=" + MC_owner_address + getAPI
    MC_owner_ABI = requests.get(MC_owner_API_URL).json()["result"]
    MC_owner_ABI_result = json.loads(MC_owner_ABI)
    MC_owner_contract = web3.eth.contract(address=MC_owner_address, abi=MC_owner_ABI)
    MC_owner_contract_type = str.split(MC_owner_ABI_result[0]["inputs"][0]["internalType"])[0]
    MC_owner_contract_name = str.split(MC_owner_ABI_result[0]["inputs"][0]["internalType"])[-1]
    print("Address is type:", MC_owner_contract_type, ". Name of address is", MC_owner_contract_name)
except:
    owner_valid = False
    print("Masterchef owner is a fucky address.")

def checkTimelock(contract):
    timelock_status = False
    delay = 0
    try:
        fn_list = contract.all_functions()

        for i in range(len(fn_list)):
            if "delay" in fn_list[i].fn_name:
                print("Contract is a Timelock contract")
                delay = contract.functions.delay().call()
                print("Current delay value in Timelock is", delay)
                timelock_status = True
    except:
        print("Timelock contract not smart contract")

    return timelock_status, delay

if owner_valid:
    checkTimelock(MC_owner_contract)

MC_poollength = MC_contract.functions.poolLength().call()

poolinfo_index = 0
for i in range(1, len(MC_ABI_result)):
    if "poolInfo".casefold() in MC_ABI_result[i]["name"].casefold():
        poolinfo_index = i
        # print("poolinfo is in index:", poolinfo_index)
        break

poolinfo_list = []
for i in range(len(MC_ABI_result[poolinfo_index]["outputs"])):
    poolinfo_list.append(MC_ABI_result[poolinfo_index]["outputs"][i]["name"])

token_address_index = 0
for i in range(len(MC_ABI_result[poolinfo_index]["outputs"])):
    if "token" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold():
        token_address_index = i
        # print("token address is in index:", token_address_index)
        break

depositfee_index = 0
for i in range(len(MC_ABI_result[poolinfo_index]["outputs"])):
    if "depositf" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold():
        depositfee_index = i
        # print("depositfeeBP is in index:", depositfee_index)
        break
    else:
        depositfee_index = None

withdrawalfee_index = 0
for i in range(len(MC_ABI_result[poolinfo_index]["outputs"])):
    if "unstak" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold() or "withdraw" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold() or "harvestf" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold():
        withdrawalfee_index = i
        # print("withdrawalfeeBP is in index:", withdrawalfee_index)
        break
    else:
        withdrawalfee_index = None

transfertax_index = 0
for i in range(len(MC_ABI_result[poolinfo_index]["outputs"])):
    if "transfert" in MC_ABI_result[poolinfo_index]["outputs"][i]["name"].casefold():
        transfertax_index = i

        break
    else:
        transfertax_index = None

pool_token_addresses = []
pool_deposit_fees = []
pool_withdrawal_fees = []
pool_transfer_fees = []

for i in range(MC_poollength):
    pool_token_addresses.append(MC_contract.functions.poolInfo(i).call()[token_address_index])
    if depositfee_index is not None:
        pool_deposit_fees.append(MC_contract.functions.poolInfo(i).call()[depositfee_index])
    if withdrawalfee_index is not None:
        pool_withdrawal_fees.append(MC_contract.functions.poolInfo(i).call()[withdrawalfee_index])
    if transfertax_index is not None:
        pool_transfer_fees.append(MC_contract.functions.poolInfo(i).call()[transfertax_index])

# print(pool_token_addresses)
# print(pool_deposit_fees)
# symbolOnOff = "on"  # To display token symbols or not

def getLPcontent(address):          #address is pool address as per each poolinfo "lpToken" address
    # print("Compiling for LP1")
    if mode == eval("bsc"):
        time.sleep(0.5)
    LPcontentAPI = url + "&module=account" + "&action=tokentx" + "&address=" + address +"&page=1&offset=3&sort=desc" + getAPI  #only works for LP token pair due to availability of ERC-20 token transactions
    LPcontentAPI_result = requests.get(LPcontentAPI).json()["result"]
    LPcontent = []      #this list will store ALL tokens found
    LP_content_deduplicated = []        #this list should only store one copy of each token
    symbolOnOff = "off"  # To display token symbols or not


    if LPcontentAPI_result is None:
        # return ["Unable to decipher"]
        pass

    else:
        for i in range(len(LPcontentAPI_result)):
            if "off" in symbolOnOff:
                LPcontent.append(LPcontentAPI_result[i]["tokenName"])
            else:
                LPcontent.append(LPcontentAPI_result[i]["tokenSymbol"])

            # print(LPcontent)

        for i in LPcontent:
            if i not in LP_content_deduplicated:
                LP_content_deduplicated.append(i)
    # print("LP1:", LP_content_deduplicated)
    # print("compiling for LP2")
    LPcontentAPI2 = url + "&module=account" + "&action=tokentx" + "&contractaddress=" + address + "&page=1&offset=20&sort=desc" + getAPI  # only works for LP token pair due to availability of ERC-20 token transactions
    LPcontentAPI2_result = requests.get(LPcontentAPI2).json()["result"]

    LPcontent2 = []  # this list will store ALL tokens found
    LP_content2_deduplicated = []  # this list should only store one copy of each token

    if LPcontentAPI2_result is None:
        # return ["Unable to decipher"]
        pass

    else:
        for i in range(len(LPcontentAPI2_result)):
            if "off" in symbolOnOff:
                LPcontent2.append(LPcontentAPI2_result[i]["tokenName"])
            else:
                LPcontent2.append(LPcontentAPI2_result[i]["tokenSymbol"])

        for i in LPcontent2:
            if i not in LP_content2_deduplicated:
                LP_content2_deduplicated.append(i)

    # print("LP2: ", LP_content2_deduplicated)

    swap_tokens = []
    for i in LP_content2_deduplicated:

        try:
            uniswap_address = web3.toChecksumAddress(address)
            uniswapv2_url = url + "&module=contract" + "&action=getabi" + "&address=" + uniswap_address + getAPI
            uniswap_abi = requests.get(uniswapv2_url).json()["result"]
            # print(uniswap_abi)
            uniswap_abi_result = json.loads(uniswap_abi)
            uniswap_contract = web3.eth.contract(address=uniswap_address, abi=uniswap_abi)


            tokenID = []
            for i in range(len(uniswap_contract.all_functions())):
                if "token" in uniswap_contract.all_functions()[i].fn_name.casefold():
                    tokenID.append(uniswap_contract.all_functions()[i].fn_name)
            # print(tokenID)

            swap_token_addresses = []
            for i in tokenID:
                eval("swap_token_addresses.append(uniswap_contract.functions." + i + "().call())")
            # print(swap_token_addresses)

            swap_tokens = []
            for i in swap_token_addresses:
                LPcontentAPI2 = url + "&module=account" + "&action=tokentx" + "&contractaddress=" + i + "&page=1&offset=1&sort=desc" + getAPI  # only works for LP token pair due to availability of ERC-20 token transactions
                LPcontentAPI2_result = requests.get(LPcontentAPI2).json()["result"]

                if LPcontentAPI2_result is None:
                    # return ["Unable to decipher"]
                    pass

                else:
                    for i in range(len(LPcontentAPI2_result)):
                        if "off" in symbolOnOff:
                            swap_tokens.append(LPcontentAPI2_result[i]["tokenName"])
                        else:
                            swap_tokens.append(LPcontentAPI2_result[i]["tokenSymbol"])
        except:
            print("LP components query failure")
            pass

    # print("swap tokens:", swap_tokens)
    # print("LP2 check #2: ", LP_content2_deduplicated)
    consolidated_list = LP_content2_deduplicated + swap_tokens #+ LP_content_deduplicated      #only save LP_content2 if filtering for  single-coin farms
    # print("consolidated list:", consolidated_list)
    consolidated_list_deduplicated = []

    for i in consolidated_list:
        if i not in consolidated_list_deduplicated:
            consolidated_list_deduplicated.append(i)
    # print("consolidated list deduplicated:", consolidated_list_deduplicated)

    return consolidated_list_deduplicated

run_lp = True

if run_lp:
    # try:
    print("======= Checking tokens in pools =========")
    print("poolinfo consists of:", poolinfo_list)

    filter_list = ['Buy SpaceRat (SpaceRat.Finance)', 'Go Buy Polydoge', 'Go Buy SpaceRat at SpaceRat.Finance',
                   'Kommunitas', 'TOMO (tomochain.top)', 'PumpBooty', 'www.METH.co.in', 'Matic Ruletka', 'Polyfck',
                   'stonky.farm STONKY', 'Mako', 'PolyPingu', 'Krill', 'RebalanceGovernance Token', 'LitCoin',
                   'GO BUY POLYSAFU https://t.me/polySAFU_official', 'PolyCum', 'SPAM', 'Solid (PoS)', 'TURKLIRASI',
                   'ATATURK', 'AzCoin', 'https://exhentai.org/tag/artist:rikose', 'Orbit Bridge Polygon Token', 'ApeAgain',
                   'Wootrade Network (PoS)', 'Fortune Cat Coin (PoS)', 'PolyMeow', 'SafeLips', 'FishFishvault', 'Dai Stablecoin',
                   'Aave Matic Market DAI', 'polyRocket', 'PolyBank', 'WINDOWS', 'PolyPanty', 'WolfSwap Token', 'moonwolf.io']

    MC_tokens = []

    print("Number of pools in " + MC_contract_name + " Masterchef: " + str(len(pool_token_addresses)))

    for i in range(len(pool_token_addresses)):
        current_pair = getLPcontent(pool_token_addresses[i])    # record current tokens in variable
        new_pair = []   # make transition empty list

        for j in range(len(current_pair)):  # checking through each item in current_pair
            if current_pair[j] not in filter_list:  # check if item is inside filter list
                new_pair.append(current_pair[j])    # not in filter list? append into new_pair

        MC_tokens.append(new_pair)

    # for i in range(len(MC_tokens)):
    #     if withdrawalfee_index is not None:
    #         print("poolID: " + str(i) + "." + " Address: " + str(pool_token_addresses[i]) + ". Deposit fee: " + str(pool_deposit_fees[i]/100) + "%." + " Withdrawal Fee:" + str(pool_withdrawal_fees[i]/100)+ ". Tokens:" + str(MC_tokens[i]))
    #     else:
    #         print("poolID: " + str(i) + "." + " Address: " + str(pool_token_addresses[i]) + ". Deposit fee: " + str(pool_deposit_fees[i]/100) + "%." + " Tokens:" + str(MC_tokens[i]))

    if depositfee_index is not None:
        for i in range(len(pool_deposit_fees)):
            pool_deposit_fees[i] = pool_deposit_fees[i]/100

    if withdrawalfee_index is not None:
        for i in range(len(pool_withdrawal_fees)):
            pool_withdrawal_fees[i] = pool_withdrawal_fees[i]/100

    if transfertax_index is not None:
        for i in range(len(pool_transfer_fees)):
            pool_transfer_fees[i] = pool_transfer_fees[i]/100

    pool_ids = list(range(MC_poollength))

    table = {"poolID": pool_ids, "tokens": MC_tokens}

    if depositfee_index is not None:
        table = {**table, **{"deposit fee %": pool_deposit_fees}}

    if withdrawalfee_index is not None:
        table = {**table, **{"withdraw fee %": pool_withdrawal_fees}}

    if transfertax_index is not None:
        table = {**table, **{"transfer fee %": pool_transfer_fees}}

    table = {**table, **{"address": pool_token_addresses}}

    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))


print("========= CHECKING FOR CODE CHECKPOINTS =========")
# def codeChecker(address):
address = MC_address

sourcecodeAPIcallURL = url + "&module=contract" + "&action=getsourcecode" + "&address=" + address + getAPI
sc = requests.get(sourcecodeAPIcallURL)  # APICALL
contract_sc = sc.json()["result"][0]["SourceCode"]
contract_sc = re.sub(r'\r\n', '', contract_sc)
contract_sc = re.sub(r'\\n\\n', '', contract_sc)
contract_sc = re.sub(r'\\n', '', contract_sc)
contract_sc = re.sub(r'\\u003c', '<', contract_sc)
contract_sc = re.sub(r'  ', '', contract_sc)

# ownerConstructor = re.findall("(?im)contract Ownable\s[\s\S]{0,100}address\s[\S]{0,10}\s([\s\S]{0,20});", contract_sc)
# print("ownerConstructor output: ", ownerConstructor)

ownerConstructor = re.findall("(?:address\sprivate\s([\w_]{0,20});)+", contract_sc)
print("ownerConstructor (private addresses) output: ", ownerConstructor)

onlyownermodifier = re.findall("(?im)function [get]{0,1}(?:owner|operator)[\s\S]{0,100}return\s([\S]{0,20});", contract_sc)
print("onlyOwner modifier output:", onlyownermodifier)

doubleownerfinder = re.findall("(?i)[_]{2,10}owner", contract_sc)
print("__owner finder output:", doubleownerfinder)

maximumvariablesfinder = re.findall("(?i)(max(?:imum){0,1}[\w]{0,60}[\s=]{0,5}[\w]{0,10});",contract_sc)
print("maximum variables finder output:", maximumvariablesfinder)


constantsfinder = re.findall("(?i)public\sconstant\s([^;]+)", contract_sc)
constantsfinder2 = re.findall("(?i)private\sconstant\s([^;]+)", contract_sc)
print("constants output:", constantsfinder + constantsfinder2)


# TO-DO Make private variables checker
# TO-DO Make all require==XXX checker

depositFeeBPfinder = re.findall("(?i)function\s([\w]{2,30})[\s\S]{0,200}(require[\s\S]{0,20}depo[\s\S]{0,60}),", contract_sc)
# depositFeefinder = re.findall("(?i)depositfee[ <=1234567890()\n]{0,20}", contract_sc)
print("depositFeefinder output:", depositFeeBPfinder)

withdrawalFeeBPfinder = re.findall("(?i)function\s([\w]{2,30})[\s\S]{0,150}(require[\s\S]{0,20}(?:withd|unsta)[\s\S]{0,50}),", contract_sc)
print("withdrawalFeeBPfinder/unstakingfeefinder output:", withdrawalFeeBPfinder)

withdrawalFeefinder = re.findall("(?i)_withdrawalfee[ <=1234567890()]{3,10}", contract_sc)
earlywithdrawalFeefinder = re.findall("(?i)earlywithdrawalfee[ <=1234567890()]{3,10}", contract_sc)
withdrawalpenaltyfinder = re.findall("(?i)withdraw[a-zA-Z]{0,5}penalty[ <=1234567890()]{3,10}", contract_sc)
print("withdrawalfinder output:", withdrawalFeefinder + earlywithdrawalFeefinder + withdrawalpenaltyfinder)

Withdrawfuckerfinder = re.findall("(?i)function\s([\w]{0,15}withdraw)[\s\S]{0,50}address\s([\w]{0,10})\)[\s\S]{0,400}emit\s[\w]{0,15}withdraw\(([\w]{0,10}),", contract_sc)
print("Withdrawfuckerfinder output:", Withdrawfuckerfinder)
for i in range(len(Withdrawfuckerfinder)):
    if Withdrawfuckerfinder[i][1] != Withdrawfuckerfinder[i][2]:
        print("***** DEV IS FUCKING WITH", Withdrawfuckerfinder[i][0], "! *****")

emergencywithdrawfinder = re.findall("(?i)function\s([\S]*?withdraw[\S]{0,20})\([\s\S]*?public[\s\S]*?(emit\s\w+?)\(", contract_sc)
print("all public withdrawal functions finder:", emergencywithdrawfinder)
if len(emergencywithdrawfinder) == 0:
    print("******* WARNING!!!! THIS CONTRACT HAS NO PUBLIC  WITHDRAWAL!!! *******")

withdrawbyowner = re.findall(
    "(?i)function\s([\S]{0,20}withdraw[\S]{0,20})\([\s\S]{0,50}only(?:[\S]{3,15})", contract_sc)
print("Withdrawbyowner output:", withdrawbyowner)

migratorfinder = re.findall("(?i)function\s(\S*migrat\S*)\(", contract_sc)
print("migratorfinder output:", migratorfinder)

# devsenderfinder = re.findall("(?im)(function\s[a-z]{0,30})[\s\S]{0,50}(require\(msg.sender\s==\s[\w]{0,30})[\s\S]{0,200}(emit\s[\s\S]{0,80});", contract_sc)
# print("devsenderfinder outout:", devsenderfinder)

# requiremsgsender = re.findall("(?i)function\s([\S]{0,30})\([\S\s]{0,50}require\(([\s\S]{0,50}\s==\s[\s\S]{0,50}),", contract_sc)
# print("requiremsgsender function finder output:", requiremsgsender)

requiremsgsender = re.findall("(?i)function\s(\w{0,30})[\s\S]{0,150}(require\([\S\s]{0,50}),[\s\S]{0,100}(emit\s\w{0,30})", contract_sc)
print("requiremsgsender function finder output:", requiremsgsender)

#
# onlyownerfinder = re.findall("(?i)function\s([\S]{0,30})\([\s\S]{0,50}only(?:owner|operator|admin|developer)",contract_sc)
# print("OnlyOwner/operator/admin/developer function finder output:", onlyownerfinder)

onlyownerfinder = re.findall("(?i)function\s([\S]{0,30})\([\s\S]{0,150}(only(?:[a-z]{3,15}))",contract_sc)
print("OnlyOwner/operator/admin/developer function finder output:", onlyownerfinder)

setfunctionfinder = re.findall("(?i)function\sset\([\s\S]*?}[\s\S]*?}", contract_sc)
pooltokenfucker = re.findall("(?i)pooli[\s\S]*?[\s\S]*?;", setfunctionfinder[0])
print("pooltokenfucker output:", pooltokenfucker)

    # pass



# codeChecker(MC_address)

tock = time.time()
ticktock = tock-tick
print(f"Total time elapsed for this query: {ticktock:.2f} seconds")