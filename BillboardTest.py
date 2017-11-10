def topCharts():

    import billboard
    user_command = input("What would you like to know? ")
    if 'number 1 song' in user_command:
        
        chart = billboard.ChartData('hot-100')
        topsong = chart[0]
        print(topsong)
    if 'top 10 songs' in user_command:
        chart = billboard.ChartData('hot-100')
        top10 = chart[0:11]
        print(top10)

topCharts()
