from django.shortcuts import render
from django.views.generic.list import ListView
from django.db import connection, models
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Q
from fire.models import Locations, Incident, FireStation
from datetime import datetime


class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"
    
class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass
    
def PieCountbySeverity(request):
    query = '''
    SELECT severity_level, COUNT(*) as count
    FROM fire_incident
    GROUP BY severity_level
    '''
    data = {}
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    if rows:
        # Construct the dictionary with severity level as keys and count as values
        data = {severity: count for severity, count in rows}
    else:
        data = {}

    return JsonResponse(data)


def LineCountbyMonth(request):

    current_year = datetime.now().year

    result = {month: 0 for month in range(1, 13)}

    incidents_per_month = Incident.objects.filter(date_time__year=current_year) \
        .values_list('date_time', flat=True)

    # Counting the number of incidents per month
    for date_time in incidents_per_month:
        month = date_time.month
        result[month] += 1

    # If you want to convert month numbers to month names, you can use a dictionary mapping
    month_names = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    result_with_month_names = {
        month_names[int(month)]: count for month, count in result.items()}

    return JsonResponse(result_with_month_names)

def MultilineIncidentTop3Country(request):

    query = '''
        SELECT 
        fl.country,
        strftime('%m', fi.date_time) AS month,
        COUNT(fi.id) AS incident_count
    FROM 
        fire_incident fi
    JOIN 
        fire_locations fl ON fi.location_id = fl.id
    WHERE 
        fl.country IN (
            SELECT 
                fl_top.country
            FROM 
                fire_incident fi_top
            JOIN 
                fire_locations fl_top ON fi_top.location_id = fl_top.id
            WHERE 
                strftime('%Y', fi_top.date_time) = strftime('%Y', 'now')
            GROUP BY 
                fl_top.country
            ORDER BY 
                COUNT(fi_top.id) DESC
            LIMIT 3
        )
        AND strftime('%Y', fi.date_time) = strftime('%Y', 'now')
    GROUP BY 
        fl.country, month
    ORDER BY 
        fl.country, month;
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    # Initialize a dictionary to store the result
    result = {}

    # Initialize a set of months from January to December
    months = set(str(i).zfill(2) for i in range(1, 13))

    # Loop through the query results
    for row in rows:
        country = row[0]
        month = row[1]
        total_incidents = row[2]

        # If the country is not in the result dictionary, initialize it with all months set to zero
        if country not in result:
            result[country] = {month: 0 for month in months}

        # Update the incident count for the corresponding month
        result[country][month] = total_incidents

    # Ensure there are always 3 countries in the result
    while len(result) < 3:
        # Placeholder name for missing countries
        missing_country = f"Country {len(result) + 1}"
        result[missing_country] = {month: 0 for month in months}

    for country in result:
        result[country] = dict(sorted(result[country].items()))

    return JsonResponse(result)

def multipleBarbySeverity(request):
    query = '''
    SELECT 
        fi.severity_level,
        strftime('%m', fi.date_time) AS month,
        COUNT(fi.id) AS incident_count
    FROM 
        fire_incident fi
    GROUP BY fi.severity_level, month
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}
    months = set(str(i).zfill(2) for i in range(1, 13))

    for row in rows:
        level = str(row[0])  # Ensure the severity level is a string
        month = row[1]
        total_incidents = row[2]

        if level not in result:
            result[level] = {month: 0 for month in months}

        result[level][month] = total_incidents

    # Sort months within each severity level
    for level in result:
        result[level] = dict(sorted(result[level].items()))

    return JsonResponse(result)

def map_station(request):
    # Define the static fire station data
    fire_stations = [
        {
            'name': 'Sta. Lourdes Fire Station',
            'latitude': 9.83369118406607,
            'longitude': 118.72275445554,
            'address': 'Near Sta. Lourdes National High School',
            'phone': '(048) 434-7701',
            'coverage': 'Sta. Lourdes Area'
        },
        {
            'name': 'Tagburos Fire Station',
            'latitude': 9.82084079557777,
            'longitude': 118.74401369655,
            'address': 'Near Tagburos Elementary School',
            'phone': '(048) 434-7702',
            'coverage': 'Tagburos Area'
        },
        {
            'name': 'Sicsican Fire Station',
            'latitude': 9.79555573875096,
            'longitude': 118.710565836493,
            'address': 'Near Sicsican Elementary',
            'phone': '(048) 434-7703',
            'coverage': 'Sicsican Area'
        }
    ]

    context = {
        'stations': fire_stations,
    }

    return render(request, 'map_station.html', context)

def map_incidents(request):
    # Get the selected city from the query parameters
    selected_city = request.GET.get('city', '')
    
    # Get all cities that have incidents
    cities = Incident.objects.select_related('location').values_list(
        'location__city', flat=True
    ).distinct().order_by('location__city')
    
    # Base query
    incidents_query = Incident.objects.select_related('location')
    
    # Apply city filter if selected
    if selected_city:
        incidents_query = incidents_query.filter(location__city=selected_city)
    
    # Get the incidents data with all necessary information
    incidents = incidents_query.values(
        'location__latitude', 
        'location__longitude',
        'severity_level',
        'date_time',
        'location__city',
        'location__address',
        'description'
    ).order_by('-date_time')  # Most recent incidents first

    # Process the incidents data
    incidents_list = []
    for incident in incidents:
        incidents_list.append({
            'latitude': float(incident['location__latitude']),
            'longitude': float(incident['location__longitude']),
            'severity_level': incident['severity_level'],
            'date_time': incident['date_time'].strftime('%Y-%m-%d %H:%M:%S'),
            'city': incident['location__city'],
            'address': incident['location__address'],
            'description': incident['description']
        })

    # Get statistics for each city
    city_stats = {}
    for city in cities:
        stats = Incident.objects.filter(location__city=city).aggregate(
            total=models.Count('id'),
            minor=models.Count('id', filter=Q(severity_level='Minor Fire')),
            moderate=models.Count('id', filter=Q(severity_level='Moderate Fire')),
            major=models.Count('id', filter=Q(severity_level='Major Fire'))
        )
        city_stats[city] = stats

    context = {
        'incidents': incidents_list,
        'cities': cities,
        'selected_city': selected_city,
        'city_stats': city_stats,
    }

    return render(request, 'map_incidents.html', context)