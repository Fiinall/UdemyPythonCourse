print(""" ----------- Hi! ----------- 
    
        Tell me what you got and I'll tell you what you have
    
    I can specify, is your polygon rectangle or square or any kind of triangle
    
    Please selecet the edge number of your polygon
    
""")

Edge_Number  = int(input("How many egdes your polygon have : "))

print("Okey, Now, Please Enter the Edge Lengths of Your {} - Sided Polygon".format(Edge_Number))

if (Edge_Number == 3) :
    Edge_1 = int(input("What is the first edge of your polygon : "))
    Edge_2 = int(input("What is the second edge of your ploygon : "))
    Edge_3 = int(input("What is the third edge of your polygon : "))
    print("Great!, Let's look at the type of the triangle")
    situaiton = True
    '''
        Örneğin [3,3,8] gibi girdiler geldiğinde yani gerçek üçgen olmadığında ikizkenarlığı kontrol eden if bloğuna girmesin diye ek bir koşul 
        Alttaki if bloklarını elif bloğuna çevirmek daha mantıklı olur mu ?
    '''
    if ((Edge_1 >= Edge_3 + Edge_2) or (Edge_1 <= abs(Edge_2 - Edge_3)) or (Edge_2 >= Edge_3 + Edge_1) or (Edge_2 <= abs(Edge_1 - Edge_3)) or (Edge_3 >= Edge_1 + Edge_2) or (Edge_3 <= abs(Edge_2 - Edge_1))) :
       print("This is not a triangle")
       situaiton = False
        # Controlling triangularness
            """ Geliştirme Önerisi : Allta kalan if'leri en genel kural olan üçgen olma şartının anltında elif şeklinde olabilir.
            """

    if (Edge_1 == Edge_2 and Edge_1 == Edge_3) :
        print("You have Equilateral Triangle with {} units on each side ".format(Edge_2))
        # Questioning the Equilateralness
    if (((Edge_1 == Edge_2 and Edge_3 != Edge_2) or (Edge_1 == Edge_3 and Edge_2 != Edge_1) or (Edge_3 == Edge_2 and Edge_1 != Edge_2)) and  situaiton == True ):
        print("You have Isosceles Triangle with {} units isosceles edges and {} units the other edge") # ikisi aynı olan 3 girdiden aynı olan ikisini seçmeyi öğrenince burayı tamamlayacağım :)
        # Questioning the Isosceles
    if (Edge_1 == 0 or Edge_2 == 0 or Edge_3 == 0 ) :
        print ("At least one of your entries is 0. Any edge of a triangle can not be = 0 ")
    if (Edge_1 != Edge_2 and Edge_2 != Edge_3 and situaiton == True) :
        print ("The triangle has three different edges")





