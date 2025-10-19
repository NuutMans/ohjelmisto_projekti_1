def gallonat_litroiksi(gallona):
    return gallona * 3.785


app_running = True

while app_running:
    gallona = float(input("Anna gallonat (jos negatiivinen, ohjelma loppuu): "))
    if gallona < 0:
        app_running = False


    else:
        litrat = gallonat_litroiksi(gallona)
        print(f"{gallona} gallonaa on {litrat:.2f} litraa.")













