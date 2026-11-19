# Horarios compartidos por colaborador local el 18/11/2026; pendientes de validación parroquial.
CHURCHES = [
    {
        "id": 1,
        "name": "Parroquia La Sagrada Familia",
        "city": "San Miguel",
        "department": "San Miguel",
        "address": "Colonia Belén, San Miguel, El Salvador",
        "phone": "2661-4298",
        "verified": False,
        "schedule_status": "community_reported",
        "schedule_note": "Horario aportado por un colaborador local; confirmar con secretaría.",
        "chapel": True,
        "source_url": "https://diocesisdesanmiguelsv.org/vicaria-san-miguel-arcangel/",
        "masses": [
            {"days": "Martes a sábado", "times": ["18:00"]},
            {"days": "Domingo", "times": ["06:00", "10:00", "18:00"]},
        ],
    },
    {
        "id": 2,
        "name": "Catedral Basílica Reina de la Paz",
        "city": "San Miguel",
        "department": "San Miguel",
        "address": "Barrio El Centro, San Miguel, El Salvador",
        "phone": "2661-1979",
        "verified": False,
        "schedule_status": "community_reported",
        "schedule_note": "Horarios habituales aportados por el usuario con referencias a Facebook y Google; hay discrepancias en las misas dominicales. Confirmar con oficina parroquial antes de asistir. Los horarios de apertura también son orientativos.",
        "chapel": False,
        "source_url": "https://www.facebook.com/100064638014323/posts/horarios-de-misas-en-catedral-bas%C3%ADlica/479692503615641/",
        "masses": [
            {"days": "Martes a sábado", "times": ["05:30"]},
            {"days": "Domingo (horarios habituales reportados)", "times": ["05:30", "08:30", "17:00"]},
        ],
        "unconfirmed_masses": [
            {"days": "Domingo (horarios alternativos reportados)", "times": ["06:00", "07:30", "09:00", "11:30", "16:00", "17:30"]},
        ],
        "opening_hours": [
            {"days": "Lunes", "open": "05:30", "close": "18:00"},
            {"days": "Martes y miércoles", "open": "05:30", "close": "18:00"},
            {"days": "Jueves", "open": "05:30", "close": "17:30"},
            {"days": "Viernes", "open": "05:30", "close": "18:00"},
            {"days": "Sábado", "open": "05:30", "close": "18:30"},
            {"days": "Domingo", "open": "05:30", "close": "20:00"},
        ],
    },
]
