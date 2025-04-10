

def greet(name: str) -> str:
   
    return f"Hello, {name}!"


def main():
   
    name = "World"
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
