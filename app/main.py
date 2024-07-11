from utils.instagram import Instagram

def use_ig():
    a = Instagram()

    try:
        a.exect()
        print("El proceso se ha ejecutado correctamente")

    except Exception as e:
        print(f"Error Messagge: {e} ")
        return

if __name__ == "__main__":
    use_ig()