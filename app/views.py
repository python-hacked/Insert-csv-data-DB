import io
import csv
from django.shortcuts import render
from .models import Stock


def insert_data(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string)  # Skip the header row

        for row in csv.reader(io_string, delimiter=','):
            date = row[0]
            open_price = float(row[1])
            high_price = float(row[2])
            low_price = float(row[3])
            close_price = float(row[4])
            adj_close_price = float(row[5])
            volume = int(row[6])

            Stock.objects.create(
                date=date,
                open=open_price,
                high=high_price,
                low=low_price,
                close=close_price,
                adj_close=adj_close_price,
                volume=volume
            )

        return render(request, 'success.html')

    return render(request, 'insert.html')


def stock_list(request):
    search_query = request.GET.get('search')

    if search_query:
        stocks = Stock.objects.filter(volume__icontains=search_query)
    else:
        stocks = Stock.objects.all()

    return render(request, 'stock_list.html', {'stocks': stocks})
