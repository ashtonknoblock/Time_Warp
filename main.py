import string
import random

def generate_key():
    alphabet = string.ascii_letters + string.digits
    ash = ['A', 'S', 'H', 'a','s', 'h']
    ton = ['T', 'O', 'N', 't', 'o', 'n' '0']


    p1 = ''.join(random.choice(alphabet) for i in range(5))
    p2 = ''.join(random.choice(alphabet) for i in range(10))
    p3 = ''.join(random.choice(alphabet) for i in range(5))
    p4 = ''.join(random.choice(alphabet) for i in range(5))
    p5 = ''.join(random.choice(alphabet) for i in range(10))
    p6 = ''.join(random.choice(alphabet) for i in range(5))
    p7 = ''.join(random.choice(alphabet) for i in range(10))

    chunk1 = random.choice(ash)
    chunk2 = random.choice(ash)
    chunk3 = random.choice(ash)
    chunk4 = random.choice(ton)
    chunk5 = random.choice(ton)
    chunk6 = random.choice(ton)

    password = p1+chunk1+p2+chunk2+p3+chunk3+p4+chunk4+p5+chunk5+p6+chunk6+p7
    return password
  
def validate_key(key):
    ash = 'ASHash'
    ton = 'TONton0'

    if key[5] in ash:

        if key[16] in ash:

            if key[22] in ash:

                if key[28] in ton:
                
                    if key[39] in ton:

                        if key[45] in ton:
                            return True
    else:
        return False


if __name__ == "__main__":
    generate_key()
    print("Testing with key XSsBaAhN6DRUkz34sglgVwHRaFMjtl9XoxCSh1w0x0C3NnwX7gSbrhAy: (should be True)")
    print(validate_key("XSsBaAhN6DRUkz34sglgVwHRaFMjtl9XoxCSh1w0x0C3NnwX7gSbrhAy"))
    print

    print("Testing with key 3FinHAxJSQzlHqUzswphy1aQ3R1otehqOOzZjAct79R7JNqy5sDtOKoI: (should be True) ")
    print(validate_key("3FinHAxJSQzlHqUzswphy1aQ3R1otehqOOzZjAct79R7JNqy5sDtOKoI"))
    print

    print("Testing with key XSsBaqhN6DRUkz34rglgVwHRaFMjtl9XoxCSh1wUW201BACsagSbrhAy: (should be False)")
    print(validate_key("XSspofmN6DRUkz34pglgVw3RaFMjtl9XoxCSh1w0x0C3NnwX7gSbr0cP"))
    print

    print("Testing with key NtseMA680AIpToS8sqh6xQHLSfS4tAIMUnEysDL05JahDnOSMu8rfJzo: (should be False)")
    print(validate_key("XSsBauhN6DRUkz34sglgVwHRaFMjtl9XoxCSh1w0x0C3NnwX7gSbrhAy"))
    print


