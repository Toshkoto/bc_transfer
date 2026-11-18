def main() -> None:
    while True:
        ans = input("login [1], register [2]")

        if not ans.isdigit() or int(ans) not in [1, 2]:
            print("🖕🖕🖕🖕")
            continue

if __name__ == "__main__":
    main()
