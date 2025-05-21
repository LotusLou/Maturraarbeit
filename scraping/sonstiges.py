def neubad_datum(raw_string):
    raw_string = raw_string

    # 1. Wochentag entfernen (alles vor dem ersten Leerzeichen + Punkt)
    parts = raw_string.split(". ", 1)
    date_time_str = parts[1] if len(parts) > 1 else raw_string

    # 2. Datum und Zeit trennen am letzten " - "
    if " - " in date_time_str:
        date_part, time_part = date_time_str.rsplit(" - ", 1)
    else:
        # Fallback: Wenn kein " - " vorhanden ist, Standardwerte setzen
        date_part = date_time_str
        time_part = "00:00"

    # 3. Datum korrekt formatieren
    monate = {
        "JANUAR": "01", "FEBRUAR": "02", "MÄRZ": "03", "APRIL": "04",
        "MAI": "05", "JUNI": "06", "JULI": "07", "AUGUST": "08",
        "SEPTEMBER": "09", "OKTOBER": "10", "NOVEMBER": "11", "DEZEMBER": "12"
    }
    try:
        day, monat, jahr = date_part.split(" ")
        day = day.split(".")
        monat = monat.strip().upper()
        monat = monate[monat]
        jahr = jahr.strip()
        date = f"{jahr}-{monat}-{day[0]}"
    except Exception:
        date = ""
        time_part = "00:00"

    # 4. Zeit
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
