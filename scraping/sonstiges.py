import datetime


def datum_formatieren(date_part, monate):
    try:
        day, monat, jahr = date_part.split(" ")
        day = day.split(".")
        monat = monat.strip()
        monat = monate[monat]
        jahr = jahr.strip()
        date = f"{jahr}-{monat}-{day[0]}"
    except Exception:
        date = ""
    return date


def neubad_datum(raw_string):
    # 1. Wochentag entfernen (alles vor dem ersten Leerzeichen + Punkt)
    parts = raw_string.split(". ", 1)
    date_time_str = parts[1] if len(parts) > 1 else raw_string

    # 2. Datum und Zeit trennen am letzten " - "
    if " - " in date_time_str:
        date_part, time_part = date_time_str.rsplit(" - ", 1)
    else:
        date_part = date_time_str
        time_part = "00:00"

    m1 = {
        "JANUAR": "01",
        "FEBRUAR": "02",
        "MÄRZ": "03",
        "APRIL": "04",
        "MAI": "05",
        "JUNI": "06",
        "JULI": "07",
        "AUGUST": "08",
        "SEPTEMBER": "09",
        "OKTOBER": "10",
        "NOVEMBER": "11",
        "DEZEMBER": "12",
    }
    date = datum_formatieren(date_part, m1)

    # Zeit ggf. auf "00:00:00" normalisieren
    if ":" in time_part:
        parts = time_part.split(":")
        if len(parts) == 2:
            time = f"{parts[0]}:{parts[1]}:00"
        elif len(parts) == 3:
            time = f"{parts[0]}:{parts[1]}:{parts[2]}"
        else:
            time = "00:00:00"
    else:
        time = "00:00:00"
    date_time = [date, time]
    return date_time


def bar59_datum(raw_string):
    parts = raw_string.split(" ")
    day, month, year = parts[1].split(".")
    date_str = f"{year}-{month}-{day}"
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    return date_obj


def treibhaus_datum(raw_string):
    # Erwartet: "Mai 23, 2025 00:00" oder ähnlich
    # Teile am Leerzeichen, um Monat, Tag, Jahr und ggf. Zeit zu extrahieren
    parts = raw_string.replace(",", "").split()
    if len(parts) < 3:
        return None
    month, day, year = parts[0], parts[1], parts[2]
    m1 = {
        "Januar": "01", "Februar": "02", "März": "03", "April": "04",
        "Mai": "05", "Juni": "06", "Juli": "07", "August": "08",
        "September": "09", "Oktober": "10", "November": "11", "Dezember": "12"
    }
    
    date_str = f"{year}-{m1[month]}-{day.zfill(2)}" #zfill macht aus zb aus 3 -> 03 
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj



def today():
    heute_date_time = datetime.datetime.now()
    heute_date = heute_date_time.date()
    heute_time = heute_date_time.time().replace(microsecond=0)
    return heute_date, heute_time
