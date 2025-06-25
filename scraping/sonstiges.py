import datetime
from datetime import datetime, date, time

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

    date_time_str = raw_string.replace("\nZum Kalender hinzufügen", "").strip()
    # 1. Wochentag entfernen (alles vor dem ersten Leerzeichen + Punkt)
    parts = date_time_str.split(". ", 1)
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

def neubad_datum2(date_str, time_str, Endtime):
    print(f"Debug - neubad_datum2 Input: date_str='{date_str}', time_str='{time_str}'")
    
    # Strings in Python date/time Objekte umwandeln
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        print(f"Debug - Date object created: {date_obj}")
    except Exception as e:
        print(f"Debug - Fehler beim Parsen des Datums '{date_str}': {e}")
        date_obj = None
        
    try:
        # Zeit kann sowohl "HH:MM:SS" als auch "HH:MM" Format haben
        if len(time_str.split(':')) == 2:
            time_obj = datetime.strptime(time_str, "%H:%M").time()
        else:
            time_obj = datetime.strptime(time_str, "%H:%M:%S").time()
        print(f"Debug - Time object created: {time_obj}")
    except Exception as e:
        print(f"Debug - Fehler beim Parsen der Zeit '{time_str}': {e}")
        time_obj = None
        
    if Endtime and len(Endtime) > 0 and Endtime[0].text:
        endtime_text = Endtime[0].text.strip()
        print(f"Debug - Endtime text: '{endtime_text}'")
        try:
            if ":" in endtime_text:
                if len(endtime_text.split(':')) == 2:
                    endtime_obj = datetime.strptime(endtime_text, "%H:%M").time()
                else:
                    endtime_obj = datetime.strptime(endtime_text, "%H:%M:%S").time()
            else:
                endtime_obj = None
        except Exception as e:
            print(f"Debug - Fehler beim Parsen der Endzeit '{endtime_text}': {e}")
            endtime_obj = None
    else:
        endtime_obj = None
        
    print(f"Debug - Final objects: date_obj={date_obj}, time_obj={time_obj}, endtime_obj={endtime_obj}")
    return date_obj, time_obj, endtime_obj

def bar59_datum(raw_string):
    parts = raw_string.split(" ")
    day, month, year = parts[1].split(".")
    date_str = f"{year}-{month}-{day}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    return date_obj


def treibhaus_datum(raw_string, time_str, endtime_el):
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
    
    date_str = f"{year}-{m1[month]}-{day.zfill(2)}" #zfill macht aus  zb aus 3 -> 03 
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    try:
        time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
    except Exception:
        time_obj = None
        endtime_str = endtime_el[0].text if endtime_el else ""
    try:
        endtime_obj = datetime.strptime(endtime_str, "%H:%M").time() if endtime_str else None
    except Exception:
        endtime_obj = None
    return date_obj, time_obj, endtime_obj

def madeleine_datum(rawstring):
    #test_input = "24.05.2025 23:00 - 04:00 Uhr"
    parts = rawstring.replace(" Uhr", "").replace("-", "").split()
    day, month, year = parts[0].split(".")
    date_str = f"{year}-{month}-{day.zfill(2)}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    time_str = parts[1]
    endtime_str = parts[2]

    try:
        time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
    except Exception:
        time_obj = None
    try:
        endtime_obj = datetime.strptime(endtime_str, "%H:%M").time() if endtime_str else None
    except Exception:
        endtime_obj = None
    return date_obj, time_obj, endtime_obj

def rok_datum(month, day, year):
    month = month.strip()
    day = day.strip()
    m1 = {
        "Januar": "01", "Februar": "02", "März": "03", "April": "04",
        "Mai": "05", "Juni": "06", "Juli": "07", "August": "08",
        "September": "09", "Oktober": "10", "November": "11", "Dezember": "12"
    }
    # Monat-String ggf. auf ersten Buchstaben groß, Rest klein normalisieren
    month_norm = month.capitalize()
    if month_norm not in m1:
        # Fallback: gib None zurück, wenn der Monat nicht gefunden wird
        return None
    date_str = f"{year}-{m1[month_norm]}-{day.zfill(2)}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj
def sudpol_datum(Date_Starttime):
    #Beispiel Datum: Sa, 14.06.2025, 23:00
    parts = Date_Starttime.split(", ")
    day, month, year = parts[1].split(".")
    date_str = f"{year}-{month}-{day.zfill(2)}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    time_str = parts[2]
    try:
        time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
    except Exception:
        time_obj = None
    return date_obj, time_obj

def sedel_datum(date_time):
    #Beispiel: 2025-06-07T20:00:00Z
    date, time = date_time.split("T")
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    time_str = time.rsplit("Z")
    time_obj = datetime.strptime(time_str[0], "%H:%M:%S").time() 
    return date_obj, time_obj


def schwarzeschaf_datum(date_str):
        try:
            # Entfernt alles, was kein Datum ist
            clean = date_str.strip()
            return datetime.strptime(clean, "%d.%m.%Y").date()
        except Exception as e:
            print(f" Fehler beim Parsen: {date_str} → {e}")
            return None

def schwarzeschafe_titel(Title, Title2 ):
    Title_single = Title 
    Title_block2 = Title2[-2]  # vorletztes Element
    Title_block3 = Title2[-1]  # letztes Element
    raw_block = [el.text.strip() for el in Title_single if el.text.strip()]
    raw_block2 = Title_block2.text
    raw_block3 = Title_block3.text
    split_block2 = [t.strip() for t in raw_block2.split("\n") if t.strip()] #\n steht für zeilen umbruch so kann man beim zeilen umbruch spliten 
    split_block3 = [t.strip() for t in raw_block3.split("\n") if t.strip()]
    titles = raw_block + split_block2 + split_block3 # alle Titel in eine Liste einfügen
    return (titles)
def today():
    heute_date_time = datetime.now()
    heute_date = heute_date_time.date()
    heute_time = heute_date_time.time().replace(microsecond=0)
    return heute_date, heute_time



