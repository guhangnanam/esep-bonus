from db import inMemoryDB



def main():

    db = inMemoryDB()

    print("\n===== TEST 1: get missing key =====")
    print(db.get("x"))


    print("\n===== TEST 2: get wrong key type =====")
    print(db.get(123))


    print("\n===== TEST 3: put without transaction =====")
    print(db.put("a", 10))


    print("\n===== TEST 4: begin transaction =====")
    print(db.begin_transaction())


    print("\n===== TEST 5: put inside transaction =====")
    print(db.put("a", 5))


    print("\n===== TEST 6: value not yet committed =====")
    print(db.get("a"))


    print("\n===== TEST 7: commit transaction =====")
    print(db.commit())


    print("\n===== TEST 8: value should now be committed =====")
    print(db.get("a"))


    print("\n===== TEST 9: overwrite in new transaction =====")
    print(db.begin_transaction())
    print(db.put("a", 99))
    print(db.get("a"))
    print(db.commit())

    print("\n===== TEST 10: overwrite committed =====")
    print(db.get("a"))


    print("\n===== TEST 11: rollback test =====")
    print(db.begin_transaction())
    print(db.put("b", 123))
    print("Before rollback, b =", db.get("b"))
    print(db.rollback())
    print("After rollback, b =", db.get("b"))


    print("\n===== TEST 12: begin_transaction twice =====")
    print(db.begin_transaction())
    print(db.begin_transaction())
    print(db.rollback())


    print("\n===== TEST 13: commit without transaction =====")
    print(db.commit())


    print("\n===== TEST 14: rollback without transaction =====")
    print(db.rollback())


    print("\n===== TEST 15: multiple puts, single commit =====")
    print(db.begin_transaction())
    print(db.put("x", 1))
    print(db.put("y", 2))
    print(db.put("z", 3))
    print(db.commit())
    print(db.get("x"), db.get("y"), db.get("z"))


if __name__ == '__main__':
    main()

