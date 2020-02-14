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
        row = 0
        for i in range(0, int(len(star)/2)):
            for j in range(0, i+1):
                print(star[x], end=' ')
                x += 1
            for a in star:
                worksheet.write(row, row, a)     # row, col, data
                row += 1

            workbook.close()
            y += 1
            print()
            if(x == len(star)):
                break

    segitigaExcel('Purwadhika')
    # segitigaExcel('Purwadhika Startup and Coding School @BSD')
    # segitigaExcel('kode')
    # segitigaExcel('kode python')
    # segitigaExcel('Lintang')
# with xlsxwriter.Workbook('tesujian.xlsx') as workbook:
#                 worksheet = workbook.add_worksheet()
#                 for row_num, data in enumerate(star):
#                     worksheet.write_row(row_num, 0, data)


# data = [
#     [1, 'Andi', 'Jakarta'],
#     [2, 'Budi', 'Bandung'],
#     [3, 'Caca', 'Jakarta'],
# ]

# Iterate over the data and write it out row by row.
