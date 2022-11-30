from django.http import HttpResponse


def info(request,name,age):
    return HttpResponse(f"""<h2>About</h2>  <br> <p>Имя: {name}</p> <br> <p>Возраст: {age}</p>""")

def about(request,City,oc,s):
    return HttpResponse(f"""<h2>About (стр.2)</h2> <br> <p>Откуда: {City}</p> <br> <p>Успеваемость в школе: {oc}</p> <br> <p>Люблю ли я учиться:{s}</p>""")

def contact(request,Tg,Github,tel):
    return HttpResponse(f"""<h2>Contact </h2> <br> <p>Мой телеграмм: {Tg}</p> <br> <p>Номер телефона: {tel}</p> <br> <p>Мой GitHub: {Github}</p>""")

