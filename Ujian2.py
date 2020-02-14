import xlsxwriter


def segitigaExcel(x):
    x = x.replace(' ', '')
    if len(x) < 10:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
    else:

        workbook = xlsxwriter.Workbook('ujian.xlsx')     # file name
        worksheet = workbook.add_worksheet('Data')      # sheet name

        star = list(x)
        x = 0
        y = 0
        for i in range(0, int(len(star)/2)):
            for j in range(0, i+1):
                worksheet.write(i, j, star[x])     # row, col, data
                x += 1
            y += 1
            print()
            if(x == len(star)):
                break
        workbook.close()


segitigaExcel('Purwadhika')
