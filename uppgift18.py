from datetime import datetime

nu = datetime.now()

print("nu = ", nu)

dt_string = nu.strftime("%d/%m/%Y %H:%M:%S")
print("datum och tid =", dt_string)	