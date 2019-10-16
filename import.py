import listrik

def main():
    #Tegangan
    i = 3
    r = 5

    v = listrik.tegangan(i, r)

    print("MENGHITUNG TEGANGAN")
    print("Arus\t\t: ", i)
    print("Hambatan\t: ", r)
    print("Tegangan\t= ", v)

    #Arus
    v = 12
    r = 6

    i = listrik.arus(v, r)

    print("\nMENGHITUNG ARUS")
    print("Tegangan\t: ", v)
    print("Hambatan\t: ", r)
    print("Arus\t\t= ", i)

    #Hambatan
    v = 15
    i = 5

    r = listrik.hambatan(v, i)
    print("\nMENGHITUNG HAMBATAN")
    print("Tegangan\t: ", v)
    print("Arus\t\t: ", i)
    print("Hambatan\t= ", r)

if __name__ == "__main__":
    main()
