casos = int(input())
for i in range(casos):
    led=0
    num = input()
    for j in num:
        if j=="1":
            led=led+2
        elif j=="2" or j == "3" or j =="5":
            led = led+5
        elif j=="4":
            led = led+4
        elif j=="0" or j=="9" or j=="6":
            led = led+6
        elif j=="8":
            led=led+7
        elif j=="7":
            led=led+3
    print(str(led)+ " leds")
